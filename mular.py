import time
import threading
import sys

print('procession file`s name: ')
ReadA = "a.dat"
ReadB = "b.dat"

AA = []
BB = []
SingleThread=[]
multi_Thread_one=[]
multi_Thread_two=[]
multi_Thread_third=[]
multi_Thread_fourth=[]

with open(ReadA) as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        AA.append(list(map(int, line.split())))

with open(ReadB) as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        BB.append(list(map(int, line.split())))

def mulab(start, end, result):
    for i in range(start, end):
        result.append(list())
        for j in range(1000):
            result[-1].append(AA[i][j]*BB[i][j])
    return


def single_process():
    single_start = time.perf_counter()
    single = threading.Thread(target = mulab, args=(0, 1000, SingleThread))
    single.start()
    single.join()
    
    return float(time.perf_counter() - single_start)

def multi_process():
    multi_start = time.perf_counter()
    First_core = threading.Thread(target = mulab, args=(0, 250, multi_Thread_one))
    Second_core = threading.Thread(target = mulab, args=(250, 500, multi_Thread_two))
    Third_core = threading.Thread(target = mulab, args=(500, 750, multi_Thread_third))
    Fourth_core = threading.Thread(target = mulab, args=(750, 1000, multi_Thread_fourth))
    First_core.start()
    Second_core.start()
    Third_core.start()
    Fourth_core.start()
    First_core.join()
    Second_core.join()
    Third_core.join()
    Fourth_core.join()
    return float(time.perf_counter() - multi_start)

single_process()
multi_process()

print('All Thread`s sum: ')
print ('First_Thread_result')
print(multi_Thread_one)
print ('Second_Thread_result')
print(multi_Thread_two)
print('Third_Thread_result')
print(multi_Thread_third)
print('Fourth_Thread_result')
print(multi_Thread_fourth)

with open('C.dat', 'w') as file:
    ceil = 250
    for i in range(ceil):
        for c in multi_Thread_one[i]:
            file.write(str(c) + ' ')
        file.write('\n')
    for i in range(ceil):
        for c in multi_Thread_two[i]:
            file.write(str(c) + ' ')
        file.write('\n')
    for i in range(ceil):
        for c in multi_Thread_third[i]:
            file.write(str(c) + ' ')
        file.write('\n')
    for i in range(ceil):
        for c in multi_Thread_fourth[i]:
            file.write(str(c) + ' ')
        file.write('\n')

with open('C.dat') as file:
    print(file.read())

print ("single_Thread running time: ", (single_process())) 
print ("multi_Thread running time: ", (multi_process()))  