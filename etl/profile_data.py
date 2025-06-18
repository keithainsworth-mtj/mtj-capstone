import os
import pandas as pd
import ollama
from pathlib import Path
import json

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / 'data'
OUTPUT_CSV = BASE_DIR / 'governance/catalog.csv'
OUTPUT_JSON = BASE_DIR / 'governance/column_notes.json'

metadata = []

for year_dir in sorted(DATA_DIR.glob('20*')):
    for csv_file in year_dir.glob('*.csv'):
        print(f'🔍 Profiling {csv_file.name}...')

        try:
            df = pd.read_csv(csv_file, nrows=100)  # Sample 100 rows
        except Exception as e:
            print(f'⚠️ Skipping {csv_file.name}: {e}')
            continue

        for col in df.columns:
            sample_vals = df[col].dropna().astype(str).unique()[:5].tolist()
            prompt = f"""
You are a data cataloging assistant. Given the column name "{col}" and the following sample values: {sample_vals}, describe in 1 sentence what this column most likely represents. Be concise, business-relevant, and avoid guessing wildly.
"""
            try:
                response = ollama.chat(model='mistral', messages=[{"role": "user", "content": prompt}])
                ai_description = response['message']['content'].strip()
            except Exception as e:
                ai_description = f"⚠️ Failed to get response: {e}"

            metadata.append({
                'file': csv_file.name,
                'column': col,
                'sample_values': sample_vals,
                'llm_description': ai_description
            })

# Save catalog
pd.DataFrame(metadata).to_csv(OUTPUT_CSV, index=False)

# Save descriptions as JSON (for optional UI use)
with open(OUTPUT_JSON, 'w') as f:
    json.dump(metadata, f, indent=2)

print(f"\n✅ Metadata profiling complete. Saved to:\n- {OUTPUT_CSV}\n- {OUTPUT_JSON}")