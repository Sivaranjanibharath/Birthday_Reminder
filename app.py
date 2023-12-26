from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    """
    This is the entry point for birthday reminder website.
    This page allows users to register birthday reminders for their loved ones
    """
    return render_template('index.html')


@app.route('/send_birthday_reminder', methods=['POST'])
def send_birthday_reminder():
    """
    This function gets the name and dob input from the user's form submit action and stores them in sqlite db
    :return: redirect to home page
    """
    name = request.form.get('name')
    date = request.form.get('date')

    if not name or not date:
        return "Invalid input. Please provide both name and date."

    # Store birthday in SQLite
    connection = sqlite3.connect('birthdays.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO birthdays (name, date) VALUES (?, ?)', (name, date))
    connection.commit()
    connection.close()
    print(f"Sucessfully registered birthday reminder for {name} on {date}")
    return redirect(url_for('index'))


if __name__ == '__main__':
    """
    Flask entry point
    """
    app.run(debug=True)
