from collections import deque
import time

class WebLogger(object):

    SECONDS_IN_FIVE = 300

    __init__(self):
        self.log = deque()

    def log():
        prune()
        self.log.append(time.time())

    def last_five():
        prune()
        return len(self.log)

    def prune():
        last_five_mins = time.time() - SECONDS_IN_FIVE
        while self.log[0] < last_five_mins:
            deque.popleft()


if __name__ == "__main__":
    logger = WebLogger()
    
