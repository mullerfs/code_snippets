for i in range(1, 11):  # A sequence from 1 to 10
    if i % 2 == 0:
        print(i, " is even")
    else:
        print(i, " is odd")

print("com step")
for i in range(1, 20,3):  # A sequence from 1 to 10
    if i % 2 == 0:
        print(i, " is even")
    else:
        print(i, " is odd")


print("deteção em nested loop")
n = 50
num_list = [10, 4, 23, 6, 18, 27, 47]
found = False  # This bool will become true once a pair is found

for n1 in num_list:
    for n2 in num_list:
        if(n1 + n2 == n):
            found = True  # Set found to True
            break  # Break inner loop if a pair is found
    if found:
        print(n1, n2) # Print the pair
        break  # Break outer loop if a pair is found


print("usando o pass para implementar depois")
num_list = list(range(20))

for num in num_list:
    pass # You can write code here later on

print(len(num_list)) 


print("brackets")
brackets="[[[[][]]]][]"

def check_balance(brackets):  # The argument is a string
    balanceado=0
    for i in brackets:
        if i == '[':
            balanceado+=1
        elif i == ']':
            balanceado-=1
        
        if balanceado <0:
            return False
        
    return True
        

print(check_balance(brackets))