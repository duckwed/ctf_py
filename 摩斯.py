'''摩斯码'''

CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.',

        '.': '.-.-.-', ': ':'---...', ',': '--..--', ';': '-.-.-.',
        '?': '..--..', '=': '-...-', '"': '.----.', '//': '-..-.',
        '!': '-.-.--', '-': '-....-', '_': '..--.-'
}

CODE_2 = dict(zip(CODE.values(), CODE.keys()))

txt = "..-. .-.. .- --. . --... .---- -.-. .- ..... -.-. -.. -....- --... -.. -... ----. -....- ....- -... .- ...-- -....- ----. ...-- ---.. ...-- -....- .---- .- ..-. ---.. -.... --... ---.. ---.. .---- ..-. ----- --..."

def char2morse(c):
    '''字符转摩斯'''
    return CODE[c]

def morse2char(c):
    '''摩斯转字符'''
    return CODE_2[c].lower()

gettxt = ''.join(morse2char(s) for s in txt.split())

# print(' '.join(char2morse(c) for c in 'SOS'))
print(gettxt.lower())


