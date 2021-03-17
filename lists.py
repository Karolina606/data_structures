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
        print("Daj mi chwilę, zbieram dane dla LIST...")

        # Time lists
        creating_times_all, creating_time = create_list(number_list, start, stop, step)
        adding_to_list_times = add_to_list(creating_times_all, start, stop, step)
        inserting_times = insert_into_list(number_list, start, stop, step)
        search_times = search_list(number_list, start, stop, step)
        deleting_times = delete_from_list(number_list, start, stop, step)

        main.write_to_csv(out_file, creating_time, adding_to_list_times, inserting_times, search_times, deleting_times)
        numbers_file.close()

        # Inform
        print("Skończyłem zbierać dane dla LIST")

    except OSError:
        print('Coś poszło nie tak, sprawdź czy masz wymagane pliki')


def create_list(number_list, start, stop, step):
    creating_times_all = []
    start_time = time.time()
    new_list = []

    for n in number_list:
        new_list.append(n)
        creating_times_all.append(time.time() - start_time)

    # wybieramy co 500-setną próbkę
    creating_times_step = {}
    for i in range(start, stop, step):
        creating_times_step[i] = creating_times_all[i]

    return creating_times_all, creating_times_step


def add_to_list(creating_time, start, stop, step):
    adding_times = {}
    for i in range(start, stop, step):
        adding_times[i] = (creating_time[i] - creating_time[i - 1])

    return adding_times


def insert_into_list(number_list, start, stop, step):
    inserting_times = {}

    for x in range(start, stop, step):
        current_list = number_list[0:x]

        start_time = time.time()
        current_list.insert(int(x/2) - 1, 0)
        inserting_times[x] = time.time() - start_time

    return inserting_times


def search_list(number_list, start, stop, step):
    searching_times = {}

    for x in range(start, stop, step):
        current_list = number_list[0:x]

        start_time = time.time()

        for i in current_list:
            if i == 1000000000:
                print('Found it in a list')
                break

        searching_times[x] = time.time() - start_time

    return searching_times


def delete_from_list(number_list, start, stop, step):
    deleting_times = {}

    for x in range(start, stop, step):
        current_list = number_list[0:x]
        number_to_delete = current_list(int(x/2))   # wybieramy liczbę ze środka listy jako tą do usunięcia

        start_time = time.time()
        current_list.remove(number_to_delete)       # znajduje na liście numer do usunięcia a następnie go usuwa
        deleting_times[x] = time.time() - start_time

    return deleting_times
