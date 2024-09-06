from translate import Translator


def translate(value, from_lang, to_lang):
    translator = Translator(from_lang=from_lang, to_lang=to_lang)
    return translator.translate(value)


languages_list_1 = '~ English' + '\n' + '~ Russian' + '\n' + '~ German' + '\n' + '~ French' + '\n' + '~ Spanish' + '\n'
languages_list_2 = '~ Chinese' + '\n' + '~ Japanese' + '\n' + '~ Italian'
print("Here's the list of supported languages:" + '\n' + languages_list_1 + languages_list_2)
from_language = input('Language you want to translate from: ')
to_language = input('Language you want to translate to: ')
text_input = input('Text to translate: ')
try:
    result = translate(text_input, from_language, to_language)
    print(result)
except Exception as exception:
    print(f'Error: {exception}')
