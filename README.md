# 🧠 Freelance Order Aggregator API

## 📌 Goal

Create a unified API that fetches and aggregates freelance job listings or order requests from multiple platforms including:

- Upwork  
- Fiverr  
- Freelancer  
- PeoplePerHour  
- Toptal  
- Reddit (e.g., [r/forhire](https://reddit.com/r/forhire))

---

## ⚙️ Tech Stack

| Layer              | Technology                        |
|--------------------|-----------------------------------|
| **Backend**        | [FastAPI](https://fastapi.tiangolo.com/) or Flask |
| **Database**       | PostgreSQL (prod) / SQLite (dev)  |
| **Scraping/API**   | `requests`, `BeautifulSoup`, or official APIs |
| **Scheduler**      | `cron`, `APScheduler`, or GitHub Actions |
| **Auth (optional)**| OAuth 2.0 / API keys              |
| **Deployment**     | GitHub Pages, Railway, Render, Fly.io |

---

## 🧱 Project Structure

```bash
freelance-aggregator-api/
├── app/
│   ├── main.py
│   ├── routers/
│   │   ├── upwork.py
│   │   ├── fiverr.py
│   │   └── freelancer.py
│   ├── models/
│   │   └── job.py
│   └── services/
│       └── fetch_jobs.py
├── data/
│   └── jobs.db
├── requirements.txt
├── README.md
└── .env
```

---

## 📦 API Features – Phase 1

| Endpoint             | Method | Description                                          |
|----------------------|--------|------------------------------------------------------|
| `/jobs`              | GET    | Fetch all aggregated job listings                   |
| `/jobs/{platform}`   | GET    | Filter jobs by platform (e.g., `upwork`, `fiverr`)  |
| `/refresh`           | POST   | Manually trigger a job refresh (or scheduled cron)  |

---

## 🔧 Setup & Run Locally

```bash
git clone https://github.com/your-username/freelance-aggregator-api.git
cd freelance-aggregator-api
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 📌 Roadmap

- [ ] Add scraping logic per platform
- [ ] Store jobs in local DB (SQLite)
- [ ] Implement pagination & filtering
- [ ] Add GitHub Actions for scheduled scraping
- [ ] Optional frontend to view jobs

---

## 📄 License

[Unlicense](https://unlicense.org/) — free for personal and commercial use.

---

## ✨ Author

[chatgpt.com](https://chat.openai.com) ✨  
