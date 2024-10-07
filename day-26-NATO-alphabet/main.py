import pandas as pd

alphabet_df = pd.read_csv("nato_phonetic_alphabet.csv")

# alphabet_dict = {row.values[0]:row.values[1] for (index,row) in alphabet_df.iterrows()}
alphabet_dict = {row.letter:row.code for (index,row) in alphabet_df.iterrows()}

def ask_word():
    return input("Give a word to convert to phonetic code\n")

completed = False

while not completed:
    word = ask_word()
    try:
        output = [alphabet_dict[letter] for letter in word.upper()]
    except KeyError:
        print("Only words please")
    else:
        print(output)
        completed = True

