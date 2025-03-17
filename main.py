from fetch import get_playlist_tracks, get_user_playlists
from download import download_song

def select_playlist():
    # Get all playlists from the user's library
    playlists = get_user_playlists()

    if not playlists:
        print("No playlists found in your Spotify library.")
        return None

    # Ask the user for a playlist name
    playlist_name = input("Enter the playlist name: ").strip()

    # Try to find the exact match
    for pid, name in playlists.items():
        if name.lower() == playlist_name.lower():
            print(f"Playlist '{name}' found!")
            return pid

    # If no match, show available playlists
    print("\nPlaylist not found! Choose from the available playlists:\n")
    for i, (pid, name) in enumerate(playlists.items(), 1):
        print(f"{i}. {name}")

    # Ask the user to select from the displayed list
    while True:
        try:
            choice = int(input("\nEnter the number of the playlist you want to download: "))
            if 1 <= choice <= len(playlists):
                selected_pid = list(playlists.keys())[choice - 1]
                print(f"Selected Playlist: {playlists[selected_pid]}")
                return selected_pid
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Please enter a number.")

def main():
    print("🎵 Spotify Playlist Downloader 🎵\n")
    
    playlist_id = select_playlist()
    if not playlist_id:
        print("No playlist selected. Exiting.")
        return

    songs = get_playlist_tracks(playlist_id)

    if not songs:
        print("No songs found in this playlist. Exiting.")
        return

    print(f"Found {len(songs)} songs. Starting download...\n")

    for song in songs:
        print(f"Downloading: {song}...")
        download_song(song)

    print("\n✅ All downloads completed!")

if __name__ == "__main__":
    main()