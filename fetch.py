from auth import authenticate_spotify

def get_user_playlists():
    sp = authenticate_spotify()
    playlists = {}

    results = sp.current_user_playlists()
    for playlist in results['items']:
        playlists[playlist['id']] = playlist['name']

    return playlists
