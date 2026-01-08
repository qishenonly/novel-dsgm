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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 check_length.py <filename>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    count = count_chinese_chars(filepath)
    print(f"File: {os.path.basename(filepath)}")
    print(f"Chinese Character Count: {count}")
    
    if count < 2300:
        print("WARNING: Word count is below 2300!")
    elif count > 2700:
        print("WARNING: Word count is significantly above 2500!")
    else:
        print("SUCCESS: Word count is within acceptable range (2300-2700).")
