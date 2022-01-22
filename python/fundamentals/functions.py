print("Immutable variables")

num = 20
def multiply_by_10(n):
    n *= 10
    num = n  # Changing the value inside the function
    print("Value of num inside function:", num)
    return num

return_num = multiply_by_10(num)
print("value return from function:",return_num)
print("Value of num outside function:", num)  # The original value remains unchanged


print("Mutable variables")
num_list = [10, 20, 30, 40]
print(num_list)

def multiply_by_10_list(my_list):
    my_list[0] *= 10
    my_list[1] *= 10
    my_list[2] *= 10
    my_list[3] *= 10

multiply_by_10_list(num_list)
print(num_list)  # The contents of the list have been changed

print("lambdas")
# formato -> lambda parameter: expression
triple = lambda num : num * 3  # Assigning the lambda to a variable
print(triple(10))  # Calling the lambda and giving it a parameter

concat_strings = lambda a, b, c: a[0] + b[0] + c[0]
print(concat_strings("World", "Wide", "Web"))

my_func = lambda num: "High" if num > 50 else "Low"
print(my_func(60))