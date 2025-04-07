def read_and_write_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as infile:
            content = infile.read()  # Read the entire content of the file

        # Modify the content (as an example, converting to uppercase)
        modified_content = content.upper()

        # Open the output file in write mode
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)  # Write the modified content to the new file

        print(f"File {input_filename} has been read and the modified content has been written to {output_filename}.")
    
    except FileNotFoundError:
        print(f"The file {input_filename} was not found.")
    except IOError:
        print(f"An error occurred while handling the file.")

# Example usage (call the function with the appropriate file names)
read_and_write_file('input.txt', 'output.txt')


def handle_file_error():
    filename = input("Please enter the filename you want to open: ")

    try:
        # Try to open the file
        with open(filename, 'r') as file:
            content = file.read()  # Read the file content
            print("File content:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    
    except IOError:
        print(f"Error: The file {filename} cannot be read. It might be in use or protected.")

# Call the function to test it
handle_file_error()
