# Sikkim Monastery Digitization

A web-based platform designed to digitize, manage, and explore monastery landmarks across Sikkim.  
The project combines cultural preservation with interactive mapping to make heritage data easily accessible.

---

## 🌄 Project Overview

Sikkim Monastery Digitization is an academic project developed to document and visualize monastery landmarks across different districts of Sikkim.  
It provides an interactive interface where users can explore locations, view details, and navigate using map-based features.

The platform focuses on:
- Cultural heritage preservation
- Geographic visualization
- Clean and user-friendly design

---

## 🚀 Features

- 🗺️ Interactive map view using Leaflet.js  
- 📍 Monastery landmarks categorized by district and type  
- 🔎 Search & filter functionality  
- 🧭 Get directions using live location  
- 🖼️ Media support for monastery images  
- 📱 Responsive UI  
- 🧱 Structured backend using Django  

---

## 🛠️ Tech Stack

**Backend**
- Django
- SQLite (development)
- PostgreSQL (production-ready via environment configuration)

**Frontend**
- HTML, CSS, JavaScript
- Leaflet.js

**Libraries & Tools**
- Pillow
- python-dotenv
- python-decouple
- psycopg2-binary

---

## 📂 Project Structure

visitsikkim_project/
│
├── main/ # Django app (models, views, urls)
├── templates/ # HTML templates
├── static/ # Static assets
├── media/ # Uploaded images
├── visitsikkim_project/ # Project settings
├── manage.py
└── requirements.txt

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/vishaldhara31/sikkim-monastery-digitization.git
cd sikkim-monastery-digitization
```

2. Create and activate virtual environment
python -m venv env
env\Scripts\activate   # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run migrations
python manage.py migrate

5. Start the development server
python manage.py runserver

Open in browser:
http://127.0.0.1:8000/

## 🔐 Environment Variables
Sensitive values are managed using environment variables.

Example .env file (not included in repository):

SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=*
DATABASE_URL=your-database-url (optional)


## 🎓 Project Type
- Academic Project

- Cultural Heritage Digitization

- Full-stack Web Application


## 📌 Future Enhancements

- User authentication & profiles

- Admin dashboard improvements

- Advanced analytics

- Multilingual support

- Cloud deployment


## 👤 Author
Vishal Dhara
Web & Data Engineering Enthusiast

## 📜 License
This project is intended for academic and educational use.
