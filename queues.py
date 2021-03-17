import csv
import time
import main
from collections import deque


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
        print("Daj mi chwilę, zbieram dane dla KOLEJEK...")

        # Time queues
        creating_times_all, creating_times = create_queue(number_list, start, stop, step)
        adding_times = add_to_queue(creating_times_all, start, stop, step)
        inserting_times = insert_into_queue(number_list, start, stop, step)
        search_times = search_queue(number_list, start, stop, step)
        deleting_times = delete_from_queue(number_list, start, stop, step)

        main.write_to_csv(out_file, creating_times, adding_times, inserting_times, search_times, deleting_times)
        numbers_file.close()

        # Inform
        print("Skończyłem zbierać dane dla KOLEJEK")

    except OSError:
        print('Coś poszło nie tak, sprawdź czy masz wymagane pliki')


def create_queue(number_list, start, stop, step):
    creating_times_all = []
    queue = deque([])
    start_time = time.time()

    for number in number_list:
        queue.append(number)
        creating_times_all.append(time.time() - start_time)

    creating_times = {}
    for i in range(start, stop, step):
        creating_times[i] = creating_times_all[i]

    return creating_times_all, creating_times


def add_to_queue(creating_times, start, stop, step):
    adding_to_queue_times = {}
    for x in range(start, stop, step):
        adding_to_queue_times[x] = creating_times[x] - creating_times[x-1]

    return adding_to_queue_times


def insert_into_queue(number_list, start, stop, step):
    inserting_times = {}

    for x in range(start, stop, step):
        current_queue = deque(number_list[0:x])
        buffer_queue = deque([])
        # chcemy wstawić element na pierwszą pozycję w stosie, zatem musimy przechować gdzieś chwilowo wartości z
        # niego ściągnięte

        start_time = time.time()

        for i in range(x):
            buffer_queue.append(
                current_queue.popleft())  # zdejmowanie elementów ze stosu aby dostać się do elementu na dole

        current_queue.append(0)  # wstawienie wartości na wybraną wcześniej, pierwszą pozycję

        len_of_buffer = len(buffer_queue)
        for i in range(len_of_buffer):
            current_queue.append(buffer_queue.popleft())  # powrotne wpisanie elementów z bufora do kolejki

        inserting_times[x] = time.time() - start_time

    return inserting_times


def search_queue(number_list, start, stop, step):
    searching_times = {}
    buffer_queue = deque([])

    for x in range(start, stop, step):
        current_queue = deque(number_list[0:x])

        start_time = time.time()

        for i in range(x):
            head_value = current_queue.popleft()
            buffer_queue.append(head_value)
            if head_value == 1000000000:
                print('Found it, in a queue')
                break

        len_of_buffer = len(buffer_queue)
        for i in range(len_of_buffer):
            current_queue.append(buffer_queue.popleft())  # powrotne wpisanie elementów z bufora do kolejki

        searching_times[x] = time.time() - start_time

    return searching_times


def delete_from_queue(number_list, start, stop, step):
    deleting_times = {}

    for x in range(start, stop, step):
        current_queue = deque(number_list[0:x])

        start_time = time.time()
        current_queue.popleft()
        deleting_times[x] = time.time() - start_time

    return deleting_times
