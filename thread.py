import threading
from datetime import datetime
from time import sleep

def work():
    sleep(1)
now = datetime.now()

print(f"start all work")
for i in range(0, 10):
    work()
print(f"end all work")
print(f"processing time = {datetime.now() - now}")

print("using thread......")
threads = []

print(f"start all work")
now = datetime.now()
for i in range(0, 10):
    t = threading.Thread(None, work)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


print(f"end all work")
print(f"processing time = {datetime.now() - now}")