import time
import threading

def daemon_task(*args):
    while True:
        print(args[0])
        time.sleep(1)

t1 = threading.Thread(target=daemon_task, daemon=True, args=['This is daemon'])
t1.start()

for i in range(10):
    print('\tThis is main - ', i)
    time.sleep(1)
