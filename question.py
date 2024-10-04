from constants import (
    TextMessages, AudioMessages, Buttons, 
    returned_data, YES, NO,
    START_COMMAND, HELP_COMMAND, REPEAT_COMMAND, CAPITULATE_COMMAND,
    WIN_SOUND_URLS, LOSE_SOUND_URLS
)
from data import music
from utils import get_random_element


def first_question(session, version, command):

    song = get_song(session, version, command)
    sound = song.get('sound')
    text_message = TextMessages.first_question.format(len(music))
    audio_message = AudioMessages.sound_first_question.format(len(music), sound)
    buttons = Buttons.menu_buttons

    return returned_data(session, version, text_message, audio_message, buttons)


def correct_answer(session, version):
    text_message = TextMessages.correct_answer.format(get_random_element(YES))
    #audio_message = f'<speaker audio="alice-sounds-game-powerup-1.opus">{AudioMessages.correct_answer_sound}'
    audio_message = f'{get_random_element(WIN_SOUND_URLS)}{AudioMessages.correct_answer_sound.format(get_random_element(YES))}'
    buttons = Buttons.menu_buttons

    return returned_data(session, version, text_message, audio_message, buttons)


def incorrect_answer(session, version):
    text_message = TextMessages.incorrect_answer.format(get_random_element(NO))
    #audio_message = f'<speaker audio="alice-sounds-game-loss-1.opus">{AudioMessages.incorrect_answer_sound}'
    audio_message = f'{get_random_element(LOSE_SOUND_URLS)}{AudioMessages.incorrect_answer_sound.format(get_random_element(NO))}'
    buttons = Buttons.menu_buttons

    return returned_data(session, version, text_message, audio_message, buttons)


def help_command(session, version):
    pass


def repeate_command(session, version):
    pass


def capitulate_command(session, version):
    pass


def exit_command(session, version):
    pass


def get_song(session, version, command):
    song = get_random_element(music)
    return song


def get_answer(session, version, command, song):
    if command in song.get('answer'):
        return correct_answer(session, version)
    else:
        return incorrect_answer(session, version)
    

def check_answer(session, version, command):
    song = ...

    if command in START_COMMAND:
        return first_question(session, version, command)
    
    elif command in HELP_COMMAND:
        return help_command(session, version)
    
    elif command in REPEAT_COMMAND:
        return repeate_command(session, version)
    
    elif command in CAPITULATE_COMMAND:
        return capitulate_command(session, version)
    
    elif command in exit_command(session, version):
        return exit_command(session, version)
    
    return get_answer(session, version, command, song)


