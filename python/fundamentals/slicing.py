my_string = "This is MY string!"
print(my_string[0:4]) # From the start till before the 4th index
print(my_string[1:7])
print(my_string[8:len(my_string)]) # From the 8th index till the end

print(my_string[8:-2])

#slicing with step
my_string = "This is MY string!"
print(my_string)
print(my_string[0:7])  # A step of 1
print(my_string[0:7:2])  # A step of 2
print(my_string[0:7:5])  # A step of 5

#reverse slicing with step
print(my_string[len(my_string)::-1]) 
print(my_string[::-1])  # The whole string in reverse (step is -1)

print(my_string[17:0:-2]) # Take 2 steps back. The opposite of what happens in the slide above

print(my_string[:8])  # All the characters before 'M'
print(my_string[8:])  # All the characters starting from 'M'
print(my_string[-7:])  # ultimos 7 campos
print(my_string[-10::2])  # ultimos 10 campos apenas pares
