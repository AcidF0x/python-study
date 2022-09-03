from datetime import datetime
import threading
from multiprocessing import Process

def work():
    result = 0
    for i in range(1, 100):
        for b in range(i, i * 10000):
           result += i+b

if __name__ == "__main__": # window에서 사용안하면 에러남
    print(f"start all work")

    now = datetime.now()
    result = 0
    for i in range(1, 10):
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
    print(f"processing time = {datetime.now() - now}") ## 전혀 안빠르다 GIL로 검색 ㄱㄱ

    print("using multiprocess")
    processes = []

    print(f"start all work")
    now = datetime.now()
    for i in range(0, 10):
        t = Process(None, work)
        t.start()
        processes.append(t)

    for process in processes:
        process.join()

    print(f"end all work")
    print(f"processing time = {datetime.now() - now}") # 짱빠르다