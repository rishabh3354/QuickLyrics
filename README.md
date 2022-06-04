<h6 align="center">  
  <img src="https://img.icons8.com/ios-glyphs/344/audio-skimming.png" alt="LyricsPy" height="250px">  
  <h5 align="center">Powerful Library To Search Music Lyrics</h5>  
</h6>  
  
## Installation  
  
QuickLyrics can be installed using pip from PyPI or from GitHub  
  
#### via PyPI using pip  
  
```bash  
pip install -U quicklyrics  
```  
  
#### via GitHub using pip+git  
  
```bash  
pip install -U git+https://github.com/rishabh3354/QuickLyrics  
```  
  
## Usage  
  
To use QuickLyrics is easy, but let's see some examples:  

### Example #1
  
```python  
  
from quicklyrics.lyrics import SearchBySong  
  
res = SearchBySong("faded").results()  
  
```

> The above command will return the following:

```json
[
  {
    "song": "faded",
    "artist": "alanwalker",
    "web_url": "https://www.azlyrics.com/lyrics/alanwalker/faded.html"
  },
  {
    "song": "fadedonme",
    "artist": "alexanderludwig",
    "web_url": "https://www.azlyrics.com/lyrics/alexanderludwig/fadedonme.html"
  },
  {
    "song": "fadedinmylastsong",
    "artist": "nct",
    "web_url": "https://www.azlyrics.com/lyrics/nct/fadedinmylastsong.html"
  },
  {
    "song": "fadedou",
    "artist": "askingalexandria",
    "web_url": "https://www.azlyrics.com/lyrics/askingalexandria/fadedout.html"
  },
  {
    "song": "faded",
    "artist": "bushidozho",
    "web_url": "https://www.azlyrics.com/lyrics/bushidozho/faded.html"
  }
]
```

### Example #2
  
```python  
  
from quicklyrics.lyrics import SearchArtists  
  
res = SearchBySong().results_by_url("https://www.azlyrics.com/lyrics/alanwalker/faded.html") 

# Note: You can get lyrics web url from example #4
```

> The above command will return the following:

```json
{
  "status": true,
  "lyrics": "\n\r\nYou were the shadow to my light\nDid you feel us?\nAnother star\nYou fade away\nAfraid our aim is out of sight\nWanna see us\nAlight\n\nWhere are you now?\nWhere are you now?\nWhere are you now?\nWas it all in my fantasy?\nWhere are you now?\nWere you only imaginary?\n\nWhere are you now?\nAtlantis\nUnder the sea\nUnder the sea\nWhere are you now?\nAnother dream\nThe monster's running wild inside of me\nI'm faded\nI'm faded\nSo lost, I'm faded\nI'm faded\nSo lost, I'm faded\n\nThese shallow waters never met what I needed\nI'm letting go a deeper dive\nEternal silence of the sea, I'm breathing\nAlive\n\nWhere are you now?\nWhere are you now?\nUnder the bright but faded lights\nYou've set my heart on fire\nWhere are you now?\nWhere are you now?\n\nWhere are you now?\nAtlantis\nUnder the sea\nUnder the sea\nWhere are you now?\nAnother dream\nThe monster's running wild inside of me\nI'm faded\nI'm faded\nSo lost, I'm faded\nI'm faded\nSo lost, I'm faded\n"
}
```

### Example #3
  
```python  
  
from quicklyrics.lyrics import SearchArtists  
  
res = SearchArtists("o").results()  
  
```

> The above command will return the following:

```json
[
  "Oakenfold, Paul",
  "Oakes, Ryan",
  "Oak Ridge Boys, The",
  "Oak, Winona",
  "O.A.R. (Of A Revolution)",
  "Oasis",
  "Obel, Agnes",
  "Oberst, Conor",
  "Obey The Brave",
  "Obie Trice",
  "Obituary",
  "OBLADAET",
  "OBN Jay",
  "OB O'Brien",
  "OBOY",
  "Obscura",
  "O.C. Dawgs",
  "Oceana",
  "Ocean Alley",
  "Ocean, Billy"
]
```

### Example #4
  
```python  
  
from quicklyrics.lyrics import SearchByArtists  
  
res = SearchByArtists("Oasis").results()  

```

> The above command will return the following:

```json
{
  "artist": "oasis",
  "albums": [
    {
      "album_name": "album: \"Definitely Maybe\" (1994)",
      "songs": [
        "Rock 'n' Roll Star",
        "Shakermaker",
        "Live Forever",
        "Up In The Sky",
        "Columbia",
        "Supersonic",
        "Bring It On Down",
        "Cigarettes & Alcohol",
        "Digsy's Dinner",
        "Slide Away",
        "Married With Children",
        "Sad Song"
      ]
    },
    {
      "album_name": "album: \"(What's The Story) Morning Glory\" (1995)",
      "songs": [
        "Hello",
        "Roll With It",
        "Wonderwall",
        "Don't Look Back In Anger",
        "Hey Now",
        "Some Might Say",
        "Cast No Shadow",
        "She's Electric",
        "Morning Glory",
        "Champagne Supernova",
        "Bonehead's Bank Holiday"
      ]
    },
  ]
}
```

### Example #5
  
```python  
  
from quicklyrics.lyrics import SearchByArtistAndSong  
  
res = SearchByArtistAndSong("Oasis", "Magic Pie").results()  
  
```

> The above command will return the following:

```json
{
  "artist": "oasis",
  "song": "magicpie",
  "lyrics": [
    "\n\r\nAn extraordinary guy\nCan never have an ordinary day\nHe might live a long goodbye\nBut that is not for me to say\nI dig his friends, I dig his shoes\nHe is just a child with nothing to lose\nBut his mind, his mind\n\nThey are sleeping while they dream\nBut then they want to be adored\nThey who don't say what they mean\nWill live and die by their own sword\nI dig their friends, I dig their shoes\nThey are like a child with nothing to lose\nIn their minds, yeah their minds\n\nBut I'll have my way\nIn my own time\nI'll have my say\nMy star will shine\n\n'Cause you see me I've got my magic pie\nThink of me, yeah that was me I was that passer by\nI've been and now I've gone\n\nThere are but a thousand days preparing for a thousand years\nMany minds to educate the people who have disappeared\nD'you dig my friends? D'you dig my shoes?\nI am like a child with nothing to lose in my mind\nYeah my mind\n\nWe'll have our way\nIn our own time\nWe'll have our say\nBecause my star's going to shine\n\n'Cause you see me I've got my magic pie\nThink of me, yeah that was me I was that passer by\nI've been and now I've gone\nYou see me I've got my magic pie\nThink of me, yeah that was me I was that passer by, passer by\nThink of me I've got my magic pie\nThink of me, yeah that was me I was that passer by\nI've been and now I've gone\nYeah\nYeah\nYeah\nShut up!\n",
    ""
  ]
}
```





