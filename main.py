from constants import TextMessages, AudioMessages

class Buttons:
    start_button = {'title': 'Начинаем', 'hide': True}
    capitulate_button = {'title': 'Сдаюсь', 'hide': True}
    repeat_button = {'title': 'Повтори', 'hide': True}
    stats_button = {'title': 'Статистика', 'hide': True}
    exit_button = {'title': 'Выход', 'hide': True}

def returned_data(session, version, text_message, audio_message, buttons, song=None):
    return {
        'response': {
            'text': text_message,
            'tts': audio_message,
            'buttons': buttons,
            'end_session': 'false',
            'session': session,
        },
        'version': version
    }, song



def welcome(session, version):
    text_message = TextMessages.welcome_message.format(TextMessages.help_text)
    audio_message = AudioMessages.welcome_sound.format(TextMessages.help_text)
    buttons = Buttons.start_button
    #data = returned_data(session, version, text_message, audio_message, buttons)
    song = 123
    return print(returned_data(session, version, text_message, audio_message, buttons, song))

session = ''
version = ''

print(welcome(session, version))


'''
def main():
    # Пример данных для теста
    
    event = {
        'request': {},
        'session': {'new': True},
        'state': {},
        'version': '1.0'
    }
    context = {}
   
    #response = handler(event, context)
    song = get_random_element(music)

    print(song.get('answer')[0])
    

if __name__ == "__main__":
    main()
'''
