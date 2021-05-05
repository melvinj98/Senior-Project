class Tempo:

    def __init__(self, tempo):
        self.tempo = tempo

    def create_spotify_uri(self):
        return f"spotify:track:{self.id}"

    def __str__(self):
        return f"{self.tempo}"
