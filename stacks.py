import csv
import time
import main


def analyze(in_file, out_file, start, stop, step):
    try:
        # Open file with data
        numbers_file = open(in_file, newline='')
        reader = csv.reader(numbers_file, delimiter=" ", quotechar='|')
        number_list = []

        # Read data from file
        for row in reader:
            number_list.append(row)

        # Inform
        print("Daj mi chwilę, zbieram dane dla STOSÓW...")

        # Time stacks
        creating_times_all, creating_times = create_stack(number_list, start, stop, step)
        adding_times = add_to_stack(creating_times_all, start, stop, step)
        inserting_times = insert_into_stack(number_list, start, stop, step)
        search_times = search_stack(number_list, start, stop, step)
        deleting_times = delete_from_stack(number_list, start, stop, step)

        main.write_to_csv(out_file, creating_times, adding_times, inserting_times, search_times, deleting_times)
        numbers_file.close()

        # Inform
        print("Skończyłem zbierać dane dla STOSÓW")

    except OSError:
        print('Coś poszło nie tak, sprawdź czy masz wymagane pliki')


def create_stack(number_list, start, stop, step):
    stack = []

    creating_times_all = []
    start_time = time.time()

    for number in number_list:
        stack.append(number)
        creating_times_all.append(time.time() - start_time)

    # wybieramy co 500-setną próbkę
    creating_times_step = {}
    for i in range(start, stop, step):
        creating_times_step[i] = creating_times_all[i]

    return creating_times_all, creating_times_step


def add_to_stack(creating_times, start, stop, step):
    adding_to_stack_times = {}
    for x in range(start, stop, step):
        adding_to_stack_times[x] = creating_times[x] - creating_times[x-1]

    return adding_to_stack_times


def insert_into_stack(number_list, start, stop, step):
    inserting_times = {}

    for x in range(start, stop, step):
        current_stack = number_list[0:x]
        buffer_stack = []

        # chcemy wstawić element na pierwszą pozycję w stosie, zatem musimy przechować gdzieś chwilowo wartości z
        # niego ściągnięte
        start_time = time.time()

        for i in range(x):
            buffer_stack.append(
                current_stack.pop())  # zdejmowanie elementów ze stosu aby dostać się do elementu na dole

        current_stack.append(0)  # wstawienie wartości na wybraną wcześniej, pierwszą pozycję

        len_of_buffer = len(buffer_stack)
        for i in range(len_of_buffer):
            current_stack.append(buffer_stack.pop())  # powrotne wpisanie elementów z bufora na stos

        inserting_times[x] = time.time() - start_time

    return inserting_times


def search_stack(number_list, start, stop, step):
    searching_times = {}
    buffer_stack = []

    for x in range(start, stop, step):
        current_stack = number_list[0:x]

        start_time = time.time()

        for i in range(x):
            top_value = current_stack.pop()
            buffer_stack.append(top_value)
            if top_value == 1000000000:
                print('Found it, on a stack')
                break

        len_of_buffer = len(buffer_stack)
        for i in range(len_of_buffer):
            current_stack.append(buffer_stack.pop())  # powrotne wpisanie elementów z bufora na stos

        searching_times[x] = time.time() - start_time

    return searching_times


def delete_from_stack(number_list, start, stop, step):
    deleting_times = {}

    for x in range(start, stop, step):
        current_stack = number_list[0:x]

        start_time = time.time()
        current_stack.pop()
        deleting_times[x] = time.time() - start_time

    return deleting_times
