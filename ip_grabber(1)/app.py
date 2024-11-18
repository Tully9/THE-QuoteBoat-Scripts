from flask import Flask, render_template, request
import socket
import uuid
import platform
from datetime import datetime
import requests

app = Flask(__name__)

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        return response.json().get('ip', 'Unknown')
    except Exception:
        return "Unable to fetch public IP"

@app.route("/")
def display_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2 * 6, 8)][::-1]) 
    public_ip = get_public_ip() 
    os_info = platform.system() + " " + platform.release()
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    user_agent = request.headers.get('User-Agent', 'Unknown')

    system_info = {
        "hostname": hostname,
        "ip_address": ip_address,
        "public_ip": public_ip,
        "mac_address": mac_address,
        "os_info": os_info,
        "current_time": current_time,
        "user_agent": user_agent,
    }

    return render_template("info.html", system_info=system_info)

if __name__ == "__main__":
    app.run(debug=True)
