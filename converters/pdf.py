import subprocess, os, uuid, zipfile
from flask import send_file

def convert_pdf_to_image(request, base):
    f = request.files["file"]
    fmt = request.form["format"]

    uid = str(uuid.uuid4())
    in_f = f"{base}/{uid}.pdf"
    out_dir = f"{base}/{uid}_imgs"
    os.makedirs(out_dir, exist_ok=True)

    f.save(in_f)

    subprocess.run([
        "pdftoppm",
        f"-{fmt}",
        in_f,
        f"{out_dir}/page"
    ], check=True)

    zip_path = f"{out_dir}.zip"
    with zipfile.ZipFile(zip_path, "w") as z:
        for file in sorted(os.listdir(out_dir)):
            z.write(f"{out_dir}/{file}", file)

    return send_file(zip_path, as_attachment=True)


def convert_image_to_pdf(request, base):
    f = request.files["file"]

    uid = str(uuid.uuid4())
    in_f = f"{base}/{uid}_{f.filename}"
    out_pdf = f"{base}/{uid}.pdf"

    f.save(in_f)

    subprocess.run([
        "magick",
        in_f,
        out_pdf
    ], check=True)

    return send_file(out_pdf, as_attachment=True)
