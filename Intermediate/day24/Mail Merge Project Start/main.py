PLACEHOLDERS = "[name]"  # <---- Esse é o termo que queremos substituir do arquivo "starting_letter.txt"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()  # <---- transforma items em uma lista.  ex. ["Aang\n", "Katara\n", "Momo"]
    # print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()  # <---- Remove espaços antes e depois do intem selecionado. No caso o "\n"
        new_letter = letter_contents.replace(PLACEHOLDERS, stripped_name)  # <---- Um arquivo só com convites ind.
        # print(new_letter)
        with open(f"./Output/ReadyToSend/Letter_for_{stripped_name}.txt", mode = "w") as completed_letter:
            completed_letter.write(new_letter)


