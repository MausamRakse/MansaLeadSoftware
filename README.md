# Mansa_infotech-lead-app

# Apollo Lead Extraction System

A powerful, dual-interface lead extraction tool strictly integrated with the Apollo.io API and CountryStateCity API. The system allows users to search, filter, and extract business contacts either through structured filters or a natural language AI prompt, and save the extracted data directly to a local CSV database.

## 🚀 Features

- **Filter Mode**: Search for leads using specific criteria like Industry, Job Title, Company Size, Location (dynamic Country/State/City dropdowns), and custom keywords.
- **AI Prompt Mode**: Type natural language queries (e.g. *"Find founders or CEOs in AI startups with 1–200 employees"*) and let the backend automatically parse them into filters.
- **Contact Enrichment**: Unlock full contact info (emails, phone numbers, and LinkedIn profiles) on a per-lead basis to conserve Apollo API credits.
- **Local Database**: All unlocked leads are correctly formatted, safely quoted, and stored in a persistent `data.csv` backend file.
- **Easy Export**: Safely download the current search results as JSON or download the entire historical raw database (`data.csv`) directly via the UI.

## 📁 Project Structure

```text
apollo/
├── backend/
│   ├── main.py            # FastAPI backend server with Apollo integrations
│   ├── data.csv           # Persistent backend storage for extracted leads
│   ├── requirements.txt   # Python backend dependencies
│   ├── .env               # Environment API Keys (Apollo & CSC)
│   └── venv/              # Python virtual environment
├── frontend/
│   ├── index.html         # Main entry point (loads React & Babel standalone)
│   └── App.jsx            # Main React application logic and UI
└── README.md              # Project documentation
```

## 🛠 Prerequisites

- Python 3.8+
- An [Apollo.io API Key](https://www.apollo.io/)
- A [CountryStateCity API Key](https://countrystatecity.in/)

## ⚙️ Setup Instructions

**1. Clone or Download the Repository**
Navigate to the project root directory (`apollo/`).

**2. Configure Environment Variables**
Inside the `backend/` folder, create a `.env` file (or duplicate `.env.example` if it exists) and add your API keys:
```env
APOLLO_API_KEY=your_apollo_api_key_here
CSC_API_KEY=your_country_state_city_api_key_here
```

**3. Install Backend Dependencies**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🏃‍♂️ Running the Application

To start the Lead Extraction System, you need to run both the backend and frontend simultaneously in separate terminal windows.

**Start the Backend (Terminal 1)**
```bash
cd backend
source venv/bin/activate
uvicorn main:app --reload --port 8000
```

**Start the Frontend (Terminal 2)**
```bash
cd frontend
python3 -m http.server 3000
```

Once both servers are running, open your web browser and navigate to:
**👉 http://localhost:3000**

## 💻 Tech Stack

- **Frontend**: React.js (via Babel standalone), Plain CSS, Axios
- **Backend**: FastAPI, Uvicorn, Python `httpx`, Python `csv` module
- **APIs**: Apollo.io REST API, CountryStateCity API

---
*Built to streamline the B2B sales and lead generation pipeline.*
