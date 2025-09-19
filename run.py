import os
import shutil
from pathlib import Path

def get_arduino_libraries_path():
    """
    Detect the default Arduino libraries path depending on OS.
    """
    if os.name == "nt":  # Windows
        return Path(os.path.expanduser("~/Documents/Arduino/libraries"))
    else:  # Linux/macOS
        return Path(os.path.expanduser("~/Arduino/libraries"))

def install_library(folder_name):
    """
    Copies the hardcoded folder (same level as this script) into Arduino libraries.
    """

    script_dir = Path(__file__).parent.resolve()
    src_path = script_dir / folder_name

    if not src_path.is_dir():
        print(f" Error: {src_path} does not exist or is not a folder.")
        return

    arduino_libs = get_arduino_libraries_path()
    arduino_libs.mkdir(parents=True, exist_ok=True)

    dest_path = arduino_libs / folder_name

    if dest_path.exists():
        print(f" Library '{folder_name}' already exists. Removing old version...")
        shutil.rmtree(dest_path)

    print(f" Installing '{folder_name}' to {arduino_libs}")
    shutil.copytree(src_path, dest_path)
    print(" Installation complete!")

if __name__ == "__main__":
    install_library("MyCobotBasic")
    install_library("avr-libstdcpp")
