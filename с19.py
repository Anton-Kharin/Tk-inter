import datetime, random


# model

class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def info(self):
        return (self.name, self.price)

class Menu:
    def __init__(self, dishes):
        self.dishes = dishes

    def get_menu_info(self):
        return [dish.info for dish in self.dishes]
    def giwe_ordered(self, order):
        ch, q = order
        for dish in self.dishes:
            if dish.name.startswith(ch):
                return (dish.name, round(dish.price * q, 2))
        return None

class Book:
    def __init__(self):
        self.data = []
        self.filename = 'book.txt'

    def add_item(self, item):
        self.data.append(item)
    def store_data(self):
        with open(self.filename, 'w') as f:
            for item in self.data:
                f.write(','.join(str(el) for el in item)+ '\n')

class Register:
    def __init__(self):
        self.cash = 0.0

    def put(self, money):
        self.cash += money
    def get_cash(self):
        return self.cash

# view

class Waiter:
    def __init__(self, name):
        self.name = name

    def show_time(self, t):
        print(f'current time is {t}')

    def goodbye(self):
        print('We are closed, see you later!')

    def show_cash(self, money):
        print(f'${money:.2f} in register')

    def show_memu(self, menu_info):
        print(f'Good evening. I am {self.name}, and we offer you:')
        for item in menu_info:
            print(f'{item[0]} - ${item[1]:.2f}')
    def take_order(self):
        s = input('your order: ')
        ch, q = s.split()
        return (str.capitalize(ch), int(q))

    def answer_order(self, dish_info):
        if dish_info is None:
            print('Sorry, can\'t do that.')
        else:
            name, cost = dish_info
            print(f'Your ordered {name}, it cost {cost:.2f}')



# controller
class Restaurant:
    def __init__(self,menu, waiter, register):
        self.menu = menu
        self.waiter = waiter
        self.register = register
        self.time = datetime.datetime.now()
        self.book = Book()

    def start(self):
        while self.time.hour < 23:
            self.waiter.show_time(t=self.time.strftime('%H:%M'))
            self.waiter.show_memu(menu_info=self.menu.get_menu_info())
            order = self.waiter.take_order()
            dish_info = self.menu.giwe_ordered(order=order)
            self.waiter.answer_order(dish_info=dish_info)
            if dish_info is not None:
                self.register.put(money=dish_info[1])
                self.book.add_item((
                    self.time.strftime('%H:%M:%S'),
                    *dish_info
                ))
            self.time += datetime.timedelta(minutes=random.randint(0, 59),
                                            seconds=random.randint(0, 59))
        self.waiter.goodbye()
        self.waiter.show_cash(money=self.register.get_cash())
        self.book.store_data()


if __name__ == '__main__':
    dishes = [
        Dish(name="Rizotto",price = 11.99),
        Dish(name="Pizza",price=13.20),
        Dish(name="Spagetti",price=9.50),
    ]

    menu = Menu(dishes=dishes)

    register = Register()

    waiter = Waiter(name='Pablo')

    restaurant = Restaurant(menu=menu, register=register,waiter=waiter)
    restaurant.start()