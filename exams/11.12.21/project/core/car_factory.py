from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar


class CarFactory:
    car_types = {
        'SportsCar': SportsCar,
        'MuscleCar': MuscleCar
    }

    def create_car(self, car_type, model, speed_limit):
        if car_type not in self.car_types:
            raise ValueError('Invalid car type.')
        if car_type in self.car_types:
            return self.car_types[car_type](model, speed_limit)
