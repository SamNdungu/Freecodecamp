func_1 = lambda a : a * a
func_2 = lambda a, b : a + b

square = func_1(20)
sum_ = func_2(10, 10)

print(square)
print(sum_)


# Further lambda functions - filter(), map(), and reduce()

from functools import reduce

nums = [3, 2, 6, 6, 4, 6, 2, 9]

even_nums = list(filter(lambda n : n % 2 == 0, nums))
print(even_nums)

double_nums = list(map(lambda n : n * 2, even_nums))
print(double_nums)

sum_nums = reduce(lambda a, b : a + b, double_nums) 
print(sum_nums)