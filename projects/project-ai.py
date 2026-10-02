import sys
import requests

sys.stdout.reconfigure(encoding='utf-8')

prompt = input("Masukkan Teks Untuk Input: ")

resp = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "openbmb/MiniCPM5-2B:latest",
        "messages": [{"role": "user", "content": prompt}],
        "stream": True
    }
)

print(resp.json()["message"]["content"])
