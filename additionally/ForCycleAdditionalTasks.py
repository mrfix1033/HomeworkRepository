# 1
print(*['*' * (i + 1) for i in range(int(input()))], sep='\n')

# 2
a, b, c, d = [int(input()) for i in range(4)]  # 7, 10, 5, 6
print(*['\t'.join(f"{'' if x * y == 1 else x * y}"for x in [1, *range(c, d + 1)]) for y in [1, *range(a, b + 1)]], sep='\n')

# 3
print(*['\t'.join(str(o + (i - 1) * i // 2) for o in range(1, i + 1)) for i in range(1, int(input()) + 1)], sep='\n')
