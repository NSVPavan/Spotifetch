from auth import authenticate_spotify

def get_user_playlists():
    """Fetch all playlists in the user's Spotify library."""
    sp = authenticate_spotify()
    playlists = {}

    results = sp.current_user_playlists()
    for playlist in results['items']:
        playlists[playlist['id']] = playlist['name']

    return playlists

def get_playlist_tracks(playlist_id):
    """Fetch all track names from a given playlist ID."""
    sp = authenticate_spotify()
    tracks = []

    results = sp.playlist_tracks(playlist_id)
    for item in results['items']:
        track = item['track']
        if track:
            tracks.append(f"{track['name']} - {track['artists'][0]['name']}")

    return tracks
