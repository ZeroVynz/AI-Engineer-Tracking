import sys
import ollama
from ollama import chat

# Memastikan console Windows bisa menampilkan emoji/karakter Unicode tanpa crash
sys.stdout.reconfigure(encoding='utf-8')


messages = [
    {
        "role": "user",
        "content": input("Masukkan Teks Untuk Input: "),
    },
]

response = chat(model="openbmb/MiniCPM5-2B:latest", messages=messages)
print(response.message.content)
