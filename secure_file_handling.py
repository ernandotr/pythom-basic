import os

def secure_file_delection(file_path):
    """
    Securely delete a file by overwriting it with random data before deletion.
    
    Args:
        file_path (str): The path to the file to be securely deleted.
    """
    with open(file_path, 'w') as file:
        file.write(os.urandom(1024)) # Overwrite with random data
    
    # Now delete the file
    os.remove(file_path)
    print(f"File {file_path} securely deleted.")

# Example usage
file_path = "example.txt"  # Replace with your file path
secure_file_delection(file_path)
