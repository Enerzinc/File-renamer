from pathlib import Path

class FileRenamer:
    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)
        self.files_in_folder = [p for p in self.folder_path.iterdir() if p.is_file()]
    def validate_folder(self):
        if not self.folder_path.exists():
            print("The specified folder does not exist.")
            return False
        if not self.folder_path.is_dir():
            print("The specified path is not a folder.")
            return False
        return True

    def remove_dashes(self):
      if not self.validate_folder():
        return
      for file in self.files_in_folder:
        if file.is_file():
          new_name = file.name.replace("-", "")
          if new_name == file.name:
            continue
          new_path = file.with_name(new_name)
          file.rename(new_path)
      print("\n Process Completed")

if __name__ == "__main__":
  folder = input("Enter the folder path: ")
  renamer = FileRenamer(folder)
  renamer.remove_dashes()