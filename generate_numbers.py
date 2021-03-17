import random
import csv


def generate_numbers():
    list = []
    # Open file
    file = open('numbers.csv', 'w', newline='')
    writer = csv.writer(file, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    # Generate 10 000 000 random numbers in range (-10000, 10000)
    for i in range(0, 1000000):
        number = random.randint(-1000000, 1000000)
        list.append(number)
        writer.writerow([number])

    print(list)


generate_numbers()

