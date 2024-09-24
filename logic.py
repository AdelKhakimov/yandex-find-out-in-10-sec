class Message:

    welcome_message = '👋 Привет.\ Ваша задача - отгадать музыкальное произведение по десяти секундному отрывку.\n{}🚩 Начинаем игру?'
    repeat_text = '↩ Чтобы повторить отрывок, нажмите на "Повтори".\n'
    capitulate_text = '🙁 Если не знаете, нажмите на "Сдаюсь", "Пас" или "Пропусти".\n'
    stats_text = '📊 Чтобы узнать текущий счет, нажмите на "Статистика".\n'
    exit_text = '🚪 Для выхода из игры нажмите на "Выход"\n'

    first_question = '👍 Отлично.\nКоличество вопросов на данный момент: {}.\nПрослушайте первый отрывок ➡'
    correct_answer = '😎 {}!\nСледующий вопрос ➡'

    help_text = '{} {} {} {}\nℹ Чтобы вывести список команд еще раз, нажмите: "Алиса, помощь".'.format(repeat_text, capitulate_text, stats_text, exit_text)


class Buttons:
    start_button = {'title': 'Начинаем', 'hide': True}
    capitulate_button = {'title': 'Сдаюсь', 'hide': True}
    repeat_button = {'title': 'Повтори', 'hide': True}
    stats_button = {'title': 'Статистика', 'hide': True}
    exit_button = {'title': 'Выход', 'hide': True}

def welcome(session, version):
    return {
        'response': {
            'text': Message.welcome_message.format(Message.help_text),
            #'tts': f'<speaker audio="alice-sounds-game-powerup-1.opus">{welcome_sound_message}'.format(help_sound),
            'buttons': [Buttons.start_button],
            'end_session': 'false',
            'session': session,
        },
        'version': version
    }


def handler(event, context):
    request = event.get('request', {})
    session = event.get('session', {})
    state = event.get('state', {})
    version = event.get('version', {})
    
    # Данные о текущем состоянии сессии и пользователя
    session_state = state.get('session', {})
    user_state = state.get('user', {})
    
    # Если сеанс новый, отправляем приветственное сообщение
    if session.get('new'):
        return welcome(session, version)
