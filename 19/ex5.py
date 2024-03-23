import csv


with open('user.csv', "w", newline="") as userdata:
    user_write_data = csv.writer(userdata)
    user_write_data.writerow(["user_name", "email", "Phone"])

    user_write_data.writerow(['nimsara','bnimsara',12222])
    user_write_data.writerow(['lakisha','lakisha',12333])


with open('user.csv') as userdata:
    user_add_data = csv.reader(userdata)
    print(list(user_add_data))

