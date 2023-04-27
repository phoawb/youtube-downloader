from nicegui import ui
from pytube import YouTube
from utils.util import duration_string_formatter
from time import sleep


class Youtube_d:
    def __init__(self) -> None:
        self.thumbnail_url = "https://i.ytimg.com/vi/VbOeopWF6Fc/sddefault.jpg"
        self.title = "Original / Оригинал - Сен Қайдан Биласан (disco, Uzbekistan USSR, 1981)"
        self.length = 289


@ui.page('/')
def home() -> None:

    def table_download(stream):
        print(stream)
        stream.download()

    def generate_download_table(yt: YouTube) -> None:
        youtube_video_streams = yt.streams.filter(
            progressive=True, file_extension="mp4").order_by("resolution").desc()
        youtube_table_rows = []
        for stream in youtube_video_streams:
            row = {"Quality": stream.resolution,
                   "Status": ui.link("download", stream.url)}
            # youtube_table.add_rows(row)

# row = {"Quality": stream.}
# print(yt.streams.filter(progressive=True))
# for row in youtube_table_rows:
#   youtube_table.add_rows(row)
# print(yt.streams.filter(only_audio=True))

    def fetch_video() -> None:
        yt = Youtube_d()
        """yt = YouTube(youtube_link.value)
        debug_cnt = 0
        while True:
            try:
                title = yt.title
                break
            except:
                debug_cnt += 1
                print("failed to get video, reloading...", debug_cnt)
                yt = YouTube(youtube_link.value)
                sleep(0.5)
                continue """
        youtube_thumbnail.set_source(yt.thumbnail_url)
        youtube_title.set_text(yt.title)
        youtube_duration.set_text(
            "Duration: " + duration_string_formatter(yt.length))
        # generate_download_table(yt)
        card.set_visibility("visible")

    with ui.column().classes(":param add: absolute-center") as main_column:
        with ui.row() as row:
            youtube_link = ui.input('Paste Youtube Link', validation={
                                    "Enter a valid YouTube link!": lambda value: value.startswith("https://www.youtube.com/watch")})
            button = ui.button('Start')
        with ui.card() as card:
            with ui.splitter() as splitter:
                with splitter.before:
                    youtube_thumbnail = ui.image()
                    youtube_title = ui.label()
                    youtube_duration = ui.label()
                with splitter.after:
                    """ youtube_table = ui.table(columns=[
                        {"name": "Quality", "label": "Quality",
                         "field": "Quality", "required": True},
                        {"name": "Status", "label": "Status", "field": "Status"}
                    ], rows=[]) """
                    with ui.row().classes(add="space-x-4") as table_row:
                        with ui.column() as column1:
                            ui.label("Quality")
                        with ui.column() as column2:
                            ui.label("Status")
        card.visible = False
        youtube_link.on(
            'keydown.enter', fetch_video)
        button.on("click", fetch_video)


ui.run(port=8000)
