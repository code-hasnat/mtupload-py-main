# 📟 Document Upload & Download Server

A high-performance, multithreaded document upload and download server built using Python's standard libraries. This server supports secure, UUID-based file access, concurrent uploads, and metadata tracking using a JSON-based store.

Designed for lightweight deployments, internal tools, or as a base for more complex file-handling systems with authentication, encryption, or cloud storage integrations.

---

## 🚀 Key Features

- ✅ **Multithreaded HTTP Server** for handling concurrent requests
- 📅 **Upload Files** via `POST /`
- 📄 **Download Files** via `GET /?docid=<uuid>`
- 🔐 **Secure Access** with UUID-based file identification
- 🧠 **Metadata Tracking** (filename, size, content-type, MD5 hash)
- ⚙️ **Zero Dependencies** — built entirely with Python standard library
- 📆 **Modular Codebase** with clear separation of concerns

---

## 💂 Project Structure

```
doc_server/
├── server.py             # Main HTTP server setup
├── upload_handler.py     # Logic for handling file uploads
├── download_handler.py   # Logic for serving file downloads
├── metadata_store.py     # JSON metadata save/load helpers
├── util.py               # Utility functions (hashing, file I/O, directories)
├── uploads/              # Folder where files & metadata are stored
└── README.md             # Project documentation
```

---

## 🔧 Setup

### 1. Prerequisites

- Python **3.6+**
- No external libraries required

### 2. Run the server

```bash
python server.py
```

Server will start on `http://localhost:8000` (or `0.0.0.0` for external access).

---

## 📄 Upload a File

Use `curl` or any HTTP client to upload a file:

```bash
curl -X POST --data-binary @yourfile.pdf http://localhost:8000
```

**Response**: UUID of the uploaded file.

Example:

```
f1c97b99-4b7f-465c-a734-abcdeff12345
```

---

## 📅 Download a File

To download a previously uploaded file, use the UUID returned at upload time:

```bash
curl -X GET "http://localhost:8000/?docid=f1c97b99-4b7f-465c-a734-abcdeff12345" -o downloaded.pdf
```

---

## 📊 Metadata Format

Every uploaded file is tracked in a JSON file located at:

```
uploads/metadata.json
```

Example metadata entry:

```json
{
  "f1c97b99-4b7f-465c-a734-abcdeff12345": {
    "filename": "f1c97b99-4b7f-465c-a734-abcdeff12345.bin",
    "content_type": "application/pdf",
    "size": 152038,
    "md5": "c53a5eb1e4efb129e3e2abce9cbb1095"
  }
}
```

---

## 🛡 Security Notes

- This is a basic demo. In production, consider:
  - Adding **authentication (JWT, API keys, etc.)**
  - Using **HTTPS** for secure transmission
  - Enforcing file **size/type limits** to prevent abuse.