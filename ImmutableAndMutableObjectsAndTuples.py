immutable_var = ("", 0, 0., True, None, str, print, (), {}, [], set(), range(0), (-1) ** 0.5, (i for i in ()), Exception())
print(immutable_var)


immutable_var[9].append(immutable_var)
# immutable_var[0] = "НЕЛЬЗЯ!!!"
print(immutable_var)

mutable_var = ['список', 'из', 'нескольких', 'элементов']
print(mutable_var)
