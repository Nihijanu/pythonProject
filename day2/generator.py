import time
l=iter(i for i in range(100))
start=time.time()
for i in l:
    print(i)
end_time=time.time()
print((end_time-start)*10**3)