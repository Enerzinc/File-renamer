from pathlib import Path

class FileRenamer:
    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)
        
    def validate_folder(self):
        if not self.folder_path.exists():
            print("The specified folder does not exist.")
            return False
        if not self.folder_path.is_dir():
            print("The specified path is not a folder.")
            return False
        return True

    def replace_character(self):
        if not self.validate_folder():
            return

        old_char = input("Enter the character/symbol to replace: ")
        new_char = input("Enter the new character/symbol to use: ")

        self.files_in_folder = [p for p in self.folder_path.iterdir() if p.is_file()]
        for file in self.files_in_folder:
            if old_char in file.name:

                new_name = file.name.replace(old_char, new_char)

                if new_name == file.name:
                    continue 

                new_path = file.with_name(new_name)

                try:
                    file.rename(new_path)
                except Exception as error:
                    print(f"Error renaming {file.name}: {error}")
            else:
                print(f"No '{old_char}' found in {file.name}, skipping.")
        print("\n Process Completed")

while True:
    path = input("\nEnter folder path (type 'exit' to stop): ")
    if path == "exit":
        print("Program ended.")
        break
    renamer = FileRenamer(path)
    renamer.replace_character()
