import csv
from os.path import splitext


class ImportCSV:
    @staticmethod
    def read(csv_filename):
        with open(csv_filename) as csv_fd:
            reader = csv.reader(csv_fd, delimiter=';')
            next(reader)
            csv_text = [row for row in reader]

        return csv_text

    @staticmethod
    def validation_car_type(car_type):
        types = ['car', 'truck', 'spec_machine']
        try:
            validation = car_type[0]
            if validation in types:
                return True

            return False

        except IndexError:
            return False

    @staticmethod
    def validation_brand(brand):
        try:
            validation = brand[1]
            return bool(validation)

        except IndexError:
            return False

    @staticmethod
    def validation_passenger_seats_count(seats):
        try:
            validation = seats[2]
            return validation.isdigit()
        except IndexError:
            return False

    @staticmethod
    def validation_image_format(img_format):
        valid_formats = ['.jpg', '.jpeg', '.png', '.gif']
        try:
            formats = splitext(img_format[3])[1]
            result = formats in valid_formats

            return result

        except IndexError:
            return False

    @staticmethod
    def validation_body_whl(whl):
        try:
            validation = whl[4].split('x', 2)
            if len(validation) == 3:
                w = float(validation[0])
                h = float(validation[1])
                l = float(validation[2])
                return True
            return (0, 0, 0)

        except (IndexError, ValueError):
            return (0, 0, 0)

    @staticmethod
    def validation_carrying(carriyng):
        try:
            validation = carriyng[5]
            validation = float(validation)
            return bool(validation)

        except (IndexError, ValueError):
            return False

    @staticmethod
    def validation_extra_field(extra_field):
        try:
            validation = extra_field[6]
            return bool(validation)

        except IndexError:
            return False

    @staticmethod
    def parse_body_whl(whl):
        _whl = whl[4].split('x', 2)
        return _whl

    @staticmethod
    def image_format(img_format):
        formats = splitext(img_format[3])[1]
        return formats


class CarBase:
    def __init__(self, brand, photo_file_name, carrying, reader=ImportCSV):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        self.reader = reader

    def get_photo_file_ext(self):
        ext = splitext(self.photo_file_name[3])[1]
        return ext


class Car(CarBase):
    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        self.passenger_seats_count = int(passenger_seats_count)
        super().__init__(brand, photo_file_name, carrying)


class Truck(CarBase):
    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        # try:
            self.body_width = float(body_whl[0])
            self.body_height = float(body_whl[1])
            self.body_length = float(body_whl[2])
        # except ValueError:
        #     self.body_width = float(0)
        #     self.body_height = float(0)
        #     self.body_length = float(0)
        # finally:
            super().__init__(brand, photo_file_name, carrying)

    def get_body_volume(self):
        volume = self.body_width * self.body_height * self.body_length
        return float(volume)


class SpecMachine(CarBase):
    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        self.extra = extra
        super().__init__(brand, photo_file_name, carrying)


def get_car_list(csv_filename):
    car_list = []
    reader = ImportCSV()
    text = reader.read(csv_filename)
    for index, row in enumerate(text):
        if reader.validation_car_type(row) and reader.validation_brand(row) and reader.validation_image_format(
                row) and reader.validation_carrying(row):
            if row[0] == 'car' and reader.validation_passenger_seats_count(row):
                car_list.append(Car(row[2], row[1], row[3], row[5]))
            elif row[0] == 'truck':
                car_list.append(Truck(row[4], row[1], row[3], row[5]))
            elif row[0] == 'spec_machine' and reader.validation_extra_field(row):
                car_list.append(SpecMachine(row[6], row[1], row[3], row[5]))

    return car_list


if __name__ == "__main__":
    reader = ImportCSV()
    text = reader.read('coursera_week3_cars.csv')
    print(text)
    for ext in text:
        # print(splitext(ext[3])[1])
        print(
            # reader.validation_car_type(ext), #
            # reader.validation_brand(ext), #
            # reader.validation_passenger_seats_count(ext),
            # reader.validation_image_format(ext), #
            reader.validation_body_whl(ext),
            # reader.validation_carrying(ext), #
            # reader.validation_extra_field(ext),
            # reader.parse_body_whl(ext)
        )
    # cars = get_car_list('coursera_week3_cars.csv')
    # print(cars)
    # print(len(cars))
    # for car in cars:
    #     print(type(car))