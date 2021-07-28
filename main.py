import time
from functools import lru_cache


@lru_cache(maxsize=5)
def fab(n):

        time.sleep(n)
        return n
if __name__ == '__main__':
    print(fab(5))
    print("now it is fab")
    input()
    print(fab(4))
