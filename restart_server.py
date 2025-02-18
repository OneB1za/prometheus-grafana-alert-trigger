#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess

HOST = "0.0.0.0"
PORT = 5000

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        """Обрабатывает POST-запрос для перезапуска контейнера"""
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Django Restarting...\n")

        # Запускаем Bash-скрипт для перезапуска контейнера
        subprocess.run(["./restart_django.sh"], check=False)

        print("Received POST request, restarting Django container...")

if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), RequestHandler)
    print(f"Starting HTTP server on {HOST}:{PORT}...")
    server.serve_forever()
