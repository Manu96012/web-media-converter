from flask import Flask, render_template, request, send_file, request
import os, uuid
import logging

from converters.video import convert_video_to_video, convert_video_to_audio
from converters.images import convert_image, remove_image_background, round_image_corners
from converters.pdf import convert_pdf_to_image, convert_image_to_pdf

app = Flask(__name__)
BASE = "/tmp/mediaweb"
os.makedirs(BASE, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("mediaweb")

@app.before_request
def log_request():
    logger.info(
        "%s %s %s",
        request.remote_addr,
        request.method,
        request.path
    )

@app.after_request
def log_response(response):
    logger.info(
        "→ %s %s",
        response.status_code,
        request.path
    )
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/video/to-video", methods=["POST"])
def video_to_video():
    return convert_video_to_video(request, BASE)

@app.route("/video/to-audio", methods=["POST"])
def video_to_audio():
    return convert_video_to_audio(request, BASE)

@app.route("/image", methods=["POST"])
def image():
    return convert_image(request, BASE)

@app.route("/image/remove-bg", methods=["POST"])
def image_remove_bg():
    return remove_image_background(request, BASE)

@app.route("/image/round-corners", methods=["POST"])
def image_round_corners():
    return round_image_corners(request, BASE)

@app.route("/pdf/to-image", methods=["POST"])
def pdf_to_image():
    return convert_pdf_to_image(request, BASE)

@app.route("/pdf/to-pdf", methods=["POST"])
def image_to_pdf():
    return convert_image_to_pdf(request, BASE)


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=9899)

