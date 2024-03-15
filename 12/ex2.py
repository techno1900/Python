# try:
#     note = open('note.txt')
#     age = int(input('enter your age : '))
#     x = 10/age
#     note.close()
# except (ValueError, ZeroDivisionError):
#     print('file error')
# else:
#     print('no exeptions')

try:
    note = open('note.txt')
    age = int(input('enter your age : '))
    x = 10/age
except (ValueError, ZeroDivisionError):
    print('please enter valide commadns')

else:
    print('no errors')

finally:
    note.close()