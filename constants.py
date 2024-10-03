YES = ['Верно', 'Правильно', 'Да', 'Отлично']
NO = ['Нет', 'Неправильно', 'Неверно', 'Неугадал']
START_COMMAND = ['начинаем', 'да']

class TextMessages:
    welcome_message = '👋 Привет.\n Ваша задача - отгадать музыкальное произведение по десяти секундному отрывку.\n{}🚩 Начинаем игру?'
    repeat_text = '↩ Чтобы повторить отрывок, нажмите на "Повтори".\n'
    capitulate_text = '🙁 Если не знаете, нажмите на "Сдаюсь", "Пас" или "Пропусти".\n'
    stats_text = '📊 Чтобы узнать текущий счет, нажмите на "Статистика".\n'
    exit_text = '🚪 Для выхода из игры нажмите на "Выход"\n'

    first_question = '👍 Отлично.\nКоличество вопросов на данный момент: {}.\nПрослушайте первый отрывок ➡'

    correct_answer = '😎 {}!\nСледующий вопрос ➡'
    incorrect_answer = '{}!\nПопробуйте еще раз'

    help_text = '{} {} {} {}\nℹ Чтобы вывести список команд еще раз, нажмите: "Алиса, помощь".'.format(repeat_text, capitulate_text, stats_text, exit_text)


class SoundMessages:
    sound_first_question = '👍 Отлично.\nКоличество вопросов на данный момент: {}.\nПрослушайте первый отрывок ➡ {}'
    sound_correct_answer = '😎 {}!\nСледующий вопрос ➡'


class Buttons:
    start_button = {'title': 'Начинаем', 'hide': True}
    capitulate_button = {'title': 'Сдаюсь', 'hide': True}
    repeat_button = {'title': 'Повтори', 'hide': True}
    stats_button = {'title': 'Статистика', 'hide': True}
    exit_button = {'title': 'Выход', 'hide': True}


class MusicUrls:
    univers_infinity = '<speaker audio="dialogs-upload/c7a8dcad-a0bc-4db1-94c8-165114718f42/495dcdff-efc6-4493-a197-ea95fc448b12.opus">'