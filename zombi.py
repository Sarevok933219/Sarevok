#!/usr/bin/env python3

import os
import sys
import time


try:
    pid = os.fork()
except Exception as e:
    print('Fork failed')
    sys.exit(1)

if pid == 0:
    # child process
    print('Hello from zombie child ' + str(os.getpid()))
    sys.exit(0)

# parent process
time.sleep(0.1)

print('Press enter to wait()')
input()
os.waitpid(pid, 0)  # The child is a zombie until we execute this line

print('Zombie child reaped')

print('Press enter to exit')
input()
