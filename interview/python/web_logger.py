from collections import deque
import time

class WebLogger(object):

    SECONDS_IN_FIVE = 300

    __init__(self):
        self.log = deque()

    def log_hit(self):
        prune()
        self.log.append(time.time())

    def last_five(self):
        prune()
        return len(self.log)

    def prune(self):
        last_five_mins = time.time() - SECONDS_IN_FIVE
        while len(self.log) > 0 and self.log[0] < last_five_mins:
            deque.popleft()


if __name__ == "__main__":
    logger = WebLogger()
