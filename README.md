# Python Translate Flask App

Proyek ini adalah aplikasi penerjemahan teks menggunakan Flask, Celery, dan RabbitMQ. Pengguna dapat mengirimkan teks untuk diterjemahkan secara asinkron, serta memeriksa status dari tugas penerjemahan yang sedang berlangsung.

---

## Prasyarat

Sebelum memulai, pastikan Anda memiliki:
- **Docker** dan **Docker Compose** terinstal di mesin Anda.
  - [Panduan instalasi Docker](https://docs.docker.com/get-docker/)

---

## Instalasi

1. **Clone repository ini**:
   ```bash
   git clone https://github.com/koji-xenpai/python-translate-flask-app.git
   cd python-translate-flask-app

2. **Runing App**
    ```bash
    docker compose build && docker compose up -d

## Endpoint

### 1. Penerjemahan Teks
* **Endpoint:** `/translate`
* **Metode:** POST
* **Deskripsi:** Menerima permintaan untuk menerjemahkan teks.
* **Permintaan:**
  * **Header:** `Content-Type: application/json`
  * **Body (JSON):**
    ```json
    {
      "text": "Teks yang akan diterjemahkan",
      "src_lang": "Kode bahasa sumber (misal: en)",
      "dest_lang": "Kode bahasa tujuan (misal: id)"
    }
    ```
* **Respons:**
  ```json
  {
    "task_id": "ID tugas",
    "status": "Status tugas (Processing)"
  }

## 2. Cek Status Tugas
* **Endpoint:** `/status/<task_id>`
* **Metode:** GET
* **Deskripsi:** API ini digunakan untuk memeriksa status tugas penerjemahan yang telah dikirim sebelumnya.
* **Parameter URL:**
  | Parameter | Tipe   | Deskripsi                                    |
  |-----------|--------|----------------------------------------------|
  | task_id   | string | ID tugas yang diterima dari endpoint `/translate`. |
* **Contoh Permintaan:**
  ```bash
  curl -X GET http://localhost:5000/status/abc123

* **Respons: PENDING**
  ```json
  {
  "state": "PENDING",
  "status": "Task is still in the queue"
  }

* **Respons:SUCCESS**
  ```json
  {
  "state": "SUCCESS",
  "result": "Saya sedang belajar Python dan menggunakan Celery untuk penerjemahan teks."
  }
