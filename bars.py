import json
import math

def load_data(filepath):
    with open(filepath, encoding='utf-8')as data:
        return json.load(data)


def get_biggest_bar(data):
    name_bar_max_size_count = ''
    json_data = load_data(data)
    max_seat_count_bar = json_data[0]["Cells"]["SeatsCount"]

    for line in json_data:
        if max_seat_count_bar < line['Cells']['SeatsCount']:
            max_seat_count_bar = line['Cells']['SeatsCount']
            name_bar_max_size_count = line['Cells']['Name']
    return max_seat_count_bar, name_bar_max_size_count


def get_smallest_bar(data):
    name_bar_min_size_count = ''
    json_data = load_data(data)
    min_seat_count_bar = json_data[0]["Cells"]["SeatsCount"]
    for line in json_data:
        if min_seat_count_bar > line['Cells']['SeatsCount']:
            min_seat_count_bar = line['Cells']['SeatsCount']
            name_bar_min_size_count = line['Cells']['Name']
    return min_seat_count_bar, name_bar_min_size_count


def get_closest_bar(data, longitude, latitude):
    json_data = load_data(data)
    temp_distance = 90000.90000
    closest_bar = ''
    for line in json_data:
        if temp_distance > math.sqrt((line["Cells"]["geoData"]["coordinates"][0] - longitude) ** 2 +
                                                     (line["Cells"]["geoData"]["coordinates"][1] - latitude) ** 2):
            temp_distance = math.sqrt((line["Cells"]["geoData"]["coordinates"][0] - longitude) ** 2 +
                                                     (line["Cells"]["geoData"]["coordinates"][1] - latitude) ** 2)

            closest_bar = line["Cells"]["Name"]["Number"]
    return closest_bar, temp_distance


if __name__ == '__main__':
    path_json_file = r'C:\Work\devman.org\devman\bars.json'
    print(get_biggest_bar(path_json_file))
    print(get_smallest_bar(path_json_file))
    longitude = float(input('Введите долготу'))
    latitude = float(input('Введите широту'))
    print(get_closest_bar(path_json_file, longitude, latitude))
