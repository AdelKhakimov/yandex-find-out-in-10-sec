from constants import (
    TextMessages, AudioMessages, Buttons, 
    YES, NO,
    WIN_SOUND_URLS, LOSE_SOUND_URLS
)
from data import music
from utils import get_random_element, get_song, returned_data


class Command:

    def __init__(self, session, version):
        self.session = session
        self.version = version


    def welcome(self):
        text_message = TextMessages.welcome_message
        audio_message = f'<speaker audio="alice-sounds-game-powerup-1.opus">{AudioMessages.welcome_sound}'
        buttons = Buttons.start_button
        return returned_data(self.session, self.version, text_message, audio_message, buttons)


    def first_question(self, song):
        sound = song.get('sound')
        text_message = TextMessages.first_question.format(len(music))
        audio_message = AudioMessages.sound_first_question.format(len(music), sound)
        buttons = Buttons.menu_buttons
        return returned_data(self.session, self.version, text_message, audio_message, buttons)


    def correct_answer(self):
        text_message = TextMessages.correct_answer.format(get_random_element(YES))
        audio_message = f'{get_random_element(WIN_SOUND_URLS)}{AudioMessages.correct_answer_sound.format(get_random_element(YES))}'
        buttons = Buttons.menu_buttons
        song = get_song(music)
        return returned_data(self.session, self.version, text_message, audio_message, buttons, song)


    def incorrect_answer(self):
        text_message = TextMessages.incorrect_answer.format(get_random_element(NO))
        audio_message = f'{get_random_element(LOSE_SOUND_URLS)}{AudioMessages.incorrect_answer_sound.format(get_random_element(NO))}'
        buttons = Buttons.menu_buttons
        return returned_data(self.session, self.version, text_message, audio_message, buttons)


    def help_command(self):
        text_message = TextMessages.help_text
        audio_message = AudioMessages.help_sound
        buttons = Buttons.menu_buttons
        return returned_data(self.session, self.version, text_message, audio_message, buttons)


    def repeat_command(self):
        text_message = TextMessages.repeate_text
        audio_message = AudioMessages.repeate_sound
        buttons = Buttons.menu_buttons
        return returned_data(self.session, self.version, text_message, audio_message, buttons)


    def capitulate_command(self):
        text_message = TextMessages.capitulate_text
        audio_message = AudioMessages.capitulate_sound
        buttons = Buttons.menu_buttons
        return returned_data(self.session, self.version, text_message, audio_message, buttons)


    def exit_command(self):
        text_message = TextMessages.exit_text
        audio_message = AudioMessages.exit_sound
        buttons = Buttons.menu_buttons
        return returned_data(self.session, self.version, text_message, audio_message, buttons)


    def get_answer(self, command, song):
        if command in song.get('answer'):
            return self.correct_answer()
        else:
            return self.incorrect_answer()


command_handler = Command(session, version)
welcome = command_handler.welcome()
