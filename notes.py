
### notes.py
```python
import sys

NOTES_FILE = 'notes.txt'

def read_notes():
    try:
        with open(NOTES_FILE, 'r') as file:
            notes = file.readlines()
        return [note.strip() for note in notes]
    except FileNotFoundError:
        return []

def write_notes(notes):
    with open(NOTES_FILE, 'w') as file:
        for note in notes:
            file.write(note + '\n')

def add_note():
    note = input("Enter your note: ")
    notes = read_notes()
    notes.append(note)
    write_notes(notes)
    print("Note added.")

def view_notes():
    notes = read_notes()
    if notes:
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note}")
    else:
        print("No notes found.")

def delete_note():
    try:
        note_index = int(input("Enter the note number to delete: ")) - 1
        notes = read_notes()
        if 0 <= note_index < len(notes):
            deleted_note = notes.pop(note_index)
            write_notes(notes)
            print(f"Deleted note: {deleted_note}")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python notes.py [add|view|delete]")
        return

    command = sys.argv[1]

    if command == 'add':
        add_note()
    elif command == 'view':
        view_notes()
    elif command == 'delete':
        delete_note()
    else:
        print("Unknown command. Use 'add', 'view', or 'delete'.")

if __name__ == "__main__":
    main()
