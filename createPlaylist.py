from spotifyclient import SpotifyClient
import settings
import random


def main(emotion):
    SPOTIFY_AUTHORIZATION_TOKEN = settings.getAuthKey()
    SPOTIFY_USER_ID = settings.getUserID()
    happy_playlist_id = "1h90L3LP8kAJ7KGjCV2Xfd"
    sad_playlist_id = "37i9dQZF1DX7qK8ma5wgG1"
    neutral_playlist_id = "4PFwZ4h1LMAOwdwXqvSYHd"
    angry_playlist_id = "3uaOn723EyF8eF7GhtJkyD"
    x = 0


    #spotify_client = SpotifyClient(os.getenv("SPOTIFY_AUTHORIZATION_TOKEN"),
    #                               os.getenv("SPOTIFY_USER_ID"))

    spotify_client = SpotifyClient(SPOTIFY_AUTHORIZATION_TOKEN,
                                   SPOTIFY_USER_ID)

    #emotion = input("Input your current emotion(angry,sad,happy,neutral)" +
     #               " or enter 'q' to quit:").lower()

    if emotion == 'Happy':
        playlist_list = spotify_client.get_playlist()
        playlist_id = happy_playlist_id
    elif emotion == 'Sad':
        playlist_list = spotify_client.get_playlist()
        playlist_id = sad_playlist_id
    elif emotion == 'Neutral':
        playlist_list = spotify_client.get_playlist()
        playlist_id = neutral_playlist_id
    elif emotion == 'Angry':
        playlist_list = spotify_client.get_playlist()
        playlist_id = angry_playlist_id
    else:
        print("Invalid emotion entered")
        quit()

    # spotify_client = SpotifyClient(os.getenv("SPOTIFY_AUTHORIZATION_TOKEN"),
    #                                os.getenv("SPOTIFY_USER_ID"))

    playlist_musics = spotify_client.get_playlist_songs(playlist_id)
    # for index, track in enumerate(playlist_musics):
    # print(f"{index+1} - {track}")

    if emotion == 'Happy':
        indexes = []
        while x < 5:
            indexes.insert(x, random.randint(0, 100))
            x += 1
    elif emotion == 'Sad':
        indexes = []
        while x < 5:
            indexes.insert(x, random.randint(0, 60))
            x += 1
    elif emotion == 'Neutral':
        indexes = []
        while x < 5:
            indexes.insert(x, random.randint(0, 85))
            x += 1
    elif emotion == 'Angry':
        indexes = []
        while x < 5:
            indexes.insert(x, random.randint(0, 180))
            x += 1

    seed_tracks = [playlist_musics[int(index) - 1] for index in indexes]

    recommended_tracks = spotify_client.get_track_recommendations(seed_tracks)

    if emotion == 'Happy':
        playlist_name = "Happy Playlist"
    elif emotion == 'Sad':
        playlist_name = "Sad Playlist"
    elif emotion == 'Neutral':
        playlist_name = "Neutral Playlist"
    elif emotion == 'Angry':
        playlist_name = "Angry Playlist"

    playlist = spotify_client.create_playlist(playlist_name)
    print(f"Playlist '{playlist.name}' was created successfully.")

    spotify_client.populate_playlist(playlist, recommended_tracks)
    print(f"Recommended tracks successfully uploaded to playlist '{playlist.name}'")


if __name__ == "__main__":
    main()
