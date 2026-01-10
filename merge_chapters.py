import os

def merge_chapters():
    output_filename = "1-11章汇总.txt"
    directory = "."  # Current directory
    
    with open(output_filename, 'w', encoding='utf-8') as outfile:
        for i in range(1, 12):
            # Format filename as 第001章.txt, 第011章.txt usually 3 digits padding based on the list I saw
            # The list showed 第001章.txt to 第011章.txt.
            chapter_filename = f"第{i:03d}章.txt"
            file_path = os.path.join(directory, chapter_filename)
            
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        outfile.write(content)
                        outfile.write("\n\n") # Add some spacing between chapters
                        print(f"Merged {chapter_filename}")
                except Exception as e:
                    print(f"Error reading {chapter_filename}: {e}")
            else:
                print(f"File not found: {chapter_filename}")

if __name__ == "__main__":
    merge_chapters()
