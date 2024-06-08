array = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(array):
    element = array[i]
    i += 1
    if element < 0:
        break
    elif element == 0:
        continue
    print(element)


# print(*[elem for elem in array[:(array + [-1]).index(([i for i in array + [-1] if i < 0])[0])] if elem != 0], sep='\n')
