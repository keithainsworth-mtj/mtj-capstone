# MTJ Capstone — AI-Powered Health Data Profiling & Governance

This project demonstrates how to use **local LLMs**, open healthcare datasets, and modern data tools to build an intelligent data profiling and governance platform. It uses the **Open Payments** dataset from CMS (Centers for Medicare & Medicaid Services) to showcase how AI can make data more discoverable, trustworthy, and analyzable.

---

## 🚀 Project Goals

- Ingest and profile Open Payments healthcare data (2017–2023)
- Use **local AI models via [Ollama](https://ollama.com/)** to classify and interpret raw data columns
- Generate a **metadata catalog** to power data governance
- Deploy a lightweight **interactive UI** for data exploration (hosted on [Render](https://render.com))
- Demonstrate how AI can assist responsibly and securely in real business workflows

---

## 🧠 AI Integration

This project uses **Mistral (via Ollama)** locally to:
- Interpret column names and sample values
- Generate plain-English descriptions of each field
- Assist in understanding large or inconsistent datasets
- Output a `catalog.csv` for governance and a JSON `column_notes.json` for deeper insight

> **Note:** Ollama-powered tasks run locally and are not included in the Render deployment.

---

## 🗂 Project Structure

```
mtj_capstone/
├── app/                    # Frontend app (NiceGUI or Streamlit)
│   └── main.py
├── data/                   # Raw Open Payments data (NOT committed)
│   └── 2017/ ... 2023/
├── etl/                    # Ingestion and profiling scripts
│   └── profile_data.py
├── governance/             # AI-generated metadata outputs
│   └── catalog.csv
│   └── column_notes.json
├── notebooks/              # (Optional) Jupyter notebooks
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📦 Requirements

- Python 3.10+
- [Ollama](https://ollama.com) with `mistral` or `llama3` model installed
- Recommended: Create a virtual environment

```bash
pip install -r requirements.txt
```

---

## 🧪 Usage

### 1. Generate metadata locally with Ollama:
```bash
ollama run mistral
python etl/profile_data.py
```

### 2. Run the local UI (e.g., NiceGUI):
```bash
python app/main.py
```

### 3. Or deploy to [Render](https://render.com) using GitHub integration

---

## 📊 Live Demo (Optional)

[https://mtj-capstone.onrender.com](#)

---

## 🔐 Disclaimer

Raw data is excluded for size and privacy. You can download the Open Payments dataset from [CMS Open Payments](https://openpaymentsdata.cms.gov/).

---

## 📜 License

MIT — for educational and portfolio use.
