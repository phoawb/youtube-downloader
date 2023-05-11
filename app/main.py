from flask import Flask, render_template, request, redirect, url_for, send_file
from pytube import YouTube, Stream, monostate
from time import sleep
from io import BytesIO
import json

app = Flask(__name__, template_folder="html", static_url_path="/static")


def download_video(url: str) -> YouTube:
    video = YouTube(url)
    count = 0
    while True:
        try:
            # Attempt to retrieve the video streams
            video.streams
            break  # If successful, exit the loop
        except Exception as e:
            # If unsuccessful, print the error message and wait a bit before retrying
            print(f"Error: {e}", "Retrying...", count)
            count += 1
            sleep(0.5)
    return video


def to_dict(stream: Stream):
    return {"itag": stream.itag,
            "resolution": stream.resolution,
            "mimeType": stream.mime_type + "; " + "codecs=\"" + ",".join(stream.codecs) + "\"",
            "mime_type": stream.mime_type,
            "url": stream.url,
            "includes_audio_track": stream.includes_audio_track,
            "includes_video_track": stream.includes_video_track,
            "is_progressive": stream.is_progressive,
            "is_otf": stream.is_otf,
            "filesize": stream.filesize,
            "duration": stream._monostate.duration,
            "title": stream._monostate.title,
            "bitrate": stream.bitrate,
            "contentLength": stream._filesize}


@app.route('/', methods=['GET', 'POST'])
def index():
    error_msg = ""
    if request.method == 'POST':

        # Get the YouTube video URL from the form input
        video_url = request.form['video_url']

        # Extract video information using PyTube
        video = download_video(video_url)
        download_options = video.streams.filter(
            progressive=True).order_by("resolution").desc()
        stream = download_options.first()
        if not stream:
            raise Exception
        stream_json = json.dumps(to_dict(stream))
        download_options_str = [json.dumps(
            to_dict(stream)) for stream in download_options]
        file1 = open('sample.txt', 'w')
        file1.write(stream_json)
        file1.close()
        streams = [to_dict(stream) for stream in download_options]
        streams_json_object = json.dumps(streams)
        with open("sample.json", "w") as outfile:
            outfile.write(streams_json_object)

        """f = open("sample.json")
        streams = json.load(f)
        f.close()
        download_options_str = [json.dumps(stream) for stream in streams] """

        return render_template('download.html', streams=streams, download_options_str=download_options_str)

    # If no URL has been submitted yet, render the main page
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download():
    if request.method == "POST":
        buffer = BytesIO()
        stream_json = request.form["stream_json"]
        stream_dict = json.loads(stream_json)
        stream = Stream(stream_dict, monostate.Monostate(
            on_complete=None, on_progress=None, title=stream_dict["title"], duration=stream_dict["duration"]))
        stream.stream_to_buffer(buffer)
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name=(stream.title + "." + stream.mime_type.split("/")[1]), mimetype=stream.mime_type)
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
