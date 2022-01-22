"""
The comprehension consists of three main parts:
[_expression_ _for loop_ _if condition_]

    The expression is an operation used to create elements in the new list.

    The for loop will iterate an existing list. The iterator will be used in the expression.

    New elements will only be added to the new list when the if condition is fulfilled. This component is optional.
"""


#list comprehension

#sem compreensão
nums = [10, 20, 30, 40, 50]
nums_double = []

for n in nums:
    nums_double.append(n * 2)

print(nums)
print(nums_double)

#com compreensão
nums = [10, 20, 30, 40, 50]

# List comprehension
nums_double = [n * 2 for n in nums]

print(nums)
print(nums_double)


# List comprehension
nums_double = [n * 2 for n in nums if n % 4 == 0]

print(nums)
print(nums_double)


list1 = [30, 50, 110, 40, 15, 75]
list2 = [10, 60, 20, 50]

sum_list = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]

print(sum_list)

