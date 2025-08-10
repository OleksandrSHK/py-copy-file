import os


def copy_file(command: str) -> None:
    if command == "":
        return
    command_list = command.split()
    if len(command_list) != 3:
        return
    _, source_path, destination_path = command_list
    if _ != "cp" or source_path == destination_path:
        return
    if not os.path.exists(source_path):
        return
    with (open(source_path, "r") as file_in,
          open(command_list[2], "w") as file_out):
        read_content = file_in.read()
        file_out.write(read_content)
