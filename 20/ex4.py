from datetime import datetime

time = datetime.now()

my_own_time = time.strftime("%m:%d:%Y")
print(my_own_time)

my_own_time = time.strftime("%I")
