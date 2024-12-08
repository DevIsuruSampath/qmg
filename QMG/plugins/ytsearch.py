from yt_dlp import YoutubeDL
from QMG.config import DOWNLOAD_PATH

async def search_and_download(query):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{DOWNLOAD_PATH}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
        'noplaylist': True
    }

    with YoutubeDL(ydl_opts) as ydl:
        # Perform YouTube search and download
        info = ydl.extract_info(f"ytsearch:{query}", download=True)
        return ydl.prepare_filename(info['entries'][0])
