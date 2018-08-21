import sys
import csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.car_type = None
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        
    def get_photo_file_ext():
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = 'car'
        
    def __str__(self):
        return f'{self.car_type}   {self.brand} {self.passenger_seats_count} {self.photo_file_name} {self.carrying}'


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_length = self.body_width = self.body_height =0
        self.car_type = 'truck'

        if body_whl == "":
            self.body_length = self.body_width = self.body_height = 0
        else:
            whl = body_whl.split('x')
            self.body_length = float(whl[0])
            self.body_width = float(whl[1])
            self.body_height = float(whl[2])

    def __str__(self):
        return f'{self.car_type} {self.brand} {self.photo_file_name} {self.body_length}*{self.body_width}*{self.body_height} {self.carrying}'
           
    def get_body_volume(self):
        return self.body_length*self.body_width*self.body_height
    

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = 'spec_machine'
        
    def __str__(self):
        return f'{self.car_type} {self.brand} {self.photo_file_name} {self.carrying} {self.extra}'
   

def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename,encoding = 'utf-8') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if len(row) ==7:
                car_type = row[0]
                brand = row[1]
                passenger_seats_count = row[2]
                photo_file_name = row[3]
                body_whl = row[4]
                carrying = row[5]
                extra = row[6]
                
                if car_type =="car":
                    vehical = Car(brand, photo_file_name, carrying, passenger_seats_count)
                    car_list.append(vehical)
                elif row[0]=="truck":
                    vehical = Truck(brand, photo_file_name, carrying, body_whl)
                    car_list.append(vehical)
                elif row[0]=="spec_machine":
                    vehical = SpecMachine(brand, photo_file_name, carrying, extra)
                    car_list.append(vehical)
                  
    return car_list

if __name__== '__main__':
    cars =get_car_list('coursera_week3_cars.csv')
    print(cars)
    for car in cars:
        print(car)
    
