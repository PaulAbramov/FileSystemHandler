import os
import shutil
from tqdm import tqdm
from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def move_files():
    print("Enter the path of the folder you want to move files from")
    path = input("Enter the path: ")

    if not os.path.exists(path):
        print("The path does not exist")
        exit()
    if not path:
        print("You did not enter a path")
        exit()

    # initialize the progress bar
    num_files = sum([len(files) for root, dirs, files in os.walk(path)])
    progress_bar = tqdm(total=num_files, desc="Copying files")

    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            source_filepath = os.path.join(dirpath, filename)
            destination_filepath = os.path.join(path, filename)
            shutil.copy(source_filepath, destination_filepath)
            try:
                shutil.rmtree(dirpath)
            except OSError as e:
                print(f"Error: {e.filename} - {e.strerror}")

            progress_bar.update(1)

    progress_bar.close()
    print("Done moving files")


if __name__ == '__main__':
    while True:
        clear()
        print("What do you want to do?")
        print("1. Move files out of subfolders to main folder")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Moving files out of subfolders to main folder")
            move_files()
        elif choice == "0":
            print("Exiting")
            exit()
