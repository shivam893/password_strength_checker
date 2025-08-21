🔐 Password Strength Checker

A simple web app that checks how strong your password is.
It looks at:

Password length

Use of uppercase, lowercase, numbers, symbols

Common weak passwords like 123456, password, qwerty

👉 Live Website: Password Strength Checker

🚀 Features

Detects Weak / Normal / Strong passwords

Suggests improvements for weak ones

Blocks common weak passwords

Clean and simple UI

Works online (deployed on Render)

🛠️ Tech Used

Python (Flask)

HTML, CSS

Render (Hosting)

📂 Project Files
app.py              → Flask app code
requirements.txt    → Python dependencies
Procfile            → For Render deployment
weak_passwords.json → Common weak passwords list
templates/          → HTML file
static/             → CSS file

⚡ Run on Your Computer

Clone this repo

git clone https://github.com/shivam893/password_strength_checker.git
cd password_strength_checker


Make virtual environment & activate it

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate   # Mac/Linux


Install dependencies

pip install -r requirements.txt


Start the app

python app.py


Open in browser:

http://127.0.0.1:5000/

👨‍💻 Author

Shivam Nakhate – Cyber Security Engineer

GitHub: shivam893
