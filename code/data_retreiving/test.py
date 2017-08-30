from multiprocessing.pool import ThreadPool
import time
import threading
from tqdm import tqdm


def demo(lock, position, total):
    text = "progresser #{}".format(position)
    with lock:
        progress = tqdm(
            total=total,
            position=position,
            desc=text,
        )
    for _ in range(0, total, 5):
        with lock:
            progress.update(5)
        time.sleep(0.1)
    with lock:
        progress.close()


pool = ThreadPool(5)
tasks = range(50)
lock = threading.Lock()
for i, url in enumerate(tasks, 1):
    pool.apply_async(demo, args=(lock, i, 100))
pool.close()
pool.join()
