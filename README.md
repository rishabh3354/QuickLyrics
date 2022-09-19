<h6 align="center">  
  <img src="https://img.icons8.com/ios-glyphs/344/audio-skimming.png" alt="LyricsPy" height="250px">  
  <h5 align="center">Powerful Library To Search Music Lyrics</h5>  
</h6>  
  
## Installation  
  
QuickLyrics can be installed using pip from PyPI or from GitHub  
Link: https://pypi.org/project/quicklyrics/
  
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
  
res = SearchArtists("R").results()  
  
```

> The above command will return the following:

```json
[
  "R3HAB",
  "R5",
  "Ra",
  "Rabbitt, Eddie",
  "RAC",
  "Racal, Maris",
  "Rachael Yamagata",
  "Rachel Chinouriri",
  "Rachel Crow",
  "Rachel Farley",
  "Rachel Grae",
  "Rachelle Ann Go",
  "Rachel Platten",
  "Rachel Stevens",
  "Rachel Taylor",
  "Rachel Wammack",
  "Raconteurs, The",
  "Racoon",
  "Radiant Children",
  "RADICAL"
]
```

### Example #4
  
```python  
  
from quicklyrics.lyrics import SearchByArtists  
  
res = SearchByArtists("Rihanna").results()  

```

> The above command will return the following:

```json
{
  "artist": "Rihanna",
  "albums": [
    {
      "album_name": "album: \"Music Of The Sun\" (2005)",
      "songs": [
        "Pon De Replay",
        "Here I Go Again",
        "If It's Lovin' That You Want",
        "You Don't Love Me (No, No, No)",
        "That La, La, La",
        "The Last Time",
        "Willing To Wait",
        "Music Of The Sun",
        "Let Me",
        "Rush",
        "There's A Thug In My Life",
        "Now I Know",
        "Pon De Replay (Remix)"
      ]
    },
    {
      "album_name": "album: \"A Girl Like Me\" (2006)",
      "songs": [
        "SOS",
        "Kisses Don't Lie",
        "Unfaithful",
        "We Ride",
        "Dem Haters",
        "Final Goodbye",
        "Break It Off",
        "Crazy Little Thing Called Love",
        "Selfish Girl",
        "P.S. (I'm Still Not Over You)",
        "A Girl Like Me",
        "A Million Miles Away",
        "If It's Lovin' That You Want Pt. 2",
        "Who Ya Gonna Run To?(Deluxe Edition Bonus Track)",
        "Coulda Been The One(Deluxe Edition Bonus Track)",
        "Should I?(Deluxe Edition Bonus Track)",
        "Hypnotized(Deluxe Edition Bonus Track)"
      ]
    },
    {
      "album_name": "album: \"Good Girl Gone Bad\" (2007)",
      "songs": [
        "Umbrella",
        "Push Up On Me",
        "Don't Stop The Music",
        "Breakin' Dishes",
        "Shut Up And Drive",
        "Hate That I Love You",
        "Say It",
        "Sell Me Candy",
        "Lemme Get That",
        "Rehab",
        "Question Existing",
        "Good Girl Gone Bad",
        "Cry(Japanese Bonus Track)",
        "Haunted(Japanese Bonus Track)",
        "Disturbia(Good Girl Gone Bad: Reloaded)",
        "Take A Bow(Good Girl Gone Bad: Reloaded)",
        "If I Never See Your Face Again(Good Girl Gone Bad: Reloaded)"
      ]
    },
    {
      "album_name": "album: \"Rated R\" (2009)",
      "songs": [
        "Mad House",
        "Wait Your Turn",
        "Hard",
        "Stupid In Love",
        "Rockstar 101",
        "Russian Roulette",
        "Fire Bomb",
        "Rude Boy",
        "Photographs",
        "G4L",
        "Te Amo",
        "Cold Case Love",
        "The Last Song",
        "Hole In My Head(Nokia Comes With Music Bonus Track)"
      ]
    }
  ]
}
```

### Example #5
  
```python  
  
from quicklyrics.lyrics import SearchByArtistAndSong  
  
res = SearchByArtistAndSong("Rihanna", "Love The Way You Lie Part II").results()  
  
```

> The above command will return the following:

```json
{
  "artist": "rihanna",
  "song": "lovethewayyouliepartii",
  "lyrics": [
    "\n\r\nOn the first page of our story\nThe future seemed so bright\nThen this thing turned out so evil\nI don't know why I'm still surprised\nEven angels have their wicked schemes\nAnd you take that to new extremes\nBut you'll always be my hero\nEven though you've lost your mind\n\nJust gonna stand there and watch me burn\nWell, that's alright because I like the way it hurts\nJust gonna stand there and hear me cry\nWell, that's alright because I love the way you lie\nI love the way you lie, oh\nI love the way you lie\n\nNow there's gravel in our voices\nGlass is shattered from the fight\nIn this tug of war, you'll always win\nEven when I'm right\n'Cause you feed me fables from your head\nWith violent words and empty threats\nAnd it's sick that all these battles\nAre what keeps me satisfied\n\nJust gonna stand there and watch me burn\nWell, that's alright because I like the way it hurts\nJust gonna stand there and hear me cry\nWell, that's alright because I love the way you lie\nI love the way you lie, oh\nI love the way you lie, oh\n\nSo maybe I'm a masochist\nI try to run, but I don't wanna ever leave\n'Til the walls are going up\nIn smoke with all our memories\n\nIt's morning, you wake, a sun ray hits your face\nSmeared makeup as we lay in the wake of destruction (Shh)\nHush baby, speak softly, tell me you're awfully sorry\nThat you pushed me into the coffee table last night so I can push you off me\nTry and touch me so I can scream at you not to touch me\nRun out the room and I'll follow you like a lost puppy\nBaby, without you, I'm nothing, I'm so lost, hug me\nThen tell me how ugly I am, but that you'll always love me\nThen after that, shove me, in the aftermath of the\nDestructive path that we're on, two psychopaths, but we\nKnow that no matter how many knives we put in each other's backs\nThat we'll have each other's backs 'cause we're that lucky\nTogether, we move mountains, let's not make mountains out of molehills\nYou hit me twice, yeah, but who's counting?\nI may have hit you three times, I'm starting to lose count\nBut together, we'll live forever, we found the youth fountain\nOur love is crazy, we're nuts, but I refused counseling\nThis house is too huge, if you move out, I'll burn all two thousand\nSquare feet of it to the ground, ain't shit you can do about it\n'Cause with you, I'm in my fucking mind, without you, I'm out it\n\nJust gonna stand there and watch me burn\nWell, that's alright because I like the way it hurts\nJust gonna stand there and hear me cry\nWell, that's alright because I love the way you lie\nI love the way you lie\nI love the way you lie\nI love the way you lie\nI love the way you lie\n",
    ""
  ]
}
```





