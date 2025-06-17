import json
import sys


def txt_to_json(input_filename, output_filename=None):
    # If no output filename is provided, create one based on the input filename
    if output_filename is None:
        output_filename = input_filename.rsplit('.', 1)[0] + '.json'

    # Read lines from the text file
    with open(input_filename, 'r', encoding='utf-8') as file:
        # Read all lines and remove trailing whitespace
        lines = [line.rstrip() for line in file.readlines()]

        # Remove empty lines (optional - comment this line if you want to keep empty lines)
        lines = [line for line in lines if line]

    # Write to JSON file
    with open(output_filename, 'w', encoding='utf-8') as file:
        json.dump(lines, file, indent=3)

    print(f"Successfully converted {input_filename} to {output_filename}")


if __name__ == "__main__":
    # Check if filename was provided as command line argument
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        txt_to_json(input_file, output_file)
    else:
        print("Usage: python script.py input.txt [output.json]")