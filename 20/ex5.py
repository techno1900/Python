import time

# print('hellow')

# time.sleep(3)

# print('my name is nimsara')



while True:
    local_time = time.localtime()
    result = time.strftime("%H:%M:%S", local_time)
    print(result)
    time.sleep(1)




