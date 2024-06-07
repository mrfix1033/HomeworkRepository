my_dict = {"Андрей": 2000, "Алексей": 2001, "Агасий": 2002}
print(my_dict)
print(my_dict.get("Андрей"))
my_dict.update({"names[3]": 2003, "names[4]":2004})
print(my_dict.pop("Андрей"))
print(my_dict)

my_set = {1, 2, 3, 1, 2, "Строка", "Еще", "Строка", "И", "Еще", None, None}
print(my_set)
my_set.update([4, "строка"])
my_set.discard(1)
print(my_set)
