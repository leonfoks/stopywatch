from stopywatch import Stopwatch


print('Instantiate and start')


import time
clk = Stopwatch(timer=time.time)

# For MPI enabled code, simply switch out the instantiation of the Stopwatch.
# from mpi4py import MPI
# clk = Stopwatch(timer=MPI.Wtime)

time.sleep(2)
print('time from the timer: ', clk.time())

time.sleep(2)
print(clk.elapsed())

time.sleep(2)
print(clk.lap())

time.sleep(2)
print(clk.lap())

time.sleep(1)
print(clk.lap())

print(clk.elapsed())

print('Stop the clock')
clk.stop()

print(clk.elapsed())
print(clk.elapsed())

clk.start()

time.sleep(1)
print(clk.elapsed())
