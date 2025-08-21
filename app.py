from flask import Flask, render_template, request
from flask import send_from_directory
app = Flask(__name__)



def check_password_strength(password):
    strength = 0
    remarks = []

    # Rules for strength
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Use at least 8 characters")

    if any(char.isdigit() for char in password):
        strength += 1
    else:
        remarks.append("Add numbers")

    if any(char.isupper() for char in password):
        strength += 1
    else:
        remarks.append("Add uppercase letters")

    if any(char.islower() for char in password):
        strength += 1
    else:
        remarks.append("Add lowercase letters")

    if any(char in "!@#$%^&*()-_=+[]{};:,.<>?/|`~" for char in password):
        strength += 1
    else:
        remarks.append("Add special characters")

    # Strength levels
    if strength <= 2:
        return "Weak", remarks
    elif strength == 3:
        return "Medium", remarks
    else:
        return "Strong", remarks
    
@app.route('/weak_passwords.json')
def weak_passwords():
    return send_from_directory('.', 'weak_passwords.json')

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    suggestions = []
    if request.method == "POST":
        password = request.form["password"]
        result, suggestions = check_password_strength(password)
    return render_template("index.html", result=result, suggestions=suggestions)

if __name__ == "__main__":
    app.run(debug=True)
