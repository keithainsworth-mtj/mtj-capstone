from nicegui import ui
import pandas as pd
from pathlib import Path

# Load catalog
CATALOG_PATH = Path(__file__).resolve().parent.parent / 'governance/catalog.csv'

@ui.page('/')
def home():
    ui.label('🧠 MTJ Capstone: Metadata Catalog Viewer').classes('text-2xl font-bold mb-4')
    ui.label('This table shows AI-generated metadata about the Open Payments data files.')

    try:
        df = pd.read_csv(CATALOG_PATH)
    except Exception as e:
        ui.label(f"❌ Failed to load catalog.csv: {e}")
        return

    if df.empty:
        ui.label('⚠️ No metadata found.')
        return

    # Show table with key columns
        # Show table with responsive, wrapped, left-aligned columns
        # Force wrapping and prevent horizontal scroll on all pages
    with ui.table(
        columns=[
            {
                'name': 'file',
                'label': 'File',
                'field': 'file',
                'align': 'left',
                'style': 'white-space: normal; word-break: break-word;'
            },
            {
                'name': 'column',
                'label': 'Column Name',
                'field': 'column',
                'align': 'left',
                'style': 'white-space: normal; word-break: break-word;'
            },
            {
                'name': 'sample_values',
                'label': 'Sample Values',
                'field': 'sample_values',
                'align': 'left',
                'style': 'white-space: normal; word-break: break-word;'
            },
            {
                'name': 'llm_description',
                'label': 'AI Description',
                'field': 'llm_description',
                'align': 'left',
                'style': 'white-space: normal; word-break: break-word;'
            },
        ],
        rows=df.to_dict(orient='records'),
        row_key='column',
        pagination=20
    ).classes('w-full max-w-full text-left text-sm'):
        pass

# Run the app
ui.run()