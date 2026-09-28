# Dev Log: Week 1 [19 Sep - 26 Sep 2026]

**Fase 0: Setup** — Status: **Selesai** (6/7 Hari)

---

## 🎯 Ringkasan Minggu Ini

Fokus utama minggu ini adalah menyelesaikan *Fase 0 (Setup)*. Saya berhasil membangun lingkungan kerja lokal, menguasai dasar Git, membuat repositori pertama, dan yang paling penting: berhasil memanggil Local SLM (Small Language Model) menggunakan Python script via HTTP request.

---

## 🧠 Apa yang Dipelajari (What I Learned)

### 1. Git & Version Control

Memahami alur kerja dasar Git untuk manajemen versi dan kolaborasi.

* **Staging & Commit:**
  * `git add .` → Menambahkan semua file di dalam folder (termasuk foldernya).
  * `git add <namafile>` → Menambahkan file spesifik.
  * `git commit -m "message"` → Menyimpan perubahan ke dalam commit.
* **Remote Repository:**
  * `git remote add <namarepo> <urlrepo>` → Menambahkan alias repo (contoh: `origin`).
  * `git remote -v` → Melihat daftar alias repo.
* **Branching & Switching:**
  * `git branch <namabranch>` → Membuat branch baru.
  * `git branch` → Melihat daftar branch.
  * `git switch <namabranch>` → Pindah branch.
  * `git switch -c <namabranch>` → Membuat branch baru sekaligus pindah ke branch tersebut.
* **Push & Delete:**
  * `git push <namarepo> <branch>` (Contoh: `git push origin main`).
  * `git rm` → Menghapus file dari repo dan local.
* 💡 **Tips:** Menggunakan suffix `--cached` (contoh: `git rm --cached <file>`) hanya menghapus file di repo GitHub, tapi tidak menghapusnya di local.

### 2. Python Virtual Environment (venv)

* **Sumber Belajar OOP:** [realpython.com](https://realpython.com)
* **Setup Venv:**
  * Membuat environment: `python -m venv venv`
  * Masuk ke venv (Windows): `venv\Scripts\Activate.ps1`
  * Install dependensi: `pip install -r requirements.txt`
* **Insight Penting:** 
  * Venv bersifat *isolated*. Hanya bisa menggunakan satu versi library tertentu. Jika ingin menggunakan library global, harus di-install ulang di dalam venv.
  * Konsep venv ini adalah cikal bakal dari **Container** (Docker & Kubernetes) yang cakupannya lebih luas.

### 3. Local LLM (Ollama) & Python Integration

* **Model:** Menggunakan `openbmb/MiniCPM5-2B:latest` (di-download dari Hugging Face).

* **Evolusi Script:**
  
  * Awalnya menggunakan `from ollama import call` (masih copas, yang penting jalan).
  * Memahami bahwa `ollama` call hanyalah sebuah *wrapper* dari HTTP request.
  * Sekarang beralih menggunakan library `requests` untuk HTTP POST ke endpoint lokal.

* **HTTP Request:**
  import requests
  
  prompt = input("Masukkan Teks Untuk Input: ")
  resp = requests.post(
  
      "http://localhost:11434/api/chat",
      json={
          "model": "openbmb/MiniCPM5-2B:latest",
          "messages": [{"role": "user", "content": prompt}],
          "stream": True,  # Gen real time tok/s bukan sekaligus
      }
  
  )

* **Insight Penting:**
  
  * LLM API lokal **harus** dijalankan dengan perintah `ollama serve` terlebih dahulu. Jika tidak, akan memicu error pada saat prompting.
  * Parameter `"stream": True` membuat LLM mengeluarkan output token per token secara *real-time* (tok/s), bukan menunggu semuanya selesai baru dimuntahkan sekaligus di akhir.

---

## 🚀 Yang Sudah Dilakukan (Accomplishments)

* ✅ Membuat repo pertama **`AI-Engineer-Tracking`** pada tanggal 19 Sep.
* ✅ Menguasai Git dasar (`push`, `pull`, `commit`, `add`, `branch`, `branch rm`, `switch`, `--cached`).
* ✅ Membuat akun GitHub (GH), Hugging Face (HF), Kaggle, dan Google Colab.
* ✅ Berhasil mengunduh dan menggunakan Ollama dengan model `openbmb/MiniCPM5-2B:latest`.
* ✅ Berhasil memanggil LLM dari Ollama menggunakan script Python murni (via `requests`).
* ✅ Membuat Dev Log mingguan ini sebagai dokumentasi progres belajar.
* ✅ **Milestone:** Menyelesaikan Fase 0 dalam waktu 6-7 hari.

---

## 📝 Catatan & Next Steps

* Terus perdalam OOP Python melalui RealPython.
* Eksplorasi lebih lanjut terkait Docker/Kubernetes sebagai lanjutan dari konsep venv.
* Mulai masuk ke Fase 1 (sesuai roadmap).
* Pahami beberapa kekeliruan pada git command