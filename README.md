# Age Calculator Flask Application

A simple Python Flask web application that takes a user's date of birth as input and calculates their current age. The app includes CSS and JavaScript for basic styling and validation, and comes with a Dockerfile for easy containerization.

---

## Application Structure

age-calculator-app/
│
├── app.py
├── requirements.txt
├── Dockerfile
│
├── templates/
│   └── index.html
│
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js



- `app.py` — Main Flask app script  
- `requirements.txt` — Python dependencies  
- `Dockerfile` — Docker build instructions  
- `templates/index.html` — HTML template with linked CSS and JS  
- `static/css/style.css` — Styling for the app  
- `static/js/script.js` — Basic client-side validation

---

## Prerequisites

- Python 3.6+ installed  
- `pip` (Python package manager) installed  
- (Optional) Docker installed for containerized deployment

---

## Setup & Run Locally (without Docker)

1. **Clone the repository**
git clone <YOUR_REPO_URL>
cd age-calculator-app

#Install dependencies:
pip install -r requirements.txt
python app.py

#Build the Docker image
docker build -t age-calculator-app .

#Run the Docker container
docker run -p 5000:5000 age-calculator-app

#Open your browser and visit
http://localhost:5000





