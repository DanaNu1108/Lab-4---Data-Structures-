# Exercise 1: Student Grades Analysis

#1. Calculate and print the average score for each student.
students = {
     "Alice": [85, 78, 92],
     "Bob": [79, 74, 81],
     "Charlie": [91, 82, 85],
     "David": [76, 85, 83],
     "Eve": [88, 79, 92]
}


average_grades = []

for name, grades in students.items():
     total = sum(grades)
     average = round(total/len(grades),2)
     print(f"{name}: {average}")
     average_grades.append((name,average))
print()

# 2. Find and print the name of the student with the highest average score.
# 3. Find and print the name of the student with the lowest average score.

max_grade = float('-inf')
min_grade = float('inf')
max_name = ''
min_name = ''

for student in average_grades:
    if student[1] > max_grade:
        max_grade = student[1]
        max_name = student[0]

    if student[1] < min_grade:
        min_grade = student[1]
        min_name = student[0]

print(f"Student with the highest average, {max_name} : {max_grade} ")
print(f"Student with the lowest average, {min_name} : {min_grade} ")

# 4. Add a new student "Frank" with scores [80, 90, 85] to the dictionary and print the updated dictionary.

students["Frank"] = [80, 90, 85]
print(students)

print()

# Exercise 2: Product Inventory Management

inventory = {
 "apple": (50, 0.5),
 "banana": (100, 0.2),
 "orange": (75, 0.3),
 "pear": (20, 0.4)
}

# 1. Print the current inventory in a user-friendly format.

print("Current Inventory:") # title
print("{:<10} {:<10} {:<10}".format("Item", "Quantity", "Price"))
print("_" * 30)

for item, data in inventory.items():
     print("{:<10} {:<10} ${:<10.2f}".format(item, data[0], data[1]))
print("-" * 30)

# 2. Calculate and print the total value of the inventory.
total_value_inventory = 0

for item, data in inventory.items():
     total_value = data[0] * data[1]
     total_value_inventory += total_value

print(f"Value of inventory: ${total_value_inventory}")
print()

# 3. Add a new product "mango" with 30 items priced at $0.6 each to the inventory.
inventory["mango"] = (30, 0.6)

# 4. Update the quantity of "banana" to 120 and print the updated inventory.
inventory["banana"] = (120,0.2)

# 5. Remove "pear" from the inventory and print the updated inventory.
inventory.pop("pear")

print(inventory)

print()

# Exercise 3: Employee Records

employees = [
 ("John Doe", "Accounting", "john.doe@example.com"),
     ("Jane Smith", "Marketing", "jane.smith@example.com"),
     ("Emily Davis", "HR", "emily.davis@example.com"),
     ("Michael Brown", "IT", "michael.brown@example.com")
]

# 1. Print the names and departments of all employees.

print("{:<20} {:<10}". format("Name", "Department"))
print("_" * 40)

for i in employees:
     name = i[0]
     department = i[1]
     print("{:<20} {:<10}". format(name, department))

print()

# 2. Print the email addresses of all employees in alphabetical order by their last names.

list_emails = []

for i in employees:
     _,_,email = i
     list_emails.append(email)

list_sorted = sorted(list_emails, key= lambda x : x.split(".")[1])
print(list_sorted)

# 3. Add a new employee ("David Wilson", "Sales", "david.wilson@example.com") and print the updated list.

employees.append(("David Wilson", "Sales", "david.wilson@example.com"))
print(employees)

# 4. Find and print the department of "Jane Smith".

for i in employees:
     if "Jane Smith" in i:
          department = i[1]
          print(f"Jane Smith is in: {department}")

print()

# Exercise 4: Book Library System

