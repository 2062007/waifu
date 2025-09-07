# server.py
import requests
from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/download")
def download():
    url = request.args.get("url")
    if not url:
        return "No URL", 400

    r = requests.get(url, stream=True)
    if r.status_code != 200:
        return "Failed to fetch image", 500

    # đoán đuôi file
    content_type = r.headers.get("Content-Type", "image/png")
    ext = content_type.split("/")[-1]
    filename = "waifu." + ext

    return Response(
        r.content,
        headers={
            "Content-Type": content_type,
            "Content-Disposition": f"attachment; filename={filename}"
        }
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
