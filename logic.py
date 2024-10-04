from constants import TextMessages, AudioMessages, Buttons, START_COMMAND, returned_data
from data import music
from question import first_question, get_answer
from utils import get_random_element


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
    song = get_random_element(music)
    sound = song.get('sound')
    answer = song.get('answer')
    
    # Если сеанс новый, отправляем приветственное сообщение
    if session.get('new'):
        return welcome(session, version)
    
    if command in START_COMMAND:
        return first_question(session, version, command)
    
    return get_answer(session, version, command, song)

