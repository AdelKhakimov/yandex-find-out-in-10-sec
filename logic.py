from constants import TextMessages, SoundMessages, Buttons, YES, NO, START_COMMAND
from data import music
from utils import get_random_element


def welcome(session, version):
    return {
        'response': {
            'text': TextMessages.welcome_message.format(TextMessages.help_text),
            #'tts': f'<speaker audio="alice-sounds-game-powerup-1.opus">{welcome_sound_message}'.format(help_sound),
            'buttons': [Buttons.start_button],
            'end_session': 'false',
            'session': session,
        },
        'version': version
    }


def first_question(session, version, sound):
    return {
        'response': {
            'text': TextMessages.first_question.format(len(music)),
            'tts': SoundMessages.sound_first_question.format(len(music), sound),
            'buttons': [
                Buttons.repeat_button,
                Buttons.capitulate_button,
                Buttons.stats_button,
                Buttons.exit_button
            ],
            'end_session': 'false',
            'session': session,
        },
        'version': version
    }


def correct_answer(session, version):
    return {
       'response': {
           'text': TextMessages.correct_answer.format(get_random_element(YES)),
           #'tts': f'<speaker audio="alice-sounds-game-powerup-1.opus">{sound_correct_answer.format('Правильно')}',
           'buttons': [
               Buttons.repeat_button,
               Buttons.capitulate_button,
               Buttons.stats_button,
               Buttons.exit_button
           ],
           'end_session': 'false',
           'session': session,
       },
       'version': version
   }


def incorrect_answer(session, version):
    return {
      'response': {
          'text': TextMessages.incorrect_answer.format(get_random_element(NO)),
           #'tts': f'<speaker audio="alice-sounds-game-powerup-1.opus">{sound_correct_answer.format('Правильно')}',
          'buttons': [
              Buttons.repeat_button,
              Buttons.capitulate_button,
              Buttons.stats_button,
              Buttons.exit_button
          ],
          'end_session': 'false',
          'session': session,
      },
      'version': version
  }


def get_random_song(music):
    song = get_random_element(music)
    i = 0
    while song.get('asked') and i < len(music):
        song = get_random_element(music)
        i += 1
    return song



def question(session, version):
    song = get_random_song(music)
    return {
      'response': {
          'text': TextMessages.incorrect_answer.format(get_random_element(NO)),
           #'tts': f'<speaker audio="alice-sounds-game-powerup-1.opus">{sound_correct_answer.format('Правильно')}',
          'buttons': [
              Buttons.repeat_button,
              Buttons.capitulate_button,
              Buttons.stats_button,
              Buttons.exit_button
          ],
          'end_session': 'false',
          'session': session,
      },
      'version': version
  }


def repeat(session, version):
    return 'повтори'


def handler(event, context):
    session = event.get('session', {})
    version = event.get('version', {})
    request = event.get('request', {})
    song = get_random_element(music)
    sound = song.get('sound')
    
    # Если сеанс новый, отправляем приветственное сообщение
    if session.get('new'):
        return welcome(session, version)
    
    if request.get('command') in START_COMMAND:
        return first_question(session, version, sound)

    if request.get('command') in song.get('answer'):
        return correct_answer(session, version)
    
    if request.get('command') not in song.get('answer'):
        return incorrect_answer(session, version)


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