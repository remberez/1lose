import os

def count_lines_in_project(root_dir, extensions=('.py',)):
    total_lines = 0
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(extensions):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    total_lines += sum(1 for _ in f)
    return total_lines

print("Total lines:", count_lines_in_project("./backend"))
