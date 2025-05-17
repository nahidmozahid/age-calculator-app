from flask import Flask, render_template, request
from datetime import datetime, date

app = Flask(__name__)

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

@app.route('/', methods=['GET', 'POST'])
def home():
    age = None
    if request.method == 'POST':
        dob_str = request.form.get('dob')
        if dob_str:
            try:
                birthdate = datetime.strptime(dob_str, '%Y-%m-%d').date()
                age = calculate_age(birthdate)
            except ValueError:
                age = "Invalid date format!"
    return render_template('index.html', age=age)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
