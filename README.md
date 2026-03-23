# 📊 Chat-Based Report Generation System

A full-stack application that allows users to generate dynamic reports using natural language queries. Built with **React (frontend)** and **FastAPI/Flask (backend)**, this system interprets user queries and produces data-driven insights from uploaded CSV files.

---

## 🚀 Features

* 💬 Chat-based interface (like ChatGPT)
* 📂 Upload your own CSV dataset
* 🧠 Dynamic query understanding (no hardcoded conditions)
* 📊 Automatic report generation:

  * Tables
  * Charts (Marks & Attendance)
* 🔄 Multi-turn conversation support
* 📥 Export reports as CSV
* 🌙 Dark / ☀️ Light theme toggle
* ⚡ Fully dynamic & data-driven

---

## 🛠️ Tech Stack

### Frontend

* ReactJS (Functional Components + Hooks)
* Recharts (for charts)
* CSS (Custom styling)

### Backend

* Python (FastAPI / Flask)
* Pandas (data processing)
* CSV / JSON (no database)

---

## 📂 Project Structure

```
Chat-Based-Report/
│
├── backend/
│   ├── app.py
│   ├── data_processor.py
│   ├── query_parser.py
│   ├── data_store.py
│   ├── sample_data/
│   │   └── students_extended.csv
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatUI.js
│   │   │   ├── Message.js
│   │   │   ├── ReportTable.js
│   │   │   ├── ChartView.js
│   │   │   └── Sidebar.js
│   │   ├── api.js
│   │   ├── styles.css
│   │   └── App.js
│   └── package.json
│
└── README.md
```

---

## ⚙️ Setup Instructions

### 🔹 Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

---

### 🔹 Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend will run at:

```
http://localhost:3000
```

---

## 📊 Sample Queries

Try these in the chat:

```
Top 3 students with highest marks
List students based on marks in ascending order
Show 5 students
Display lowest attendance students
Show students in grade 10
```

---

## 📂 Upload CSV

* Use the sidebar to upload your dataset
* The system automatically adapts to new columns
* No hardcoding required

---

## 🧠 How It Works

1. User enters a natural language query
2. Backend interprets intent (metric, sorting, limit)
3. Data is processed dynamically using Pandas
4. Results returned as structured JSON
5. Frontend displays:

   * Table
   * Charts
   * Download option

---

## 📈 Charts

* 📊 Marks Distribution
* 📊 Attendance Overview
* Automatically generated based on dataset

---

## 🔥 Key Highlights

* ❌ No hardcoded queries
* ❌ No database required
* ✅ Fully dynamic
* ✅ Works with any CSV
* ✅ Scalable design

---

## 💡 Future Enhancements

* 📊 Multiple chart types (Pie, Line)
* 📁 Multi-dataset switching
* 🧠 AI-powered NLP (LLM integration)
* 📉 Advanced analytics (group by, aggregation)
* 📱 Mobile responsive UI

