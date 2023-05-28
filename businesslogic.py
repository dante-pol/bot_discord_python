import system_data
def check_command_prefix(message) -> bool:
    import system_data
    if message.startswith(system_data.command_prefix):
        return True
    return False

class MessageCommand:
    pass


class DefaultCommand:

    @staticmethod
    def get_word_greeting(word: str = "") -> str:
        from random import randint
        index = randint(0, len(system_data.bot_words_greetings))
        return system_data.bot_words_greetings[index]


    @staticmethod
    def get_word_how_are_you(word: str = "") -> str:
        from random import randint
        index = randint(0, len(system_data.bot_words_how_are_you))
        return system_data.bot_words_how_are_you[index]


    @staticmethod
    def start_pars_to_message(text : str) -> str:
        greeting = DefaultCommand.check_greeting(text)
        how_are_you = DefaultCommand.check_how_are_you(text)
        if greeting[0] == True:
            return DefaultCommand.get_word_greeting()
        elif how_are_you[0] == True:
            return DefaultCommand.get_word_how_are_you()
        elif greeting[0] == True and how_are_you[0] == True:
            return DefaultCommand.get_word_greeting() + DefaultCommand.get_word_how_are_you()


    @staticmethod
    def check_greeting(message : str) -> tuple:
        for i in system_data.users_words_greetings:
            if i in message:
                return True, i
        return False, None


    @staticmethod
    def check_how_are_you(message : str) -> tuple:
        for i in system_data.users_words_how_are_you:
            if i in message:
                return True, i
        return False, None

