def copy_file(command: str) -> None:
    splitted_entry_command = command.split()

    if len(splitted_entry_command) != 3:
        return

    if splitted_entry_command[0] != "cp":
        return

    if splitted_entry_command[1] == splitted_entry_command[2]:
        return

    file_to_copy = splitted_entry_command[1]
    new_file = splitted_entry_command[2]

    try:
        with (open(file_to_copy, "r") as input_file,
              open(new_file, "w") as output_file):
            content = input_file.read()
            output_file.write(content)
    except FileNotFoundError:
        return
