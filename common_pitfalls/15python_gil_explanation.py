import threading
import time

counter = 0

def increment():
    global counter
    for _ in range(1000000):
        counter += 1

threads = [threading.Thread(target=increment) for _ in range(2)]
start = time.time()
for t in threads:
    t.start()
for t in threads:
    t.join()
end = time.time()

print(f"Counter value: {counter}")
print(f"Time taken: {end - start:.2f} seconds")

# Despite threading, GIL prevents true parallel increments in CPython