library = {
 "978-3-16-148410-0": {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
 "978-0-14-028329-7": {"title": "1984", "author": "George Orwell", "year": 1949},
 "978-0-7432-7356-5": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
 "978-0-452-28423-4": {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
}

# 1. Print the details of all books in a user-friendly format.
print("{:<20} {:<30} {:<30} {:<10}".format("ISBN", "TITLE", "AUTHOR", "YEAR"))
print("_" * 100)

for key, details in library.items():
     print("{:<20} {:<30} {:<30} {:<10}".format(key, details["title"], details["author"], details["year"]))

print()

# 2. Find and print the details of the book with the ISBN "978-0-14-028329-7".

for key in library.items():
     if "978-0-14-028329-7" in key:
          details = key[1]
          print(f"Book 978-0-14-028329-7 : {details}")

# 3. Add a new book with ISBN "978-1-4028-9462-6", title "The Great Gatsby", author "F. Scott Fitzgerald", and year 1925.

library["978-1-4028-9462-6"] = {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}

# 4. Update the year of "To Kill a Mockingbird" to 1961 and print the updated details.

library["978-0-7432-7356-5"]["year"] = 1961

# 5. Remove the book with ISBN "978-0-452-28423-4" and print the updated library.

del library["978-0-452-28423-4"]

print("Updated library")
print("{:<20} {:<30} {:<30} {:<10}".format("ISBN", "TITLE", "AUTHOR", "YEAR"))
print("_" * 100)

for key, details in library.items():
     print("{:<20} {:<30} {:<30} {:<10}".format(key, details["title"], details["author"], details["year"]))

print()

# Exercise 5: City Population Data

cities = {
 "New York": 8419000,
 "Los Angeles": 3980000,
 "Chicago": 2716000,
 "Houston": 2328000,
 "Phoenix": 1690000
}

# 1. Print the population of each city in a user-friendly format.

print("{:<15} {:<10}".format("City", "Population"))
print("_" * 25)

for city, pop in cities.items():
     print(("{:<15} {:<10}".format(city, pop)))
print()

# 2. Find and print the city with the highest population.
print(f"The city with the highest population: {max(cities, key = cities.get)}")

# 3. Find and print the city with the lowest population.
print(f"The city with the lowest population: {min(cities, key = cities.get)}")
print()

# 4. Update the population of "Phoenix" to 1700000 and print the updated data.
cities["Phoenix"] = 1700000

# 5. Add a new city "San Francisco" with a population of 884000 and print the updated data.
cities["San Francisco"] = 884000

print("Updated data")
print("{:<15} {:<10}".format("City", "Population"))
print("_" * 25)

for city, pop in cities.items():
     print(("{:<15} {:<10}".format(city, pop)))

print()

#Exercise 6: Movie Database

movies = {
 "Inception": {"year": 2010, "rating": 8.8, "genre": "Sci Fi"},
 "The Godfather": {"year": 1972, "rating": 9.2, "genre": "Crime"},
 "The Dark Knight": {"year": 2008, "rating": 9.0, "genre": "Action"},
 "Pulp Fiction": {"year": 1994, "rating": 8.9, "genre": "C rime"},
 "Forrest Gump": {"year": 1994, "rating": 8.8, "genre": "D rama"}
}

# 1. Print the details of all movies in a user-friendly format.
print("{:<20} {:<10} {:<10} {:<10}".format("Title", "Year", "Rating", "Genre"))
print("_" * 50)

for key, details in movies.items():
     print("{:<20} {:<10} {:<10} {:<10}".format(key, details["year"], details["rating"], details["genre"]))

print()
# 2. Find and print the highest-rated movie.

highest = movies[max(movies, key=lambda val: movies[val]['rating'])]

highest_movie_name = (list(movies.keys())[list(movies.values()).index(highest)])

print(f"The movie with the highest rating is : {highest_movie_name}")

print()

# 3. Add a new movie "The Matrix" with year 1999, rating 8.7, and genre "Sci-Fi" to the database.
movies["The Matrix"] = {"year": 1999, "rating": 8.7, "genre": "Sci Fi"}

# 4. Update the rating of "Inception" to 9.0 and print the updated details.
movies["Inception"] = {"year": 2010, "rating": 9.0, "genre": "Sci Fi"}

# 5. Remove "Pulp Fiction" from the database and print the updated list.
del movies["Pulp Fiction"]

print("Updated list")
print("{:<20} {:<10} {:<10} {:<10}".format("Title", "Year", "Rating", "Genre"))
print("_" * 50)

for key, details in movies.items():
     print("{:<20} {:<10} {:<10} {:<10}".format(key, details["year"], details["rating"], details["genre"]))

print()

# Exercise 7: Country Capitals

countries = {
 "USA": "Washington, D.C.",
 "Canada": "Ottawa",
 "France": "Paris",
 "Germany": "Berlin",
 "Japan": "Tokyo"
}

# 1. Print the names of all countries and their capitals.
for k,v in countries.items():
     print(k,"-", v)
print()

# 2. Find and print the capital of Germany.
germany = countries["Germany"]

print(f"Capital of Germany: {germany}")

# 3. Add a new country "Australia" with capital "Canberra" to the dictionary and print the updated dictionary.
countries["Australia"] = "Canberra"

# 4. Update the capital of "USA" to "New Washington" and print the updated dictionary.
countries["USA"] = "New Washington"

# 5. Remove "France" from the dictionary and print the updated dictionary.
del countries["France"]

print(countries)

print()

# Exercise 8: Shopping Cart

cart = [
     {"item": "apple", "quantity": 3, "price_per_unit": 0.5},
     {"item": "banana", "quantity": 6, "price_per_unit": 0.2},
     {"item": "orange", "quantity": 4, "price_per_unit": 0.3},
     {"item": "pear", "quantity": 2, "price_per_unit": 0.4}
]

total_cart = 0
# 1. Print the details of all items in the cart.
for i in cart:
     print(i["item"], "u",i["quantity"], "$",i["price_per_unit"])


# 2. Calculate and print the total cost of the cart.
     value_each = i["quantity"] * i["price_per_unit"]
     total_cart += value_each
print(f"Total cost of the cart is: ${total_cart}")
print()

# 3. Add a new item "grape" with quantity 5 and price per unit 0.6 to the cart.
cart.append({"item": "grape", "quantity": 5, "price_per_unit": 0.6})

# 4. Update the quantity of "banana" to 10 and print the updated cart.
banana = cart[1]

for k,v in banana.items():
     banana["quantity"] = 10

print(cart)

# 5. Remove "pear" from the cart and print the updated cart.
cart.pop(3)
print(cart)

print()

# Exercise 9: Weather Data

weather = {
     "Monday": {"temperature": 20, "humidity": 60},
     "Tuesday": {"temperature": 22, "humidity": 55},
     "Wednesday": {"temperature": 19, "humidity": 65},
     "Thursday": {"temperature": 23, "humidity": 50},
     "Friday": {"temperature": 21, "humidity": 70}
}

# 1. Print the weather details for each day.
for k,v in weather.items():
     print(k, "-", "temperature", v["temperature"], "humidity", v["humidity"])
print()

# 2. Find and print the day with the highest temperature.
highest_temp = weather[max(weather, key=lambda val: weather[val]["temperature"])]
highest_day = (list(weather.keys())[list(weather.values()).index(highest_temp)])
temp = highest_temp["temperature"]

print(f"The day with the highest temperature is {highest_day} with {temp} degrees")

# 3. Find and print the day with the lowest humidity.
lowest_hum = weather[min(weather, key=lambda val: weather[val]["humidity"])]
lowest_day = (list(weather.keys())[list(weather.values()).index(lowest_hum)])
hum = lowest_hum["humidity"]

print(f"The lowest humid day is {lowest_day} with humidity of {hum}")

print()

# 4. Update the temperature of "Wednesday" to 25 and print the updated weather data.
wednesday = weather["Wednesday"]
wednesday["temperature"] = 25
print(weather)

print()

# 5. Add weather data for "Saturday" with temperature 24 and humidity 60 to the dictionary and print the updated weather data.
weather["Saturday"] = {"temperature": 24, "humidity": 60}

for k,v in weather.items():
     print(k, "-", "temperature", v["temperature"], "humidity", v["humidity"])
print()

# Exercise 10: Library Members

members = [
 {"name": "Alice", "age": 25, "books_borrowed": ["1984", "To Kill a Mockingbird"]},
 {"name": "Bob", "age": 30, "books_borrowed": ["The Catcher in the Rye"]},
 {"name": "Charlie", "age": 22, "books_borrowed": ["Brave New World", "1984"]},
 {"name": "David", "age": 35, "books_borrowed": ["The Great Gatsby"]}
]

# 1. Print the names and ages of all members.
for i in members:
     print(i["name"], i["age"], "years old")
print()

# 2. Find and print the books borrowed by "Charlie".
for i in members:
     if "Charlie" in i["name"]:
          print("Charlie borrowed:", i["books_borrowed"])
print()

# 3. Add a new member "Eve" with age 28 and books borrowed ["Pride and Prejudice"] to the list.
members.append({"name": "Eve", "age": 28, "books_borrowed": ["Pride and Prejudice"]})

# 4. Update the age of "Bob" to 31 and print the updated list.
bob = members[1]
bob["age"] = 31
for i in members:
     print(i["name"], i["age"], "years old")
print()

# 5. Remove "David" from the list and print the updated list.
members.pop(3)

for i in members:
     print(list(i.values()))