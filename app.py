from flask import Flask, render_template, request, redirect, url_for, flash, session
import pyodbc
import joblib
import datetime
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load ML model
model = joblib.load('model.pkl')

# DB connection to SQL Server (edit below with your info)


def connect_db():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=GIMZR;'  # replace with your SSMS server name
        'DATABASE=WSN_Database;'                    # replace with your actual database
        'Trusted_Connection=yes;'
    )


# Home redirect
@app.route('/')
def index():
    return redirect(url_for('login'))

# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        passwd = request.form['password']
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", uname, passwd)
        user = cursor.fetchone()
        conn.close()
        if user:
            session['username'] = uname
            return redirect(url_for('user_home', username=uname))
        else:
            flash("Invalid username or password.")
    return render_template('login.html')

# User signup
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        uname = request.form['username']
        passwd = request.form['password']
        conn = connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", uname, passwd)
            conn.commit()
            flash("Signup successful! Please log in.")
            return redirect(url_for('login'))
        except:
            flash("Username already exists.")
        finally:
            conn.close()
    return render_template('signup.html')

# Home after login
@app.route('/home/<username>')
def user_home(username):
    if 'username' in session and session['username'] == username:
        return render_template('home.html', username=username)
    else:
        flash("Please login first.")
        return redirect(url_for('login'))

# Logout
@app.route('/logout/<username>')
def logout(username):
    session.pop('username', None)
    flash("Logged out successfully.")
    return redirect(url_for('login'))

# Predict route
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction = None
    if 'username' not in session:
        flash("You must be logged in to access predictions.")
        return redirect(url_for('login'))

    if request.method == 'POST':
        dist = float(request.form['Dist_To_CH'])
        energy = float(request.form['Expaned_Energy'])
        code = int(request.form['send_code'])

        input_data = [[dist, energy, code]]
        result = model.predict(input_data)[0]
        prediction = 'Normal' if result == 0 else 'Attack'

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO predictions (username, input_data, predicted_class, timestamp) VALUES (?, ?, ?, ?)",
            session['username'], json.dumps(input_data), prediction, datetime.datetime.now()
        )
        conn.commit()
        conn.close()

    return render_template('predict.html', prediction=prediction)

# Dashboard page
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT predicted_class, COUNT(*) FROM predictions GROUP BY predicted_class")
    results = cursor.fetchall()
    labels = [row[0] for row in results]
    values = [row[1] for row in results]
    conn.close()

    return render_template('dashboard.html', labels=labels, values=values)

# About
@app.route('/about')
def about():
    return render_template('about.html')

# Contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Run
if __name__ == '__main__':
    app.run(debug=True)
