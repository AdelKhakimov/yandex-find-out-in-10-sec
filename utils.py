import random


def get_random_element(arr):
    return random.choice(arr)


def get_song(music):
    song = get_random_element(music)
    return song


def returned_data(session, version, text_message, audio_message, buttons, song=None):
    if song:
        sound = song.get('sound')
        return {
        'response': {
            'text': text_message,
            'tts': audio_message + sound,
            'buttons': buttons,
            'end_session': 'false',
            'session': session,
        },
        'version': version
    }
    else:
        return {
            'response': {
                'text': text_message,
                'tts': audio_message,
                'buttons': buttons,
                'end_session': 'false',
                'session': session,
            },
            'version': version
        }
