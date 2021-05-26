import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
try:
    phonetic_df = pandas.read_csv('nato_phonetic_alphabet.csv')
except FileNotFoundError:
    print("File does not exists.")
    exit()
else:
    phonetic_dict = {row.letter: row.code for index, row in phonetic_df.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_input = input("Input a word:").upper()
    try:
        nato_word = [phonetic_dict[letter] for letter in user_input]
    except KeyError as error_message:
        print(f"The key {error_message} does exists. Entry only alphabets.")
        generate_phonetic()
    else:
        print(nato_word)


generate_phonetic()
