Replacer = "[name]"

with open("./Input/Names/invited_names.txt") as file:
    listNames = file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    old_letter = letter.read()
    for name in listNames:
        name = name.strip()
        new_letter=old_letter.replace(Replacer, name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as a:
            a.write(new_letter)





