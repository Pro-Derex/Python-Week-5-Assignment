def create_file(filename):
    """Create a file and write initial content."""
    try:
        with open(filename, 'w') as file:
            file.write("This is the first line.\n")
            file.write("This is the second line with a number: 12345\n")
            file.write("This is the third line.\n")
        print(f"{filename} created and initial content written.")
    except (PermissionError, IOError) as e:
        print(f"Error creating/writing to the file: {e}")
    finally:
        print("Create file operation completed.")

def read_file(filename):
    """Read and display the contents of the file."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nContents of the file:")
            print(content)
    except FileNotFoundError:
        print(f"{filename} not found.")
    except (PermissionError, IOError) as e:
        print(f"Error reading the file: {e}")
    finally:
        print("Read file operation completed.")

def append_to_file(filename):
    """Append additional content to the file."""
    try:
        with open(filename, 'a') as file:
            file.write("This is the fourth line.\n")
            file.write("This is the fifth line with a number: 67890\n")
            file.write("This is the sixth line.\n")
        print("Additional content appended to the file.")
    except (PermissionError, IOError) as e:
        print(f"Error appending to the file: {e}")
    finally:
        print("Append file operation completed.")

if __name__ == "__main__":
    filename = "my_file.txt"
    
    create_file(filename)  # Step 1: Create the file and write initial content
    read_file(filename)     # Step 2: Read and display contents
    append_to_file(filename) # Step 3: Append additional content
    read_file(filename)     # Step 4: Read and display updated contents
