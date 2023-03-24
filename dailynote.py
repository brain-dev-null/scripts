import argparse
import sys

from dataclasses import dataclass
from datetime import datetime
from os import environ, makedirs, path
from pathlib import Path


HOME_PATH = Path.home()
NOTES_DIRECTORY_NAME = "daily_notes"
EDITOR = environ["EDITOR"]

DEFAULT_NOTES_BASE_DIRECTORY = path.join(HOME_PATH, NOTES_DIRECTORY_NAME)


@dataclass
class Note:
    filename: str
    directory: str
    default_title: str

    @property
    def full_path(self) -> str:
        return path.join(self.directory, self.filename)


def get_note(notes_base_directory: str) -> Note:

    now = datetime.now()

    year = str(now.year)
    month = f"{now.month:02}"
    day = f"{now.day:02}"

    filename = f"{year}-{month}-{day}_note.md"
    directory = path.join(notes_base_directory, year, month)
    default_title = f"# Daily Note {year}-{month}-{day}"

    return Note(filename, directory, default_title) 


def create_note(note: Note) -> None:
    makedirs(note.directory, exist_ok=True)

    with open(note.full_path, "w") as note_file:
        note_file.write(note.default_title + "\n")

    

def main(notes_base_directory: str) -> None:
    note = get_note(notes_base_directory)

    if not path.isfile(note.full_path):
        create_note(note)
    
    print(note.full_path)


if __name__ == "__main__":


    parser = argparse.ArgumentParser(prog="dailynote.py")

    parser.add_argument(
        "notes_base_directory", 
        help="Base directory for your daily notes "
        f"(Default: $HOME/{NOTES_DIRECTORY_NAME})",
        default=DEFAULT_NOTES_BASE_DIRECTORY,
        nargs="?"
    )

    args = parser.parse_args()
    
    if not path.isdir(args.notes_base_directory):
        print(
            "ERROR: Please use a valid base path for your notes",
            file=sys.stderr
        )
        print()
        parser.print_help()
        sys.exit(1)

    main(args.notes_base_directory)
