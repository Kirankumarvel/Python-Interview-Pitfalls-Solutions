import threading
import multiprocessing
import time

def worker():
    print(f"Worker {threading.current_thread().name} started")
    time.sleep(1)
    print(f"Worker {threading.current_thread().name} finished")

print("Using threading:")
threads = [threading.Thread(target=worker, name=f'Thread-{i}') for i in range(3)]
for t in threads: t.start()
for t in threads: t.join()

print("\nUsing multiprocessing:")
processes = [multiprocessing.Process(target=worker, name=f'Process-{i}') for i in range(3)]
for p in processes: p.start()
for p in processes: p.join()
