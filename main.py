import socket
import time
import requests
import os

SERVER_IP = os.getenv("SERVER_IP")
SERVER_PORT = int(os.getenv("SERVER_PORT"))
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
CHECK_INTERVAL = 300  # 5 minutes

was_online = None

def is_server_online(ip, port, timeout=5):
    try:
        with socket.create_connection((ip, port), timeout=timeout):
            return True
    except:
        return False

def send_discord_message(content):
    data = {"content": content}
    try:
        requests.post(WEBHOOK_URL, json=data)
    except Exception as e:
        print("Failed to send message:", e)

while True:
    online = is_server_online(SERVER_IP, SERVER_PORT)

    if was_online is None:
        was_online = online
    elif online != was_online:
        if online:
            send_discord_message("🟢 **Project P.A.L.E. is now ONLINE.**")
        else:
            send_discord_message("🔴 **Project P.A.L.E. is now OFFLINE.**")
        was_online = online

    print(f"[Status Check] Server is {'ONLINE' if online else 'OFFLINE'}")
    time.sleep(CHECK_INTERVAL)
