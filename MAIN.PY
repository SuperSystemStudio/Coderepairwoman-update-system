import socket
import threading
import os
import English,chinese
print('Can you tell me')
print('where are from')
print('1.china')
print('2.USA/us')
choose = int(input())
if choose == 1:
    hi = chinese.hi
print(hi)