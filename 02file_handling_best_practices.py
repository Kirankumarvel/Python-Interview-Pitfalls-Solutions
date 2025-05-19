# 2. File Handling
# file_handling_best_practices.py

with open('sample.txt', 'w') as file:
    file.write('Hello, World!')

with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)
