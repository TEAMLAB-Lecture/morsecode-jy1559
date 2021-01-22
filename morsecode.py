# -*- coding: utf8 -*-


# Help Function - 수정하지 말 것
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code


# Help Function - 수정하지 말 것
def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()

    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"

    return message


def is_help_command(user_input):
    if user_input.lower() == 'help' or user_input.lower() == 'h': return True
    else: return False


def is_validated_english_sentence(user_input):
    n = 0
    t = ['_','@','#','$','%','^','&','*','(',')','-','+','=','[',']','{','}','\"','\'', ';',':','|','\\','~']
    m = ['.',',','!','?',' ']
    for x in user_input:
        if x.isdigit() or x in t: return False
        if x not in m: n+=1
    if n: return True
    else: return False


def is_validated_morse_code(user_input):
    morse = get_morse_code_dict()
    one = ''
    for x in ' '.join(user_input.split()):
        if x != '-' and x != '.' and x != ' ' : return False
        if x == ' ':
            if one not in list(morse.values()): return False
            one = ''
        else: one += x
    if one not in list(morse.values()): return False
    return True



def get_cleaned_english_sentence(raw_english_sentence):
    result = ''
    m = ['.',',','!','?']
    for x in ' '.join(raw_english_sentence.strip().split()):
        if x not in m:
            result += x

    return result


def decoding_character(morse_character):
    morse = get_morse_code_dict()
    for i in range(65,91):
        if morse[chr(i)] == morse_character: return chr(i)


def encoding_character(english_character):
    morse = get_morse_code_dict()
       
    return morse[english_character.upper()]


def decoding_sentence(morse_sentence):
    result = ''
    one = ''
    for x in morse_sentence:
        if x == ' ':
            if one == '':
                result += ' '
            else:
                result += decoding_character(one)
                one = ''
        else: one += x
    result += decoding_character(one)
    return result


def encoding_sentence(english_sentence):
    result = ''
    sentence = get_cleaned_english_sentence(english_sentence)
    for x in sentence:
        if x == ' ': result += ' '
        else: result += encoding_character(x)+' '
    return result[:-1]


def main():
    print("Morse Code Program!!")
    end = False
    while not end:
        sentence = input('Input your message(H - Help, 0 - Exit) : ')
        do = ''
        if sentence == '0':
            end = True
        elif is_help_command(sentence):
            print(get_help_message())
        elif is_validated_english_sentence(sentence):
            do = 'encode'
        elif is_validated_morse_code(sentence):
            do = 'decode'
        else: do = 'wrong'

        if do == 'decode':
            print(decoding_sentence(sentence))
        elif do == 'encode':
            print(encoding_sentence(sentence))
        elif do == 'wrong':
            print('Wrong Input')
    print("Good Bye")
    print("Morse Code Program Finished!!")

if __name__ == "__main__":
    main()
