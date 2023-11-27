from seminar2.vehicle import Vehicle


class Motorcycle (Vehicle):

    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year_release = year
        self.num_wheels = 2
        self.speed = 0

    def test_drive(self):
        self.speed = 75

    def park(self):
        self.speed = 0

    def get_company(self):
        return self.company

    def get_model(self):
        return self.model

    def get_year_release(self):
        return self.year_release

    def get_num_wheels(self):
        return self.num_wheels

    def get_speed(self):
        return self.get_speed

    def __str__(self):
        return f"This moto is a {self.company}, model {self.model}, year {self.year_release}."