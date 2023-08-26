import os
import shutil
import time


def move_exe_files(folder_path):
    temp_folder = "exe files bin"
    if not os.path.exists(temp_folder):
        os.mkdir(temp_folder)

    exe_files = []

    for root, _, files in os.walk(folder_path):
        exe_files.extend([os.path.join(root, file)
                         for file in files if file.endswith(".exe")])

    if not exe_files:
        print("No .exe files found in the repository.")
        return

    print("Found the following .exe files:")
    for exe_file in exe_files:
        print(f"📁 {exe_file}")

    # Progress animation
    print("\nMoving .exe files to temp folder ", end="")
    for _ in range(5):  # Simulate progress with animation
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()

    for exe_file in exe_files:
        target_path = os.path.join(temp_folder, os.path.basename(exe_file))
        shutil.move(exe_file, target_path)

    confirmation = input("Do you want to delete the .exe files? (yes/no): ")
    if confirmation.lower() == "yes":
        print("Deleting files... ", end="")
        for _ in range(3):  # Simulate progress with animation
            print("🗑️", end="", flush=True)
            time.sleep(0.8)
        print()

        deleted_count = 0
        for exe_file in os.listdir(temp_folder):
            os.remove(os.path.join(temp_folder, exe_file))
            deleted_count += 1
        print(f"✅ {deleted_count} files deleted.")
    else:
        print("Files not deleted.")


if __name__ == "__main__":
    current_directory = os.getcwd()
    move_exe_files(current_directory)
