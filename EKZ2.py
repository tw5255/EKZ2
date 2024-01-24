#Задача №1
# Напиши функцию на python,
# которая будет принимать номер кредитной карты
# и показывать только последние 4 цифры.
# Остальные цифры должны заменяться звездочками.

def hide_card_number(card_number):
    # Проверяем, что номер карты содержит хотя бы 4 цифры
    if len(card_number) < 4:
        return "Неверный номер карты"

    # Заменяем все цифры, кроме последних 4, звездочками
    hidden_number = "*" * (len(card_number) - 4) + card_number[-4:]

    return hidden_number


card_number = input("Введите номер карты: ")
hidden_number = hide_card_number(card_number)
print(hidden_number)

#Задача №2
# Напишите осмысленный декоратор. Пин код по умолчанию-1234, номер карты-9 символов.

def pin_code_decorator(func):
    def wrapper(pin_code, card_number):
        if pin_code != "1234":
            print("Неверный пин код")
            for _ in range(2):
                pin_code = input("Осталось {} попыток ввода пин кода: ".format(2 - _))
                if pin_code == "1234":
                    break
            else:
                print("Превышено количество попыток ввода пин кода")
                return
        if len(card_number) != 9:
            print("Неверный номер карты")
            print("Платеж не может быть обработан")
            return
        func(pin_code, card_number)
        print("Платеж обработан")
    return wrapper

@pin_code_decorator
def hide_card_number(pin_code, card_number):
    hidden_number = "*" * (len(card_number) - 4) + card_number[-4:]
    print(hidden_number)

pin_code = input("Введите пин код: ")
card_number = input("Введите номер карты: ")
hide_card_number(pin_code, card_number)



#Задача №3
# Реализовать на свободную темы все концепции ООП, соединенные единым смыслом.
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False

    def start_engine(self):
        self.is_running = True
        print("Двигатель автомобиля {} {} запущен".format(self.brand, self.model))

    def stop_engine(self):
        self.is_running = False
        print("Двигатель автомобиля {} {} остановлен".format(self.brand, self.model))

    def drive(self):
        if self.is_running:
            print("Автомобиль {} {} едет".format(self.brand, self.model))
        else:
            print("Сначала нужно запустить двигатель")


class Mechanic:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    def repair(self, car):
        print("Механик {} ремонтирует автомобиль {} {}".format(self.name, car.brand, car.model))
        # Логика ремонта автомобиля
        print("Ремонт автомобиля {} {} завершен".format(car.brand, car.model))


class ServiceCenter:
    def __init__(self, name):
        self.name = name
        self.mechanics = []

    def hire_mechanic(self, mechanic):
        self.mechanics.append(mechanic)
        print("Механик {} принят на работу в сервисный центр {}".format(mechanic.name, self.name))

    def perform_repair(self, car):
        print("Сервисный центр {} начинает ремонт автомобиля {} {}".format(self.name, car.brand, car.model))

        for mechanic in self.mechanics:
            mechanic.repair(car)

        print("Ремонт автомобиля {} {} в сервисном центре {} завершен".format(car.brand, car.model, self.name))


# Создание объектов
car1 = Car("BMW", "X5", 2020)
car2 = Car("Mercedes", "E-Class", 2019)

mechanic1 = Mechanic("Иван", "двигатель")
mechanic2 = Mechanic("Петр", "электрика")

service_center = ServiceCenter("АвтоСервис")

# Найм механиков в сервисный центр
service_center.hire_mechanic(mechanic1)
service_center.hire_mechanic(mechanic2)

# Запуск двигателя и ремонт автомобилей
car1.start_engine()
car2.start_engine()

service_center.perform_repair(car1)
service_center.perform_repair(car2)

# Остановка двигателя
car1.stop_engine()
car2.stop_engine()

# Вождение автомобиля
car1.drive()
car2.drive()



#Задача №4

# Дан класс корзина продуктов. реализовать сложение и вычитание из продуктов.
# В качестве корзины предусмотреть словарь, в который будут помещены продукты,
# Создаете 2 разных объекта, они должны складывать, вычитать.
# **Так же реализуйте бонусную систему.


class ProductBasket:
    def __init__(self):
        self.products = {}

    def add_product(self, product_name, quantity):
        if product_name in self.products:
            self.products[product_name] += quantity
        else:
            self.products[product_name] = quantity

    def add(self, other_basket):
        result = ProductBasket()
        result.products = self.products.copy()
        for product_name, quantity in other_basket.products.items():
            if product_name in result.products:
                result.products[product_name] += quantity
            else:
                result.products[product_name] = quantity
        return result

    def sub(self, other_basket):
        result = ProductBasket()
        result.products = self.products.copy()
        for product_name, quantity in other_basket.products.items():
            if product_name in result.products:
                result.products[product_name] -= quantity
                if result.products[product_name] <= 0:
                    del result.products[product_name]
        return result

    def apply_bonus(self, bonus_percentage):
        result = ProductBasket()
        result.products = self.products.copy()
        for product_name, quantity in result.products.items():
            result.products[product_name] -= int(quantity * bonus_percentage / 100)
        return result

    def print_basket(self):
        for product_name, quantity in self.products.items():
            print(f"{product_name}: {quantity}")



basket1 = ProductBasket()
basket1.add_product("Apple", 5)
basket1.add_product("Banana", 3)

basket2 = ProductBasket()
basket2.add_product("Apple", 2)
basket2.add_product("Orange", 4)

basket3 = basket1.add(basket2)
basket3.print_basket()

basket4 = basket3.sub(basket1)
basket4.print_basket()

basket5 = basket4.apply_bonus(50)
print("Результат после применения бонуса")
basket5.print_basket()



#Задача №5 Класс Tomato

class Tomato:
    states = {
        0: 'зеленый',
        1: 'зрелый',
        2: 'переспелый'
    }

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):                                   # стадия созревания
        if self._state < len(self.states) - 1:
            self._state += 1

    def is_ripe(self):
        return self._state == len(self.states) - 1


class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(index) for index in range(1, num_tomatoes + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:
    def __init__(self, name):
        self.name = name
        self._plant = None

    def work(self):
        if self._plant is not None:
            self._plant.grow_all()
        else:
            print("Нет растения для обработки!")

    def harvest(self):
        if self._plant is None:
            print("Нет растения для сбора урожая!")
        elif self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай собран!")
        else:
            print("Не все томаты созрели! Продолжайте уход за растением.")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:\n"
              "1. Посадите растение -  создаем TomatoBush со списком помидоров.\n"
              "2. Заведите садовника - Васю и передайте ему  растение.\n"
              "3. Садовник работает, чтобы растение стало более зрелым (work()).\n"
              "4. Проверяет, все ли помидоры созрели (harvest()).\n"
              "5. Если да, собирает урожай (give_away_all()).\n"
              "6. Если нет, продолжает работать с растением.")


# Вызов справки по садоводству
Gardener.knowledge_base()

# Создание объектов классов TomatoBush и Gardener
tomato_bush = TomatoBush(1000000)                    # параметры количества томатов
gardener = Gardener("Вася")
gardener._plant = tomato_bush  # Предполагаем, что помидорный куст передается садовнику

# Уход за кустом с помидорами
gardener.work()
gardener.work()
gardener.work()

# Попытка сбора урожая
gardener.harvest()

# Если томаты еще не дозрели, продолжайте ухаживать за ними
gardener.work()

# Собираем урожай
gardener.harvest()
gardener.harvest()



