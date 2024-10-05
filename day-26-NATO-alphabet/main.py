import pandas as pd

alphabet_df = pd.read_csv("nato_phonetic_alphabet.csv")

# alphabet_dict = {row.values[0]:row.values[1] for (index,row) in alphabet_df.iterrows()}
alphabet_dict = {row.letter:row.code for (index,row) in alphabet_df.iterrows()}


print(alphabet_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Give a word to convert to phonetic code\n")

output = [alphabet_dict[letter] for letter in word.upper()]

print(output)