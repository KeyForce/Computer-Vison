from multiprocessing import Process
import os

# 子进程要执行的代码


def run_proc(name):
    print("Hello World")


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc)
    p.start()
    p.join()
