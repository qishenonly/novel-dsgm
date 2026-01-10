import os
import argparse
import re

def numerical_sort(value):
    """
    Extracts the number from the filename for sorting.
    Assumes format like '第001章.txt' or similar.
    """
    numbers = re.findall(r'\d+', value)
    return int(numbers[0]) if numbers else 0

def merge_chapters(directory, output_filename):
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' not found.")
        return

    txt_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                 txt_files.append(os.path.join(root, file))
    
    # Sort files numerically based on the chapter number in filename
    try:
        txt_files.sort(key=lambda x: numerical_sort(os.path.basename(x)))
    except Exception as e:
        print(f"Warning: Could not sort numerically, falling back to alphabetical. Error: {e}")
        txt_files.sort()

    
    if not txt_files:
        print(f"No .txt files found in '{directory}'.")
        return

    # Determine start and end chapters for default filename
    start_chapter = numerical_sort(os.path.basename(txt_files[0]))
    end_chapter = numerical_sort(os.path.basename(txt_files[-1]))
    
    if output_filename is None:
        output_filename = f"独守国门：我把诡异禁区上交国家_{start_chapter:02d}_{end_chapter:02d}.txt"

    try:
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            for file_path in txt_files:
                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        # Write filename as a header for clarity
                        outfile.write(f"\n\n{'='*20}\n{os.path.basename(file_path)}\n{'='*20}\n\n")
                        outfile.write(content)
                        print(f"Merged {os.path.basename(file_path)}")
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
        print(f"\nSuccessfully merged {len(txt_files)} chapters into '{output_filename}'.")
    except Exception as e:
        print(f"Error writing to output file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge all .txt files in a directory into one file.")
    parser.add_argument("directory", help="The directory containing chapter files.")
    parser.add_argument("--output", help="The output filename. If not provided, defaults to '独守国门：我把诡异禁区上交国家_start_end.txt'.")
    
    args = parser.parse_args()
    
    merge_chapters(args.directory, args.output)
