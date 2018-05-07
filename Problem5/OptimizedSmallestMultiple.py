import time

start = time.time()

result = 0
done = False

while not done:
    result += 20
    for x in [20, 19, 18, 17, 16, 15, 14, 13, 11]:
        if result % x != 0:
            break
    else:
       done = True

end = time.time()

print('result:', result)
print('time in seconds:', end-start)