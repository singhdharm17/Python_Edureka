# 6. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000
# and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
lst = [i for i in range(2000, 3000) if i % 7 == 0 if i % 5 != 0]
print(lst)
