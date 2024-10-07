from constants import (
    TextMessages, AudioMessages, Buttons,
    START_COMMAND, HELP_COMMAND, REPEAT_COMMAND, CAPITULATE_COMMAND, EXIT_COMMAND,
    returned_data
)
from data import music
from question import (
    first_question, get_answer, help_command, repeate_command, capitulate_command, exit_command
)
from utils import get_song

def welcome(session, version):
    text_message = TextMessages.welcome_message
    audio_message = f'<speaker audio="alice-sounds-game-powerup-1.opus">{AudioMessages.welcome_sound}'
    buttons = Buttons.start_button

    return returned_data(session, version, text_message, audio_message, buttons)


def repeat(session, version):
    return 'повтори'


def handler(event, context):
    session = event.get('session', {})
    version = event.get('version', {})
    request = event.get('request', {})
    command = request.get('command', {})
    song = get_song(music)
    sound = song.get('sound')
    answer = song.get('answer')
    
    if session.get('new'):
        return welcome(session, version)

    if command in START_COMMAND:
        return first_question(session, version, command, song)
    
    elif command in HELP_COMMAND:
        return help_command(session, version)
    
    elif command in REPEAT_COMMAND:
        return repeate_command(session, version)
    
    elif command in CAPITULATE_COMMAND:
        return capitulate_command(session, version)
    
    #elif command in EXIT_COMMAND(session, version): пока вызывает ошибку list object is not iterable
    #    return exit_command(session, version)
    
    return get_answer(session, version, command, song)

