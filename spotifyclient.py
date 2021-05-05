import json
import requests

from track import Track
from tempo import Tempo
from playlist import Playlist


class SpotifyClient:

    def __init__(self, authorization_token, user_id):
        self.authorization_token = authorization_token
        self.user_id = user_id

    def get_last_played_tracks(self, limit=10):
        url = f"https://api.spotify.com/v1/me/player/recently-played?limit={limit}"
        response = self._place_get_api_request(url)
        response_json = response.json()
        tracks = [Track(track["track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"]) for
                  track in response_json["items"]]
        return tracks

    def get_playlist(self):
        url = f"https://api.spotify.com/v1/me/playlists"
        response = self._place_get_api_request(url)
        response_json = response.json()
        playlist_list = [Playlist(playlist["name"], playlist["id"]) for
                         playlist in response_json["items"]]

        return playlist_list

    def get_playlist_songs(self, playlist_id):
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
        response = self._place_get_api_request(url)
        response_json = response.json()
        # print("JSON: ", response_json)
        playlist_musics = [Track(track["track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"]) for
                           track in response_json["items"]]
        return playlist_musics

    def get_track_recommendations(self, seed_tracks, limit=50):
        seed_tracks_url = ""
        for seed_track in seed_tracks:
            seed_tracks_url += seed_track.id + ","
        seed_tracks_url = seed_tracks_url[:-1]
        url = f"https://api.spotify.com/v1/recommendations?seed_tracks={seed_tracks_url}&limit={limit}"
        response = self._place_get_api_request(url)
        response_json = response.json()
        tracks = [Track(track["name"], track["id"], track["artists"][0]["name"]) for
                  track in response_json["tracks"]]
        return tracks

    def get_tempo_recommendations(self, seed_tracks):
        seed_tracks_id = ""
        for seed_track in seed_tracks:
            seed_tracks_id += seed_track.id + ","
        seed_tracks_id = seed_tracks_id[:-1]

        url = f"https://api.spotify.com/v1/audio-features?ids={seed_tracks_id}"
        response = self._place_get_api_request(url)
        response_json = response.json()

        tempo_audio = [Tempo(tempo["tempo"]) for tempo in response_json["audio_features"]]

        return tempo_audio

    def create_playlist(self, name):
        data = json.dumps({
            "name": name,
            "description": "Recommended tracks",
            "public": True
        }
        )

        url = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        response = self._place_post_api_request(url, data)
        response_json = response.json()

        playlist_id = response_json["id"]
        playlist = Playlist(name, playlist_id)
        return playlist

    def populate_playlist(self, playlist, tracks):
        tracks_uris = [track.create_spotify_uri() for track in tracks]
        data = json.dumps(tracks_uris)
        url = f"https://api.spotify.com/v1/playlists/{playlist.id}/tracks"
        response = self._place_post_api_request(url, data)
        response_json = response.json()

        return response_json

    def _place_post_api_request(self, url, data):
        response = requests.post(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.authorization_token}"
            },
            data=data
        )

        return response

    def _place_get_api_request(self, url):
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.authorization_token}"
            }
        )
        # print("RESPONSE GET: ", response)
        return response
