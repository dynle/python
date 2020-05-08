n = int(input())
add = 6
first = 1
room = 1
if n == 1:
    print(1)
else:
    while True:
        first = first + add
        room +=1
        if n <= first:
            print(room)
            break
        add +=6 #등차가 6일 때 밑에 넣어준다.
