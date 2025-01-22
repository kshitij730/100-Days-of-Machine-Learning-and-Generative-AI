# Create a Python module with reusable functions and demonstrate file reading/writing.
# utils.py

def write_to_file(filename, data):
    """
    Write data to a file.

    Args:
        filename (str): The name of the file to write to.
        data (str): The content to write into the file.
    """
    with open(filename, 'w') as file:
        file.write(data)
    print(f"Data written to {filename}.")

def read_from_file(filename):
    """
    Read data from a file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        str: The content of the file.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(f"Data read from {filename}:")
        return content
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None

def append_to_file(filename, data):
    """
    Append data to a file.

    Args:
        filename (str): The name of the file to append to.
        data (str): The content to append.
    """
    with open(filename, 'a') as file:
        file.write(data)
    print(f"Data appended to {filename}.")

# Demonstration
if __name__ == "__main__":
    file_name = "example.txt"
    
    # Writing to the file
    write_to_file(file_name, "This is the first line.\n")
    
    # Appending to the file
    append_to_file(file_name, "This is the second line.\n")
    
    # Reading from the file
    content = read_from_file(file_name)
    if content:
        print(content)
