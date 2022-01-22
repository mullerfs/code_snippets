# construção 
empty_dict = {}  # Empty dictionary
print(empty_dict)

phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

#construção com dict
empty_dict = dict()  # Empty dictionary
print(empty_dict)

phone_book = dict(Batman=468426, Cersei=237734, Ghostbusters=44678)
# Keys will automatically be converted to strings
print(phone_book)

# Alternative approach
phone_book = dict([('Batman', 468426),
                   ('Cersei', 237734),
                   ('Ghostbusters', 44678)])
print(phone_book)



# i# Removing
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

del phone_book["Batman"]
print(phone_book)

#adding
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

phone_book["Godzilla"] = 46394  # New entry
print(phone_book)

phone_book["Godzilla"] = 9000  # Updating entry
print(phone_book)


# copying content of dict

phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}

second_phone_book = {"Catwoman": 67423, "Jaime": 237734, "Godzilla": 37623}

# Add secondphone_book to phone_book
phone_book.update(second_phone_book)
print(phone_book)


#comprehension
houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
new_houses = {n**2: house + "!" for (n, house) in houses.items()}
print(houses)
print(new_houses)
