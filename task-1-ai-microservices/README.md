# Task 1 – LangFlow + HTML Frontend

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt 
```

2. Run LangFlow:
```bash
langflow run
```

3. In LangFlow UI:
- Go to **Settings → LangFlow API Keys → Add New** to generate your API key. :contentReference[oaicite:1]{index=1}
- Export your flow and get the `FLOW_ID`.

4. Create `.env` using `.env.example`.

5. Start backend:
```bash
uvicorn app:app --reload
```

6. Visit: `http://127.0.0.1:8000/` to access the frontend.

### How It Works

- Frontend sends your prompt.
- Backend (`run_flow.py`) calls LangFlow `/run/{FLOW_ID}` using `x-api-key` header. :contentReference[oaicite:2]{index=2}
- Returns output to display.

