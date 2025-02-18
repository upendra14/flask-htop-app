from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Upendra Kumar"
    username = os.getlogin()
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    top_output = subprocess.getoutput("top -b -n 1 | head -20")

    response = f"""
    <html>
    <head><title>HTop Info</title></head>
    <body>
        <h1>System Information</h1>
        <p><b>Name:</b> {name}</p>
        <p><b>Username:</b> {username}</p>
        <p><b>Server Time (IST):</b> {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</p>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
