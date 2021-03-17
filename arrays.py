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

        # Create the array
        array = [None] * len(number_list)

        # Inform
        print("Daj mi chwilę, zbieram dane dla TABLIC...")

        # Time arrays
        creating_times_all, creating_times = create_array(number_list, array, start, stop, step)
        adding_times = add_to_array(creating_times_all, start, stop, step)
        inserting_times = insert_into_array(number_list, start, stop, step)
        search_times = search_array(number_list, start, stop, step)
        deleting_times = delete_from_array(number_list, start, stop, step)

        main.write_to_csv(out_file, creating_times, adding_times, inserting_times, search_times, deleting_times)
        numbers_file.close()

        # Inform
        print("Skończyłem zbierać dane dla TABLIC")

    except OSError:
        print('Coś poszło nie tak, sprawdź czy masz wymagane pliki')


def create_array(number_list, array, start, stop, step):
    creating_times_all = []
    start_time = time.time()

    i = 0
    for number in number_list:
        array[i] = number
        i += 1
        creating_times_all.append(time.time() - start_time)

    # wybieramy co 500-setną próbkę
    creating_times_step = {}
    for i in range(start, stop, step):
        creating_times_step[i] = creating_times_all[i]

    return creating_times_all, creating_times_step


def add_to_array(creating_time, start, stop, step):
    adding_to_array_times = {}

    for i in range(start, stop, step):

        adding_to_array_times[i] = (creating_time[i] - creating_time[i - 1])

    return adding_to_array_times


def insert_into_array(number_list, start, stop, step):
    inserting_times = {}

    for x in range(start, stop, step):
        current_array = number_list[0:x]

        start_time = time.time()
        current_array[int(x/2)] = 0
        inserting_times[x] = time.time() - start_time

    return inserting_times


def search_array(number_list, start, stop, step):
    searching_times = {}

    for x in range(start, stop, step):
        current_array = number_list[0:x]

        start_time = time.time()

        for i in range(0, len(current_array)-1):
            if current_array[i] == 1000000:
                print('Found it in the array')
                break

        searching_times[x] = time.time() - start_time

    return searching_times


def delete_from_array(number_list, start, stop, step):
    deleting_times = {}

    for x in range(start, stop, step):
        current_array = number_list[0:x]
        # tworzymy nową tablicę z długością mniejszą o 1, ponieważ usuniemy jeden element
        new_array = [None] * (x-1)

        start_time = time.time()

        # usuniemy ostatni element, czyli pominiemy go przy przepisywaniu
        for i in range(x-1):
            new_array[i] = current_array[i]

        deleting_times[x] = time.time() - start_time

    return deleting_times
