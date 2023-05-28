users_words_greetings = ["привет",
                   "утро",
                   "день",
                   "вечер",
                   "ночь",
                   "хай",
                   "ку",
                   "салют"
                         ]

users_words_how_are_you = ["дела?",
                           "дела",
                           "как дела",
                           "как дела?",
                           "как жизнь?"]

bot_words_greetings = { 1: "Привет!",
                        2: "Доброе утро!",
                        3: "Добрый день!",
                        4: "Добрый вечер!",
                        5: "Доброй ночи!",
                        6: "Салют!"}

bot_words_greetings_with_error = ["я не понимаю вашего приветствия ",
                                  "не несите чушь",
                                  "я ушел в магазин..."]

bot_words_how_are_you = {1: "хорошо",
                         2: "все идет по плану",
                         3: "хочу домой",
                         4: "отлично!!"
                        }
message = None

def check_command_prefix(message) -> bool:
    import system_data
    if message.startswith(bot_data.command_prefix):
        return True
    return False

class MessageCommand:
    pass


class DefaultCommand:

    @staticmethod
    def get_word_greeting(word: str = "") -> str:
        from random import randint
        index = randint(0, len(bot_words_greetings))
        return bot_words_greetings[index]


    @staticmethod
    def get_word_how_are_you(word: str = "") -> str:
        from random import randint
        index = randint(0, len(bot_words_how_are_you))
        return bot_words_how_are_you[index]


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
        for i in users_words_greetings:
            if i in message:
                return True, i
        return False, None


    @staticmethod
    def check_how_are_you(message : str) -> tuple:
        for i in users_words_how_are_you:
            if i in message:
                return True, i
        return False, None

