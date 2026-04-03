# Challenge #4 - Create classes for Songs & Playlists
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration 

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.duration} Seconds Long)"


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)

    def __str__(self):
        output = f"{self.name} Playlist:\n"
        total_duration = 0
        for song in self.songs:
            total_duration += song.duration
            output += f"{song.__str__()}\n"
        output += "Total Duration: " + str(total_duration) + " Seconds"
        return output


def test_spotify():
    song1 = Song("Song 1", "Artist 1", 180)
    song2 = Song("Song 2", "Artist 2", 240)

    playlist1 = Playlist("My Playlist")
    playlist1.add_song(song1)
    playlist1.add_song(song2)

    print(playlist1)


test_spotify()

