from playsound import playsound
import threading

file_paths = [
    'a/bruh.mp3',
    'a/ze-da-manga_G3QwWGi.mp3',
    'a/happy-happy-happy-song.mp3',
    'a/z-z-z-z-z-z.mp3',
    'a/oh-my-god-meme.mp3',
    'a/snore-mimimimimimi.mp3',
    'a/george-micael-wham-careless-whisper-1.mp3',
    'a/toothless-dancing_rT0J7Pn.mp3',
    'a/indian-music-mp3.mp3',
    'a/that-one-josh-hutcherson-whistle-edit.mp3',
    'a/bad-to-the-bone-meme.mp3'
]

def play_sound(file_path):
    while True:
        playsound(file_path)

threads = []

for file_path in file_paths:
    thread = threading.Thread(target=play_sound, args=(file_path,))
    thread.start()
    threads.append(thread)

# Mantém o programa principal em execução
for thread in threads:
    thread.join()
