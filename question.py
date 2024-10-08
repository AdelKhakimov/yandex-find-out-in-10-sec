from constants import (
    TextMessages, AudioMessages, Buttons, 
    returned_data, YES, NO,
    START_COMMAND, HELP_COMMAND, REPEAT_COMMAND, CAPITULATE_COMMAND, EXIT_COMMAND,
    WIN_SOUND_URLS, LOSE_SOUND_URLS
)
from data import music
from utils import get_random_element, get_song


def first_question(session, version, command, song):
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
    song = get_song(music)
    next_question = get_question(session, version, song)
    return returned_data(session, version, text_message, audio_message, buttons, next_question)


def incorrect_answer(session, version):
    text_message = TextMessages.incorrect_answer.format(get_random_element(NO))
    #audio_message = f'<speaker audio="alice-sounds-game-loss-1.opus">{AudioMessages.incorrect_answer_sound}'
    audio_message = f'{get_random_element(LOSE_SOUND_URLS)}{AudioMessages.incorrect_answer_sound.format(get_random_element(NO))}'
    buttons = Buttons.menu_buttons
    return returned_data(session, version, text_message, audio_message, buttons)


def help_command(session, version):
    text_message = TextMessages.help_text
    audio_message = AudioMessages.help_sound
    buttons = Buttons.menu_buttons
    return returned_data(session, version, text_message, audio_message, buttons)


def repeate_command(session, version):
    text_mesage = TextMessages.repeate_text
    audio_message = AudioMessages.repeate_sound
    buttons = Buttons.menu_buttons
    return returned_data(session, version, text_mesage, audio_message, buttons)


def capitulate_command(session, version):
    text_message = TextMessages.capitulate_text
    audio_message = AudioMessages.capitulate_sound
    buttons = Buttons.menu_buttons
    return returned_data(session, version, text_message, audio_message, buttons)


def exit_command(session, version):
    text_message = TextMessages.exit_text
    audio_message = AudioMessages.exit_sound
    buttons = Buttons.menu_buttons
    return returned_data(session, version, text_message, audio_message, buttons)


def get_answer(session, version, command, song):
    if command in song.get('answer'):
        return correct_answer(session, version)
    else:
        return incorrect_answer(session, version)


def get_question(session, version, song):
    sound = song.get('sound')
    buttons = Buttons.menu_buttons
    return returned_data(session, version, sound, buttons)
    

def check_answer(session, version, command, song):

    if command in START_COMMAND:
        return first_question(session, version, command)
    
    elif command in HELP_COMMAND:
        return help_command(session, version)
    
    elif command in REPEAT_COMMAND:
        return repeate_command(session, version)
    
    elif command in CAPITULATE_COMMAND:
        return capitulate_command(session, version)
    
    elif command in EXIT_COMMAND(session, version):
        return exit_command(session, version)
    
    return get_answer(session, version, command, song)


