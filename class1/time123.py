import time
initial =time.time()
print(initial)
for i in range (45) :
    print(i+1)
    time.sleep(0.3)
print(time.time() - initial)
second = time.time()
k = 0
while k< 45 :
    print(k+1)
    k+=1
print(time.time() - second)

# mytime = time.asctime(time.localtime(time.time()))
# print(mytime)