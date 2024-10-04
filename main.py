from constants import TextMessages, AudioMessages

class Buttons:
    start_button = {'title': 'Начинаем', 'hide': True}
    capitulate_button = {'title': 'Сдаюсь', 'hide': True}
    repeat_button = {'title': 'Повтори', 'hide': True}
    stats_button = {'title': 'Статистика', 'hide': True}
    exit_button = {'title': 'Выход', 'hide': True}

def returned_data(session, version, text_message, audio_message, buttons):
    return {
        'response': {
            'text': text_message,
            'tts': audio_message,
            'buttons': [buttons],
            'end_session': 'false',
            'session': session,
        },
        'version': version
    }


def welcome(session, version):
    text_message = TextMessages.welcome_message.format(TextMessages.help_text)
    audio_message = AudioMessages.welcome_sound.format(TextMessages.help_text)
    buttons = Buttons.start_button
    #data = returned_data(session, version, text_message, audio_message, buttons)
    return print(returned_data(session, version, text_message, audio_message, buttons))

session = ''
version = ''

print(welcome(session, version))