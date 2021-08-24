import threading
import time

def thread1():
    for i in range(10):
        print(f"This is thread1: {i}")
        time.sleep(1)

def thread2():
    time.sleep(3)
    print("  This is thread2")

thread_one = threading.Thread(target=thread1)
thread_two = threading.Thread(target=thread2)

thread_one.start()
thread_two.start()
# join()がないとそれぞれの処理を始めた直後に"finish!!"が表示される。
thread_one.join()
thread_two.join()

print("finish!!")