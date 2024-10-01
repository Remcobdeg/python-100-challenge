
with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()

#create letters from sample letter
for name in names:
    name = name.strip()
    with open("Input/Letters/starting_letter.txt") as file:
        starting_letter = file.read()
    letter = starting_letter.replace("[name]",name) #note name.strip() also removes new line characters by default
    with open(f"Output/ReadyToSend/letter_{name}.txt",mode="w") as file:
        file.write(letter)
