def main():
    print("Hello from python-crash-course-2026!")
    x = "beege"
    print(x)
    x = "coding is fun"
    print(x)
    number_5 = 5
    bigger_number = 10
    # == is EQUIVALENCE --- are these two things equivalent?
    if number_5 == bigger_number:
        print("5 is equivalent to 10")
    elif number_5 < bigger_number:
        print("5 is less than 10")
        if bigger_number % number_5 == 0:
            print("10 is divisible by 5")
    else:
        print("5 must be bigger than 10")
    
    for i in range(3):
        print("you are so cool:", i)
    
    counter = 100
    while counter < 105:
        print(counter)
        counter += 1
        # ^----- same as: counter = counter + 1 
    
    fruits = ["banana", "orange", "apple"]
    for fruit in fruits:
        print(fruit)
    
    for position, fruit in enumerate(fruits):
        print(position, fruit)
    
    print(fruits[1])
    fruits.append("strawberry")
    print(fruits)

    fruits[0] = "cherry"
    print(fruits)

    del fruits[2]
    print(fruits)

    my_dict = {
        "grade": 100,
        "name": "Beege",
        "numbers": [3, 57, 3, 7, 23],
        "wearing_hat": True
    }
    print(my_dict["name"])
    my_dict["name"] = "Luke"
    print(my_dict["name"])
    print(my_dict["numbers"][1])
    for key, value in my_dict.items():
        print(key, ":", value)


def monkey_add(first_number, second_number):
    return first_number + second_number

if __name__ == "__main__":
    main()
    my_number = 3
    output = monkey_add(my_number, 4)
    print(output)
