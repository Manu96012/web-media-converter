import subprocess, uuid, os
from flask import send_file

def convert_video_to_video(request, base):
    f = request.files["file"]
    fmt = request.form["format"]

    uid = str(uuid.uuid4())
    in_f = f"{base}/{uid}_{f.filename}"
    out_f = in_f.rsplit(".", 1)[0] + "." + fmt

    f.save(in_f)

    subprocess.run([
        "ffmpeg",
        "-i", in_f,
        "-map_metadata", "0",
        out_f
    ], check=True)

    return send_file(out_f, as_attachment=True)


def convert_video_to_audio(request, base):
    f = request.files["file"]
    fmt = request.form["format"]

    uid = str(uuid.uuid4())
    in_f = f"{base}/{uid}_{f.filename}"
    out_f = in_f.rsplit(".", 1)[0] + "." + fmt

    f.save(in_f)

    subprocess.run([
        "ffmpeg",
        "-i", in_f,
        "-vn",
        out_f
    ], check=True)

    return send_file(out_f, as_attachment=True)
