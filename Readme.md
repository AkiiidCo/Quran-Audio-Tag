# Quran Audio Tag

Quran Audio Tag allows you to easily tag a list of quran that you've downloaded from the web.
This allows you to easily add a Title with the surah names, artist, album, and genre with a quick executable

I noticed that the internet is filled with Quran, but anytime I download a new reciter there was no meta information. Even titles and surah numbers were not always reliable. This tool cleans that data up in a second

## Setup

Python 3 and PIP is required

#### Install python requirements

pip install -r requirements.txt

#### Add your Quran inside the Audio folder

#### Run the main.py with command line args

```bash
python main.py ./Audio "Mishary Alafasy" "Quran Mishary Alafasy"
```

- Arg 1 is the folder of the audio
- Arg 2 is the name of the reciter/artist
- Arg 3 is the name of the album
