import pandas as pd

# TODO Create Text to Morse Code converter( get data from .txt file using .readlines() )
# Open file with characters and their morse code translation
with open("morse.txt") as file:
    data = file.readlines()

# Create list of characters
characters: list = [letter.split("\t")[0] for letter in data]
# Create list of  morse code
morse_chars: list = [morse.split("\t")[1].split("\n")[0] for morse in data]


def encode(text: str) -> None:
    morse_code = []
    for letter in text:
        if letter == " ":
            morse_code.append("/")
        else:
            index = characters.index(letter.upper())
            morse_code.append(morse_chars[index])
    print(' '.join(morse_code))


def decode(text: str) -> None:
    decoded_text = []
    for morse in text.split(" "):
        if morse == "/":
            decoded_text.append(' ')
        else:
            morse_index = morse_chars.index(morse)
            decoded_text.append(characters[morse_index])
    print("".join(decoded_text))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    choice = input("To encode please enter 'E': , \nTo decode please enter 'D': \n")
    if choice == 'E':
        encode(input("Enter your text here: "))
    elif choice == 'D':
        decode(input("Enter morse code here: "))


# TODO Create Text to Morse Code converter( get data from .txt file using pandas )
# column_names: list = ['chars', 'morse']
# # Create a data frame with tables named chars and morse
# df = pd.read_csv('morse.txt', sep='\t', names=column_names)
#
#
# def encode(text: str) -> None:
#     morse_code = []
#     for letter in text:
#         if letter == " ":
#             morse_code.append('/')
#         else:
#             letter_index = df.index[df['chars'] == letter.upper()].tolist()[0]
#             single_letter = df['morse'].loc[letter_index]
#             morse_code.append(single_letter)
#     print(morse_code)
#     print(" ".join(morse_code))
#
#
# encode(input("Please enter your text:\n "))
#
#
# def decode(text: str) -> None:
#     decoded_text = []
#     for morse in text.split(" "):
#         if morse == "/":
#             decoded_text.append(' ')
#         else:
#             morse_index = df.index[df['morse'] == morse].tolist()[0]
#             single_latter = df['chars'].loc[morse_index]
#             decoded_text.append(single_latter)
#     print("".join(decoded_text))
#
#
# decode(input('Enter morse code: \n'))
#
# if __name__ == '__main__':
#     choice = input("To encode please enter: 'E', \nTo decode please enter: 'D' ")
#     if choice == 'E':
#         encode(input("Enter your text here: "))
#     elif choice == 'D':
#         decode(input("Enter morse code here: "))
