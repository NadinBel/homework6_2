from colorama import init, Fore

class Vehicle:
    def __init__(self, owner: str, __model: str, __engine_power: int, __color: str):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def get_model(self):
        return f'Модель: {self.__model}'
    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'
    def get_color(self):
        return f'Цвет: {self.__color}'
    def print_info(self):
        print(Fore.BLUE + self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: ' + Fore.GREEN + (self.owner) + '\033[34m')
    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = Fore.GREEN + new_color + '\033[34m'
        else:
            print(Fore.RED + f'Нельзя сменить цвет на {new_color}')
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
