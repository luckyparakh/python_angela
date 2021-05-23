import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

phonetic_df = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_dict = {row.letter: row.code for index, row in phonetic_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Input a word:").upper()
nato_word = [phonetic_dict[letter] for letter in user_input]
print(nato_word)

