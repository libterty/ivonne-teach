import threading
import queue
import memoryHandler as mh

q = queue.Queue(maxsize=10)

# def worker():
#     while True:
#         item = q.get()
#         print('Working on' + item)
#         print('Finished' + item)
#         q.task_done()


# turn-on the worker thread
# threading.Thread(target=worker, daemon=True).start()

@mh.track
def looping():
    for i in range(100):
        if q.qsize() >= 10:
            break
        else:
            q.put(i)

    while not q.empty():
        n = q.get()
        print("Take out Data:" + str(n))

looping()
