first = int(input())
second = int(input())
third = int(input())
if first == second and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)


# print([3, 2, 0][len(set(int(input()) for i in range(3))) - 1])
