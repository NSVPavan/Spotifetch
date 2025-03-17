from auth import authenticate_spotify

def get_playlist_tracks(playlist_id):
    sp = authenticate_spotify()
    results = sp.playlist_tracks(playlist_id)
    tracks = []

    for item in results['items']:
        track = item['track']
        song_name = f"{track['name']} {track['artists'][0]['name']}"
        tracks.append(song_name)

    return tracks

# Example usage
if __name__ == "__main__":
    playlist_id = "YOUR_PLAYLIST_ID"
    songs = get_playlist_tracks(playlist_id)
    print("Songs found:", songs)
