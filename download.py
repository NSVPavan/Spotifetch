import yt_dlp
import os

# Create downloads directory if it doesn't exist
os.makedirs("downloads", exist_ok=True)

def download_song(song_name):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f"downloads/{song_name}.mp3",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch:{song_name} audio"])

# Example usage
# if __name__ == "__main__":
#     download_song("Shape of You Ed Sheeran")
