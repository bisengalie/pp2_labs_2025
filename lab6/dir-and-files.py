import os
import shutil
import string

def list_contents(path):
    """List directories, files, and all contents in the specified path."""
    if not os.path.exists(path):
        print(f"The specified path '{path}' does not exist.")
        return

    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    print("Directories:", directories)
    print("Files:", files)
    print("All contents:", directories + files)

def check_access(path):
    """Check existence, readability, writability, and executability of the specified path."""
    print(f"Checking access for: {path}")
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

def path_info(path):
    """Check if a path exists and, if so, display its directory and filename components."""
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        print("Directory part:", os.path.dirname(path))
        print("Filename part:", os.path.basename(path))
    else:
        print(f"The path '{path}' does not exist.")

def count_lines(filename):
    """Count the number of lines in a text file."""
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for _ in file)
        print(f"Number of lines in '{filename}':", line_count)
        return line_count
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return 0

def write_list_to_file(filename, data_list):
    """Write a list of items to a file, each on a new line."""
    with open(filename, 'w') as file:
        for item in data_list:
            file.write(str(item) + "\n")
    print(f"List written to '{filename}'.")

def generate_text_files():
    """Generate 26 text files named A.txt to Z.txt."""
    for letter in string.ascii_uppercase:
        filename = f"{letter}.txt"
        with open(filename, 'w') as file:
            file.write(f"This is file {filename}")
        print(f"Created file '{filename}'.")

def copy_file(source, destination):
    """Copy contents from source file to destination file."""
    try:
        shutil.copy(source, destination)
        print(f"Copied content from '{source}' to '{destination}'.")
    except FileNotFoundError:
        print(f"Source file '{source}' not found.")
    except PermissionError:
        print(f"Permission denied while copying '{source}' to '{destination}'.")

def delete_file(path):
    """Delete a file if it exists and is writable."""
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"File '{path}' deleted successfully.")
        else:
            print(f"No permission to delete the file '{path}'.")
    else:
        print(f"File '{path}' does not exist.")
name=str("__main__")
# Example usage:
if name == "__main__":
    # 1. List contents
    test_directory = "test_directory"
    os.makedirs(test_directory, exist_ok=True)
    list_contents(test_directory)

    # 2. Check access
    check_access(test_directory)

    # 3. Path information
    path_info(test_directory)

    # 4. Count lines in a file
    test_file = os.path.join(test_directory, "test_file.txt")
    with open(test_file, 'w') as f:
        f.write("Line 1\nLine 2\nLine 3\n")
    count_lines(test_file)

    # 5. Write a list to a file
    sample_list = ["Apple", "Banana", "Cherry"]
    output_file = os.path.join(test_directory, "output.txt")
    write_list_to_file(output_file, sample_list)

    # 6. Generate text files A.txt to Z.txt
    generate_text_files()

    # 7. Copy file contents
    source_file = test_file
    destination_file = os.path.join(test_directory, "copied_file.txt")
    copy_file(source_file, destination_file)

    # 8. Delete a file
    file_to_delete = destination_file
    delete_file(file_to_delete)