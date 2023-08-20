from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/monitor')
def monitor():
    # Run RHEL commands and capture output
    cpu_info = subprocess.getoutput("top -n 1")
    memory_info = subprocess.getoutput("free -h")
    disk_info = subprocess.getoutput("df -h")

    return render_template('monitor.html', cpu_info=cpu_info, memory_info=memory_info, disk_info=disk_info)

if __name__ == '__main__':
    app.run(debug=True)
