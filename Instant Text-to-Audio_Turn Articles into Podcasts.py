#Instant text to Audio (turn Articles into Podcasts) 

from gtts import gTTS
import os

#Run: pip install gTTS

text = """What dictionaries do I need?
Abilingual dictionary [using two languages] is easy for you to understand, and quick and
easy to use. A dictionary in English will give you reading practice in English and many more
examples of how words are used. If possible, use both. These are good dictionaries in English
for your level, and most of them are available online:
Cambridge Learner’s Dictionary
Oxford Wordpower Dictionary
Longman Active Study Dictionary
B Information in dictionaries
Macmillan Essential Dictionary
If you look up a word [find a word in a dictionary] using the Cambridge Learner’s Dictionary, the
information is shown like this:"""

tts = gTTS(text=text, lang='en')
tts.save("audiobook.mp3")
os.system("start audiobook.mp3") #Opens automatically on Windows(use 'open' on Mac)