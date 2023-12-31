import os


def generate_sample_directory_structure(root_dir):

    os.makedirs(root_dir, exist_ok=True)

    folders = ['FolderA', 'FolderB', 'FolderC']
    subfolders = ['Subfolder1', 'Subfolder2', 'Subfolder3']
    files = ['File1.exe', 'File2.exe', 'File3.exe']

    for folder in folders:
        folder_path = os.path.join(root_dir, folder)
        os.makedirs(folder_path, exist_ok=True)

        for subfolder in subfolders:
            subfolder_path = os.path.join(folder_path, subfolder)
            os.makedirs(subfolder_path, exist_ok=True)

        for file in files:
            file_path = os.path.join(folder_path, file)
            with open(file_path, 'w') as f:
                f.write("This is a sample file.")


if __name__ == "__main__":

    sample_root_directory = "SampleDirectory"
    generate_sample_directory_structure(sample_root_directory)
    print("✅ Sample exe files generated.")
