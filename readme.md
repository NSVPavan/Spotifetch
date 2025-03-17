
# Spotify Playlist Downloader

A simple tool that downloads songs from your Spotify playlists by searching for the tracks on YouTube and converting them to high-quality MP3 files using yt-dlp and ffmpeg.

## Features

- **Spotify Authentication:** Uses Spotify's API to fetch your playlists.
- **Interactive Selection:** Enter a playlist name or choose from a list if not found.
- **Organized Downloads:** Creates a dedicated folder (named after the playlist) inside the `downloads` directory.
- **Audio Conversion:** Downloads and converts audio to MP3 using ffmpeg.

## Prerequisites

- **Python 3.11+**
- A [Spotify Developer Account](https://developer.spotify.com/dashboard/)  
  - Create an app and obtain your `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, and set the redirect URI (e.g., `http://localhost:8888/callback`).
- [ffmpeg](https://ffmpeg.org/download.html) installed and either added to your system PATH or provided using the `--ffmpeg-location` argument.
- (Optional) [Chocolatey](https://chocolatey.org/) on Windows to easily install ffmpeg.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/spotify-playlist-downloader.git
   cd spotify-playlist-downloader
   ```

2. **(Optional) Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   # Activate the virtual environment:
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**

   Create a `.env` file in the root directory and add your Spotify API credentials:

   ```env
   SPOTIPY_CLIENT_ID=your_client_id
   SPOTIPY_CLIENT_SECRET=your_client_secret
   SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
   ```

## Usage

Run the main script:

```bash
python main.py
```

### How It Works

1. **Playlist Selection:**
   - The script will prompt you to enter a playlist name.
   - If an exact match isn’t found, it displays a list of all your playlists. Choose one by entering the corresponding number.

2. **Downloading:**
   - The script fetches all songs from the selected playlist.
   - It creates a dedicated folder under the `downloads` directory (named after the playlist) and downloads each track there.

3. **ffmpeg Location:**
   - If ffmpeg is not in your system PATH, you can provide its location when running the script:
     
     ```bash
     python main.py --ffmpeg-location "C:\path\to\ffmpeg\bin"
     ```

## Troubleshooting

### ffmpeg Not Found in VS Code Terminal

- **Environment Variable Issue:**  
  VS Code may not immediately pick up changes to system environment variables.  
  **Solution:**  
  - Restart VS Code.
  - Verify the PATH in the VS Code terminal:
    ```bash
    echo $env:Path  # For PowerShell
    echo %PATH%     # For CMD
    ```
  - If the ffmpeg path is missing, add it manually or use the `--ffmpeg-location` argument.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/spotify-playlist-downloader/issues).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy downloading and enjoy your music!
