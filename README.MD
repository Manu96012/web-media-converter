# Web Media Converter

Web Media Converter è un’applicazione web per **convertire file multimediali** (immagini, video e PDF) direttamente dal browser, tramite una semplice interfaccia web basata su Python e Flask.

Il progetto nasce con l’obiettivo di offrire uno strumento leggero, auto‑hostabile e facile da estendere.

---

## 🚀 Funzionalità

- 🖼️ Conversione di immagini tra formati comuni
- 🎥 Conversione video
- 📄 Conversione PDF
- Interfaccia web semplice e intuitiva
- Backend Python / Flask
- Utilizzabile interamente in locale

---

## 📦 Installazione

### Requisiti
- Python 3.9+
- pip
- ImageMagick
- ffmpeg
- Poppler

### Clonare il repository
```bash
git clone https://github.com/Manu96012/web-media-converter.git
cd web-media-converter
```

### Creare un virtual environment
```bash
python3 -m venv .venv
sudo chmod u+x .venv/bin/activate && source .venv/bin/activate   # Aggiunta dei permessi di esecuzione + activate del venv su Linux / macOS
.venv\Scripts\activate    # Windows
```

### Installare le dipendenze
```bash
pip install -r requirements.txt
```

---

## ▶️ Avvio dell’applicazione

```bash
python app.py
```

Apri il browser su:
```
http://localhost:9899
```
L'applicazione è raggiungibile anche in LAN:
```
http://0.0.0.0:9899
```

---

## 🧠 Struttura del progetto

```
web-media-converter/
├── app.py              # Entry point Flask
├── converters/         # Logica di conversione
├── static/             # File statici (CSS, JS)
├── templates/          # Template HTML
├── requirements.txt    # Dipendenze Python
└── README.md
```

---

## 🛠️ Utilizzo

1. Apri l’interfaccia web
2. Carica il file da convertire
3. Seleziona il formato di output
4. Avvia la conversione
5. Scarica il file convertito

---

## 🤝 Contribuire

Contributi, suggerimenti e pull request sono benvenuti.

1. Fai un fork del progetto
2. Crea un branch per la tua feature
3. Commit con messaggi chiari
4. Apri una Pull Request

---

## 📜 Licenza

Questo progetto è distribuito sotto licenza **MIT**.

---

## ✉️ Autore

Creato da **Manu96012**  
GitHub: https://github.com/Manu96012
