def get_matrix(height, width, value):
    return [[value for i in range(width)] for i in range(height)]


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
