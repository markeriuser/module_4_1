from fake_math import divide as fake_res
from true_math import divide as true_res

result1 = fake_res(69, 3)
result2 = fake_res(3, 0)
result3 = true_res(49, 7)
result4 = true_res(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)