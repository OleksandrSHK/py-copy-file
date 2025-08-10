import os


def copy_file(command: str) -> None:
    if command == "":
        return
    command_list = command.split()
    if len(command_list) != 3:
        return
    if command_list[0] != "cp" or command_list[1] == command_list[2]:
        return
    if not os.path.exists(command_list[1]):
        return
    with (open(command_list[1], "r") as file_in,
          open(command_list[2], "w") as file_out):
        read_content = file_in.read()
        file_out.write(read_content)
