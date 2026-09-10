import sys
import time

def animated_lyrics(text, speed):
    for char in text:
        sys.stdout.write(char) #prints letters one by one
        sys.stdout.flush() #imediately shows the printed letter.
        time.sleep(speed) #Time gap between letters.
    print() #For new line

animated_lyrics("1", 0.4)
animated_lyrics("2", 0.4)
animated_lyrics("3", 0.4)
animated_lyrics("Start...", 0.04)
animated_lyrics(".", 0.1)
animated_lyrics(".", 0.1)
animated_lyrics("Tumi ar to karo nou, Shudhu amar...", 0.15)
animated_lyrics(".", 0.35)
animated_lyrics("Joto dure shore jaw, robe amar....", 0.17)
animated_lyrics(".", 0.48)
animated_lyrics("Stobdho shomoi taake dhore rekhe...", 0.15)
animated_lyrics(".", 0.45)
animated_lyrics("Sritir patay shudhu tumi amar..", 0.16)
animated_lyrics(".", 0.6)
animated_lyrics(".", 0.4)
animated_lyrics("Keno aaj eto eka ami....", 0.18)
animated_lyrics(".", 1.6)
animated_lyrics("Aloo hoyee dure tumi.....", 0.16)
animated_lyrics(".", 0.73)
animated_lyrics(".", 0.74)
animated_lyrics(".", 0.75)
animated_lyrics(".", 0.76)
animated_lyrics("Alo alo ami kokhono, khuje pabo na", 0.15)
animated_lyrics(".", 0.1)
animated_lyrics("Chaader alo tumi kokhono, amar hobe na...", 0.16)
animated_lyrics(".", 0.1)
animated_lyrics("Alo alo ami kokhono, khuje pabo naa.....", 0.17)
animated_lyrics(".", 0.1)
animated_lyrics("Chaader alo tumi kokhono, amar hobe na....", 0.15)
animated_lyrics(".", 0.15)
animated_lyrics("Hobe na....", 0.16)