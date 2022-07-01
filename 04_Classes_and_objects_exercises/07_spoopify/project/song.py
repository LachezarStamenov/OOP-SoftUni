# The Song class should receive a name (string), a length (float), and a single (bool) upon initialization. It has
# one method:
# -	get_info()
# o	Returns the information of the song in this format: "{song_name} - {song_length}"

class Song:

    def __init__(self, name: str, length: float, single: bool):
        self.name = name
        self.length = length
        self.single = single

    def get_info(self):
        return f"{self.name} - {self.length}"


