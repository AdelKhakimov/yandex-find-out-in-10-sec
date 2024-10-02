import random

from data import music

def get_random_element(arr):
    return random.choice(arr)

def get_random_song(music):
    song = get_random_element(music)
    i = 0
    while song.get('asked') and i < len(music):
        song = get_random_element(music)
        i += 1
    return song
    

print(get_random_song(music))