class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type:
            print(f"Exception: {exc_val}")
        return True  # Suppress exceptions

with ManagedFile('test.txt') as f:
    f.write('Hello, context manager!')

# File automatically closed after block
