import os

def read_and_modify_file(input_filename, output_filename):
    """
    Reads content from 'input_filename', modifies it, and writes to 'output_filename'.
    Handles errors gracefully and provides feedback to the user.
    """
    try:
        # Check if the input file exists
        if not os.path.exists(input_filename):
            print(f"Error: The file '{input_filename}' does not exist.")
            return

        # Open and read the content of the input file
        with open(input_filename, 'r') as file:
            content = file.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to the output file
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"Success: The content has been modified and saved to '{output_filename}'.")

    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_filename}' or '{output_filename}'.")
    except IOError as e:
        print(f"Error: An I/O error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
input_file = 'example.txt'
output_file = 'modified_example.txt'
read_and_modify_file(input_file, output_file)
