def copy_file(command: str) -> None:
    splitted_entry_command = command.strip().split()

    if len(splitted_entry_command) != 3 or splitted_entry_command[0] != "cp":
        return

    file_to_copy = splitted_entry_command[1]
    new_file = splitted_entry_command[2]

    if file_to_copy == new_file:
        return

    try:
        with open(file_to_copy, "r") as f_in, open(new_file, "w") as f_out:
            f_out.write(f_in.read())
    except FileNotFoundError:
        return
