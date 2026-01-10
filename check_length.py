#!/usr/bin/env python3
import sys
import os

def count_chinese_chars(filepath):
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        return 0

    count = 0
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        for char in content:
            if '\u4e00' <= char <= '\u9fff':
                count += 1
    return count

def process_file(filepath):
    count = count_chinese_chars(filepath)
    print(f"File: {os.path.basename(filepath)}")
    print(f"Chinese Character Count: {count}")
    
    if count < 2300:
        print("WARNING: Word count is below 2300!")
    elif count > 2700:
        print("WARNING: Word count is significantly above 2500!")
    else:
        print("SUCCESS: Word count is within acceptable range (2300-2700).")
    print("-" * 30)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 check_length.py <filename_or_directory>")
        sys.exit(1)
    
    path = sys.argv[1]
    
    
    if os.path.isdir(path):
        # Walk through directory and process all .txt files
        files_found = False
        total_count = 0
        file_list = []
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(".txt"):
                    file_list.append(os.path.join(root, file))
        
        # Sort files
        file_list.sort()
        
        for file_path in file_list:
            files_found = True
            count = count_chinese_chars(file_path) # Utilize the function but we need to refactor logic slightly if we want to print details inside process_file
            # To keep it simple, I'll just call process_file which prints individual counts, and I'll re-calculate or return the count.
            # It's better to modify process_file to return the count.
            
            # Since process_file prints, let's just use it and rely on it.
            # Wait, process_file prints but doesn't return anything useful for summation if I interpret the previous code correctly.
            # I will modify process_file to return the count.
            
            # Actually, I can just recalculate here or change process_file signature. 
            # Let's modify process_file in the previous block or just inline it here for the loop.
            # But to be clean, let's modify the whole block.
            
            print(f"File: {os.path.basename(file_path)}")
            current_file_count = 0
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                for char in content:
                    if '\u4e00' <= char <= '\u9fff':
                        current_file_count += 1
            
            print(f"Chinese Character Count: {current_file_count}")
            if current_file_count < 2300:
                print("WARNING: Word count is below 2300!")
            elif current_file_count > 2700:
                print("WARNING: Word count is significantly above 2500!")
            else:
                print("SUCCESS: Word count is within acceptable range (2300-2700).")
            print("-" * 30)
            
            total_count += current_file_count

        if not files_found:
             print(f"No .txt files found in directory: {path}")
        else:
             print(f"\n{'='*30}")
             print(f"Total Chinese Characters in Directory: {total_count}")
             print(f"{'='*30}\n")
             
    else:
        process_file(path)
