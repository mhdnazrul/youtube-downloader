from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form['url']
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        output_path = stream.download()
        return send_file(output_path, as_attachment=True, download_name=f"{yt.title}.mp4")
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
