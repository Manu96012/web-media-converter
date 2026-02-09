🇬🇧 English | 🇮🇹 [Italiano](README-IT.md)

# Web Media Converter

Web Media Converter is a web application designed to **convert media files** (images, videos, and PDFs) directly from the browser, through a simple web interface built with Python and Flask.

The project aims to provide a lightweight, self-hostable, and easily extensible tool.

---

## 🚀 Features

- 🖼️ Image conversion between common formats  
- 🎥 Video conversion  
- 📄 PDF conversion  
- Simple and intuitive web interface  
- Python / Flask backend  
- Fully usable locally  

---

## 📦 Installation

### Requirements
- Python 3.9+
- pip
- ImageMagick
- ffmpeg
- Poppler

### Clone the repository
```bash
git clone https://github.com/Manu96012/web-media-converter.git
cd web-media-converter
```

### Create a virtual environment
```bash
python3 -m venv .venv
sudo chmod u+x .venv/bin/activate && source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate    # Windows
```

### Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Run the application

```bash
python app.py
```

Open your browser at:
```
http://localhost:9899
```
The application is also accessible over the local network (LAN):
```
http://0.0.0.0:9899
```

---

## 🧠 Project structure

```
web-media-converter/
├── app.py              # Flask entry point
├── converters/         # Conversion logic
├── static/             # Static files (CSS, JS)
├── templates/          # HTML templates
├── requirements.txt    # Python dependencies
├── README.md
└── README-IT.md
```

---

## 🛠️ Usage

1. Open the web interface
2. Upload the file to convert
3. Select the desired output format
4. Start the conversion
5. Download the converted file

---

## 🤝 Contributing

Contributions, suggestions, and pull requests are welcome.

1. Fork the project
2. Create a branch for your feature
3. Commit with clear messages
4. Open a Pull Request

---

## 📜 License

This project is distributed under the **MIT** license.

---

## ✉️ Author

Created by **Manu96012**  
GitHub: https://github.com/Manu96012
