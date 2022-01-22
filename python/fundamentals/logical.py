"""
Operator 	Purpose 	Notation
> 	Greater Than 	In-fix
< 	Less Than 	In-fix
>= 	Greater Than or Equal To 	In-fix
<= 	Less Than or Equal To 	In-fix
== 	Equal To 	In-fix
!= 	Not Equal To 	In-fix
is 	Equal To (Identity) 	In-fix
is not 	Not Equal To (Identity) 	In-fix
"""

print(10 * True)
print(10 * False)


num = 60

output = "The number is less than or equal to 50" \
    if num <= 50 else "The number is greater than 50"

print(output)