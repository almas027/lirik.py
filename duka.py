import time
import sys
from threading import Thread

def animate_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("Sampai kini masih ku coba", 0.10),
        ("Tuk terjaga dari mimpiku", 0.10),
        ("Yang buat ku tak sadar", 0.10),
        ("Bahwa kau bukan lagi milikku", 0.08),
        ("Walau hati tak akan pernah", 0.08),
        ("Dapat melupakan dirimu", 0.08),
        ("Dan tiap tetes air mata", 0.08),
        ("yang jatuh kuatkan rinduku......", 0.08)
    ]

    delays = [1, 0.53, 0.48, 1, 1, 1.5, 1, 1]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    sing_song()
