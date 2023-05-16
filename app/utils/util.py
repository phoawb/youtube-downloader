from pytube import YouTube, Stream
from time import sleep


def duration_string_formatter(seconds: int) -> str:
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    hour_str: str = ""
    minute_str: str = "00:"
    second_str: str = "00"
    if not h == 0:
        hour_str = f"{h}:"
    if not m == 0:
        minute_str = f"{m}:"
    if s > 9:
        second_str = f"{s}"
    else:
        second_str = f"0{s}"
    return hour_str + minute_str + second_str


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
