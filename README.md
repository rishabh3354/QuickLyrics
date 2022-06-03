<h6 align="center">
  <img src="https://img.icons8.com/ios-glyphs/344/audio-skimming.png" alt="LyricsPy" height="250px">
  <h5 align="center">Powerful library to search for music lyrics.</h5>
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


search = Musixmatch("Musixmatch key").auto("Hello",lang="pt" , limit=1)

with open("lyrics.json", "w") as f:
  dump(search, f)
```