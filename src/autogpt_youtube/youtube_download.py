import youtube_dl
from . import AutoGPTYouTube

plugin = AutoGPTYouTube()

def download_youtube_video(url: str, output: str) -> str:
    """Download a youtube video to mp4 format.

    Args:
        url (str): The url of the video to download.
        output (str): The output path.

    Returns:
        str: status message
    """

    # download the video
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": output,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return f"Downloaded the video from {url} to {output}"


def download_youtube_audio(url: str, output: str) -> str:
    """Download a youtube video to mp3 format.

    Args:
        url (str): The url of the video to download.
        output (str): The output path.

    Returns:
        str: status message
    """

    # download the video
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return f"Downloaded the audio from {url} to {output}"