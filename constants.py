YES = ['Верно', 'Правильно', 'Да', 'Отлично']
NO = ['Нет', 'Неправильно', 'Неверно', 'Неугадал']

START_COMMAND = ['начинаем', 'да']
HELP_COMMAND = ['помощь', 'помоги']
REPEAT_COMMAND = ['повтори', 'повтор']
CAPITULATE_COMMAND = ['сдаюсь', 'пас', 'пропустить', 'пропусти', 'не знаю']
EXIT_COMMAND = ['выход', 'хватит']

WIN_SOUND_URLS = [
    '<speaker audio="alice-sounds-game-win-1.opus">',
    '<speaker audio="alice-sounds-game-win-2.opus">',
    '<speaker audio="alice-sounds-game-win-3.opus">'
]
LOSE_SOUND_URLS = [
    '<speaker audio="alice-sounds-game-loss-1.opus">',
    '<speaker audio="alice-sounds-game-loss-2.opus">',
    '<speaker audio="alice-sounds-game-loss-3.opus">'
]

class TextMessages:
    repeate_text = '↩ Чтобы повторить отрывок, нажмите на "Повтори".\n'
    capitulate_text = '🙁 Если не знаете, нажмите на "Сдаюсь", "Пас" или "Пропусти".\n'
    stats_text = '📊 Чтобы узнать текущий счет, нажмите на "Статистика".\n'
    exit_text = '🚪 Для выхода из игры нажмите на "Выход".\n'


    help_text = '{} {} {} {}\n Чтобы вывести список команд еще раз, нажмите: "Алиса, помощь".'.format(repeate_text, capitulate_text, stats_text, exit_text)

    welcome_message = '👋 Привет.\n Ваша задача - отгадать музыкальное произведение по десяти секундному отрывку.\n{}🚩 Начинаем игру?'.format(help_text)
    first_question = '👍 Отлично.\nКоличество вопросов на данный момент: {}.\nПрослушайте первый отрывок ➡'

    correct_answer = '😎 {}!\nСледующий вопрос ➡'
    incorrect_answer = '{}!\nПопробуйте еще раз'


class AudioMessages:
    repeate_sound = '↩ Чтобы повторить отрывок, скажите "Повтори".'
    capitulate_sound = 'Если не знаете, скажите "Пас" или "Пропусти".'
    stats_sound = 'Чтобы узнать текущий счет, скажите "Статистика".'
    exit_sound = 'Для выхода из игры скажите "Выход".'

    help_sound = '{} {} {} {} Чтобы вывести список команд еще раз, скажите: "Алиса, помощь".'.format(repeate_sound, capitulate_sound, stats_sound, exit_sound)

    welcome_sound = 'Привет.\nВаша задача - отгадать музыкальное произведение по десяти секундному отрывку.\n{} Начинаем игру?'.format(help_sound)
    sound_first_question = 'Отлично.\nКоличество вопросов на данный момент: {}.\nПрослушайте первый отрывок ➡ {}'

    correct_answer_sound = '{}!\nСледующий вопрос ➡'
    incorrect_answer_sound = '{}!\nПопробуйте еще раз'


class Buttons:
    start_button = [{'title': 'Начинаем', 'hide': True}]
    capitulate_button = [{'title': 'Сдаюсь', 'hide': True}]
    repeat_button = [{'title': 'Повтори', 'hide': True}]
    stats_button = [{'title': 'Статистика', 'hide': True}]
    exit_button = [{'title': 'Выход', 'hide': True}]

    menu_buttons = [
        {'title': 'Сдаюсь', 'hide': True},
        {'title': 'Повтори', 'hide': True},
        {'title': 'Статистика', 'hide': True},
        {'title': 'Выход', 'hide': True}
    ]


class MusicUrls:
    univers_infinity = '<speaker audio="dialogs-upload/c7a8dcad-a0bc-4db1-94c8-165114718f42/495dcdff-efc6-4493-a197-ea95fc448b12.opus">'


def returned_data(session, version, text_message, audio_message, buttons):
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
