

from http.cookies import Morsel


def decode_morse(morse_code):
    morse_code = morse_code.replace('  ', ' / ')
    morse_code = morse_code.split(' ')
    result = ''
    for i in range(len(morse_code)):
        if morse_code[i] == '/':
            result += ' '
        else:
            result += morse[morse_code[i]]
    return result


# Morse = {'A':'.-', 'B':'-...',
#         'C':'-.-.', 'D':'-..', 'E':'.',
#         'F':'..-.', 'G':'--.', 'H':'....',
#         'I':'..', 'J':'.---', 'K':'-.-',
#         'L':'.-..', 'M':'--', 'N':'-.',
#         'O':'---', 'P':'.--.', 'Q':'--.-',
#         'R':'.-.', 'S':'...', 'T':'-',
#         'U':'..-', 'V':'...-', 'W':'.--',
#         'X':'-..-', 'Y':'-.--', 'Z':'--..',
#         '1':'.----', '2':'..---', '3':'...--',
#         '4':'....-', '5':'.....', '6':'-....',
#         '7':'--...', '8':'---..', '9':'----.',
#         '0':'-----', ', ':'--..--', '.':'.-.-.-',
#         '?':'..--..', '/':'-..-.', '-':'-....-',
#         '(':'-.--.', ')':'-.--.-'}
 
morse = {'.-...': '&', '--..--': ',', '....-': '4', '.....': '5', 
'...---...': 'SOS', '-...': 'B', '-..-': 'X', '.-.': 'R', '.--': 'W', 
'..---': '2', '.-': 'A', '..': 'I', '..-.': 'F', '.': 'E', '.-..': 'L', 
'...': 'S', '..-': 'U', '..--..': '?', '.----': '1', '-.-': 'K', '-..': 'D', 
'-....': '6', '-...-': '=', '---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M', 
'-.': 'N', '....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';', 
'-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G', '--.-': 'Q', 
'--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C', '---...': ':', '-.--': 'Y', '-': 'T', 
'.--.-.': '@', '...-..-': '$', '.---': 'J', '-----': '0', '----.': '9', '.-..-.': '"', 
'-.--.': '(', '---..': '8', '...--': '3'}

res = decode_morse('...---...')
print(res)

# def decode_morse(morse_code):
#     morse_code = morse_code.replace('  ', ' / ')
#     print(morse_code)
#     result = ''
#     i = 0
#     l = len(morse_code)
#     for j in range(0, len(morse_code), 2):
#         for i in range(j, len(morse_code)):
#             while morse_code[i] == '.' or morse_code == '-' or morse_code == '/':
#                 result += morse_code[i]
#                 print(result)
#                 i += 1
#             else:
#                 # l -= len(result) - 1
#                 morse_code = morse_code.replace(result, morse[result])
#                 result = ''
#                 # i = 2
#                 print(l)
#                 break
        
#     return morse_code

# res = decode_morse('.... . -.--   .--- ..- -.. .')
# print(res)
