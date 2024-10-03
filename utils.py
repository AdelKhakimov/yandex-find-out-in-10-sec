import random


def get_random_element(arr):
    return random.choice(arr)


def get_random_song(music):
    if music.song.get('asked'):
        return get_random_song(music)
    else:
        return music.song


def get_random_song(music):
    song = get_random_element(music)
    i = 0
    while song.get('asked') and i < len(music):
        song = get_random_element(music)
        i += 1
    return song