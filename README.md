# EXEcutor

EXEcutor helps you manage executable files in your repository. It identifies `.exe` files, moves them to a temporary folder, and deletes them with your confirmation.

## Usage

The EXEcutor script (`EXEcutor.py`) and the `generate_exe_files.py` script work together to showcase the functionality. The generate_exe_files.py script generates a sample directory structure with .exe files, and the EXEcutor.py script manages these files based on user input.

## Demonstration Video

<video controls>
  <source src="./Demo_Video.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Steps

1. **Generate Sample Directory Structure**

   Run `generate_exe_files.py` to create a sample directory structure with .exe files. This step is necessary before running the EXEcutor.py script.

   ```bash
   python generate_exe_files.py
   ```

   Sample exe files will be generated in the "SampleDirectory" folder.

2. **Run EXEcutor Script**

   Run `EXEcutor.py` to manage the .exe files generated in the previous step.

   ```bash
   python EXEcutor.py
   ```

   The script will:

   - List the found .exe files.
   - Move .exe files to a temporary folder.
   - Optionally delete the .exe files with your confirmation.

   During the process, you will see progress animations and emojis indicating the actions taken.
