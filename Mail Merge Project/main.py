# Placeholder string that will be replaced in the letter template
Replacer = "[name]"

# Open and read the list of names from the invited_names.txt file
with open("./Input/Names/invited_names.txt") as file:
    # Read each line (name) from the file and store it in a list
    listNames = file.readlines()

# Open and read the template letter from starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as letter:
    old_letter = letter.read()
    
    for name in listNames:
        # Strip any leading/trailing whitespace characters from the name
        name = name.strip()
        
        # Replace the placeholder [name] in the template with the actual name
        new_letter = old_letter.replace(Replacer, name)
        
        # The file is saved as 'letter_for_<name>.txt' in the ReadyToSend folder
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as a:
            a.write(new_letter)
