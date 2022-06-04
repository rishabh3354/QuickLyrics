from bs4 import BeautifulSoup
import requests
import json
from .constant import SOURCE, HEADERS, SEARCH_SOURCE


class SearchArtists:
    def __init__(self, query, count=20):
        """
        :param query: str
        :param count: int default 20, set 0 for max
        """
        self.query = query.lower()
        self.count = count

    def results(self):
        try:
            if not self.query.isalpha():
                raise Exception("Input query string can only be alphabets from A-Z")

            if len(self.query) != 1:
                raise Exception(
                    "Input query string length should not be greater than 1"
                )
            url = SOURCE + self.query + ".html"
            try:
                req = requests.get(url, headers=HEADERS)
            except requests.ConnectionError as rce:
                raise requests.ConnectionError(
                    f"Please check your internet connection: {rce}"
                )

            except requests.Timeout as rto:
                raise requests.Timeout(f"Connection timeout: {rto}")
            soup = BeautifulSoup(req.content, "html.parser")
            data = []

            for div in soup.find_all("div", {"class": "container main-page"}):
                links = div.findAll("a")[: self.count]
                for item in links:
                    data.append(item.text.strip())
            return json.dumps(data)
        except Exception as e:
            raise Exception(f"Error Occurred: {e}")


class SearchByArtists:
    def __init__(self, artist_name):
        """
        :param artist_name:
        """
        self.artist_name = artist_name.lower().replace(" ", "")

    def results(self):
        try:
            first_char = self.artist_name[0]
            url = SOURCE + first_char + "/" + self.artist_name + ".html"
            try:
                req = requests.get(url, headers=HEADERS)
            except requests.ConnectionError as rce:
                raise requests.ConnectionError(
                    f"Please check your internet connection: {rce}"
                )

            except requests.Timeout as rto:
                raise requests.Timeout(f"Connection timeout: {rto}")
            soup = BeautifulSoup(req.content, "html.parser")
            all_albums = soup.find("div", id="listAlbum")
            first_album = all_albums.find("div", class_="album")
            artist = {"artist": self.artist_name, "albums": []}
            all_items = str(
                first_album.find_next_siblings(["a", "div"])[0].parent.text
            ).split("\n")
            album_data = {"album_name": "", "songs": []}

            for item in all_items:
                if item != "":
                    if item.startswith("album:"):
                        artist["albums"].append(album_data)
                        album_data = {"album_name": item, "songs": []}
                    else:
                        album_data["songs"].append(item)

            del artist["albums"][0]
            return json.dumps(artist)

        except Exception as e:
            raise Exception(f"Error Occurred: {e}")


class SearchByArtistAndSong:
    def __init__(self, artist, song):
        """
        :param artist: str
        :param song: str
        """
        self.artist = artist.lower().replace(" ", "")
        self.song = song.lower().replace(" ", "")

    def results(self):
        try:
            response = {"artist": self.artist, "song": self.song, "lyrics": ""}
            url = SOURCE + "lyrics/" + self.artist + "/" + self.song + ".html"
            try:
                req = requests.get(url, headers=HEADERS)
            except requests.ConnectionError as rce:
                raise requests.ConnectionError(
                    f"Please check your internet connection: {rce}"
                )

            except requests.Timeout as rto:
                raise requests.Timeout(f"Connection timeout: {rto}")
            soup = BeautifulSoup(req.content, "html.parser")
            lyrics = soup.find_all("div", attrs={"class": None, "id": None})
            if not lyrics:
                return json.dumps(
                    {"Error": "Unable to find " + self.song + " by " + self.artist}
                )
            elif lyrics:
                lyrics = [x.getText() for x in lyrics]
                response["lyrics"] = lyrics
            return json.dumps(response)

        except Exception as e:
            raise Exception(f"Error Occurred: {e}")


class SearchBySong:
    def __init__(self, song="", count=5):
        """
        :param song: str
        :param count: int
        """
        self.song = song.lower().replace(" ", "")
        self.count = count

    def results(self):
        try:
            if self.count <= 0:
                raise Exception(
                    "Result count should be greater than 0 and of Integer type."
                )
            try:
                url = SEARCH_SOURCE + "search.php?q=" + self.song
                req = requests.get(url, headers=HEADERS)
            except requests.ConnectionError as rce:
                raise requests.ConnectionError(
                    f"Please check your internet connection: {rce}"
                )
            except requests.Timeout as rto:
                raise requests.Timeout(f"Connection timeout: {rto}")
            else:
                data = req.text
                soup = BeautifulSoup(data, "lxml")
                tags = soup.find_all("a")
                l2 = []
                for x in tags:
                    l2.append(x.get("href"))
                song_url = []
                for y in l2:
                    if "www.azlyrics.com/lyrics/" in y:
                        song_url.append(y)
                song_title = []
                artist_name = []
                if len(song_url) != 0:
                    for i in song_url:
                        res = i.rstrip(".html")
                        res1 = res.split("/")
                        song_title.append(res1[5])
                        artist_name.append(res1[4])
                    finaldata = []
                    for counter in range(0, len(song_url))[: self.count]:
                        json_data = {
                            "song": str(song_title[counter]),
                            "artist": str(artist_name[counter]),
                            "web_url": str(song_url[counter]),
                        }
                        finaldata.append(json_data)
                    return json.dumps(finaldata)
                else:
                    raise "Lyrics not found !"

        except Exception as e:
            raise Exception(f"Error Occurred: {e}")

    @staticmethod
    def results_by_url(url):
        try:
            response = {"status": False, "lyrics": ""}
            try:
                req = requests.get(url, headers=HEADERS)
            except requests.ConnectionError as rce:
                raise requests.ConnectionError(
                    f"Please check your internet connection: {rce}"
                )
            except requests.Timeout as rto:
                raise requests.Timeout(f"Connection timeout: {rto}")
            else:
                soup = BeautifulSoup(req.content, "lxml")
                lyrics = soup.find_all("div", attrs={"class": None, "id": None})[
                    0
                ].getText()
                if lyrics:
                    response["status"] = True
                    response["lyrics"] = lyrics
                else:
                    response["lyrics"] = "Lyrics not found !"
                return json.dumps(response)

        except Exception as e:
            raise Exception(f"Error Occurred: {e}")
