import unittest

from seminar2.car import Car
from seminar2.motorcycle import Motorcycle


class VehicleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car("Toyota", "Camry", 2022)
        self.moto = Motorcycle("Yamaha", "FZ-6N", 2007)

    # - Проверить, что экземпляр объекта Car также является экземпляром транспортного средства (используя оператор instanceof)
    def test_car_instance_check(self):
        self.assertIsInstance(self.car, Car)

    # - Проверить, что объект Car создается с 4-мя колесами.
    def car_wheels_check(self):
        self.assertEqual(self.car.get_num_wheels(), 4)

    # - Проверить, что объект Car создается с 2-мя колесами.
    def moto_wheels_check(self):
        self.assertEqual(self.moto.get_num_wheels(), 2)

    # - Проверить, что объект Car развивает скорость 60 в режиме тестового вождения (используя метод testDrive()).
    def car_speed_check(self):
        self.car.test_drive()
        self.assertEqual(self.car_speed_check(), 60)

    # - Проверить, что объект Car развивает скорость 60 в режиме тестового вождения (используя метод testDrive()).
    def moto_speed_check(self):
        self.moto.test_drive()
        self.assertEqual(self.moto_speed_check(), 75)

    # - Проверить, что объект Car развивает скорость 60 в режиме тестового вождения (используя метод testDrive()).
    def car_parking_check(self):
        self.car.test_drive()
        self.car.park()
        self.assertEqual(self.car_speed_check(), 0)

    # - Проверить, что объект Car развивает скорость 60 в режиме тестового вождения (используя метод testDrive()).
    def moto_parking_check(self):
        self.moto.test_drive()
        self.moto.park()
        self.assertEqual(self.moto_speed_check(), 0)


if __name__ == "__main__":
    unittest.main()

