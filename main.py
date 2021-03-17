from configparser import ConfigParser
import csv
import arrays
import lists
import stacks
import queues


def main():
    try:
        file = 'config.ini'
        config = ConfigParser()
        config.read(file)

        # .analyze(in_file, out_file, start, stop, step)
        arrays.analyze(config['data']['file'], config['result']['arrays'],
                      int(config['operation']['start_instance_size']),
                      int(config['operation']['end_instance_size']), int(config['operation']['step']))

        lists.analyze(config['data']['file'], config['result']['lists'],
                      int(config['operation']['start_instance_size']),
                      int(config['operation']['end_instance_size']), int(config['operation']['step']))

        stacks.analyze(config['data']['file'], config['result']['stacks'],
                       int(config['operation']['start_instance_size']),
                       int(config['operation']['end_instance_size']), int(config['operation']['step']))

        queues.analyze(config['data']['file'], config['result']['queues'],
                       int(config['operation']['start_instance_size']),
                       int(config['operation']['end_instance_size']), int(config['operation']['step']))

        print('Skończyłem, wciśnij cokolwiek, aby mnie wyłączyć...')

    except ConfigParser.Error:
        print("Coś poszło nie tak, sprawdź czy plik inicjujący istnieje lub czy jest dobrze napisany")


def write_to_csv(out_file_name, creating_times, adding_times, inserting_times, searching_times, deleting_times):
    out_file = open(out_file_name, 'w', newline='')
    headers = ['instance_size', 'creating_time', 'adding_time', 'inserting_time', 'searching_time', 'deleting_time']
    writer = csv.DictWriter(out_file, delimiter=';', lineterminator='\n', fieldnames=headers)

    writer.writeheader()

    for i in range(len(adding_times)):
        writer.writerow({'instance_size': list(inserting_times.keys())[i],
                         'creating_time': str(list(creating_times.values())[i]).replace('.', ','),
                         'adding_time': str(list(adding_times.values())[i]).replace('.', ','),
                         'inserting_time': str(list(inserting_times.values())[i]).replace('.', ','),
                         'searching_time': str(list(searching_times.values())[i]).replace('.', ','),
                         'deleting_time': str(list(deleting_times.values())[i]).replace('.', ',')})

    out_file.close()


if __name__ == "__main__":
    main()

main()
