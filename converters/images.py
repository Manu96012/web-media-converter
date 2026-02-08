import os, subprocess, uuid
from flask import Flask, render_template, request, send_file, jsonify, url_for
from rembg import remove
from PIL import Image, ImageDraw
from io import BytesIO

def convert_image(request, base):
    f = request.files["file"]
    fmt = request.form["format"]

    uid = str(uuid.uuid4())
    in_f = f"{base}/{uid}_{f.filename}"
    out_f = in_f.rsplit(".",1)[0] + "." + fmt

    f.save(in_f)

    # Se il formato di output è .ico, ridimensioniamo per sicurezza
    if fmt == "ico":
        with Image.open(in_f) as img:
            img.thumbnail((64, 64))  # mantiene proporzioni
            temp_path = in_f.rsplit(".",1)[0] + "_resized.png"
            img.save(temp_path)
            in_f_for_magick = temp_path
    else:
        in_f_for_magick = in_f

    subprocess.run(["magick", in_f_for_magick, out_f], check=True)

    if fmt == "ico" and os.path.exists(temp_path):
        os.remove(temp_path)

    return send_file(out_f, as_attachment=True)

def remove_image_background(request, base_dir):
    f = request.files['file']
    filename = f.filename
    input_path = os.path.join(base_dir, f"{uuid.uuid4()}_{filename}")
    temp_png_path = os.path.join(base_dir, f"{uuid.uuid4()}_temp.png")

    f.save(input_path)

    with open(input_path, "rb") as i:
        input_bytes = i.read()
        output_bytes = remove(input_bytes)
    with open(temp_png_path, "wb") as o:
        o.write(output_bytes)

    output_format = request.form.get("format", "png").lower()
    if output_format not in ["png", "webp", "gif", "ico"]:
        output_format = "png"

    if output_format != "png":
        output_path = os.path.join(base_dir, f"{uuid.uuid4()}.{output_format}")

        if output_format == "ico":
            with Image.open(temp_png_path) as img:
                img.thumbnail((64,64))
                temp_resized_path = temp_png_path.rsplit(".",1)[0] + "_resized.png"
                img.save(temp_resized_path)
                in_f_for_magick = temp_resized_path
        else:
            in_f_for_magick = temp_png_path

        subprocess.run([
            "magick", in_f_for_magick,
            "-background", "none",
            output_path
        ], check=True)

        if output_format == "ico" and os.path.exists(temp_resized_path):
            os.remove(temp_resized_path)

        os.remove(temp_png_path)
    else:
        output_path = temp_png_path

    return send_file(output_path, as_attachment=True)


def round_image_corners(request, base_dir):
    """Arrotonda gli angoli di un'immagine secondo la percentuale scelta."""
    f = request.files['file']
    filename = f.filename
    input_path = os.path.join(base_dir, f"{uuid.uuid4()}_{filename}")
    f.save(input_path)

    corner_percent = int(request.form.get("corner_percent", 20))
    output_format = request.form.get("format", "png").lower()
    if output_format not in ["png", "webp", "gif", "ico"]:
        output_format = "png"

    output_path = os.path.join(base_dir, f"{uuid.uuid4()}.{output_format}")

    with Image.open(input_path).convert("RGBA") as im:
        w, h = im.size
        radius = int(min(w,h) * corner_percent / 100)

        # Maschera arrotondata
        mask = Image.new("L", im.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle([0, 0, w, h], radius=radius, fill=255)
        im.putalpha(mask)

        # Se formato .ico, ridimensiona a 64x64
        if output_format == "ico":
            im.thumbnail((64,64))

        im.save(output_path, format=output_format.upper())

    return send_file(output_path, as_attachment=True)
