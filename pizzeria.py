from pizza_bones import Hawaiian, Margherita, Pepperoni, PizzaGeneral
from typing import List
import random
from tqdm import tqdm
from time import sleep
from decorator import pizza_log


PIZZERIA_NAMES = [
    "Пиццезвон",
    "Горячая Дуомо",
    "Римские секреты",
    "Везучий Тесто",
    "Маленькая Италия",
    "Пепперони Рай",
    "Вкус Тосканы",
    "Деревенская Лавка",
    "Сицилийские Сокровища",
    "Пицца-Вкусняшка",
]

MAX_BAKING_TIME = {"L": 4, "XL": 8}


class Pizzaria:
    """Самая обычная пиццерия, которая будет нам готовить пиццу
    Attributes:
        pizzas (List[PizzaGeneral]):
            Пиццы в меню

        name (str):
            Название пиццерии (выбирается случайно из PIZZERIA_NAMES)

        menu (List[Dict]):
            Меню заведения в формате {Пицца: список ингридиентов}

        to_bake (List):
            Список пицц, которые нужно испечь

        to_delivery (List):
            Список пицц, которые нужно доставить

        to_takeaway (List):
            Список пицц, которые нужно подготовить к самовывозу

        dict_menu (dict):
            Поварской чеклист для готовки пиццы в формате {Название: пицца}

    Methods:
        show_menu(self) -> str
            Метод выводит меню пиццерии

        get_order(self, name: str, delivery: bool = False, size: str = "L") -> None
            Метод позволяет приимать пиццерии заказы

        bake(self) -> None:
            Печет пиццу на кухне пиццерии

        get_order_delivered(self) -> None
            Метод доставляет пиццы, котовые к доставке

        get_order_takeaway(self) -> None
            Метод подготавливает к самовывозу готовые пиццы

        get_buisiness(self, order: str, delivery: bool = False, size: str = "L") -> None
            Метод запускает основные бизнес-процессы пиццерии:
            -прием заказов
            -готовка пицц
            -подготовка к самовывозу
            -доставка
    """

    def __init__(
        self, pizzas: List["PizzaGeneral"] = [Hawaiian(), Margherita(), Pepperoni()]
    ) -> None:
        """Создает инстанс пиццерии

        Attributes:
            pizzas (List[PizzaGeneral]):
                Пиццы, доступные в меню пиццерии

        Raises:
            TypeError:
                Возникает, если пиццерию заставляют готовить не пиццы, а что-то другое
        """
        if not all(map(lambda x: isinstance(x, PizzaGeneral), pizzas)):
            raise TypeError("Наша пиццерия готовит только пиццы!")

        self.pizzas = pizzas
        self.name = random.choice(PIZZERIA_NAMES)
        self.menu = [list(piz.dict().items())[0] for piz in self.pizzas]
        self.to_bake: List[PizzaGeneral] = []
        self.to_delivery: List[PizzaGeneral] = []
        self.to_takeaway: List[PizzaGeneral] = []
        self.dict_menu = {piz._name: piz for piz in self.pizzas}

    def show_menu(self) -> str:
        """Метод создает строку с меню пиццерии"""

        menu_str = f"Добро пожаловать в пиццерию {self.name}\nНаше меню:\n"
        for piz in self.menu:
            name, ingred = piz
            ingred = ", ".join(ingred)
            menu_str += f"- {name} : {ingred}\n"

        return menu_str

    def get_order(self, name: str, delivery: bool = False, size: str = "L") -> None:
        """Метод позволяет принимать заказы

        Parameters:
            name (str):
                Название пиццы из меню
            delivery (bool):
                Флаг, показывающий, нужна ли доставка
            size (str) (default = L):
                Размер желаемой пиццы
                    (доступные размеры L или XL)
        """
        names = [piz._name for piz in self.pizzas]
        if name.lower().capitalize() not in set(names):
            raise NameError("Такой пиццы нет в меню, попробуйте выбрать другую")

        if size not in MAX_BAKING_TIME.keys():
            raise NameError("Такого размера нет в меню, попробуйте выбрать другой")

        menu_pos = name.lower().capitalize()
        pizza = self.dict_menu[menu_pos]
        pizza.size = size
        self.to_bake.append(pizza)
        if delivery:
            self.to_delivery.append(pizza)
        else:
            self.to_takeaway.append(pizza)

    @pizza_log("🔥🔪 Испекли пиццу за {:.2f}с")
    def bake(self) -> None:
        """Метод позволяет печь пиццу на кухне пиццерии"""

        with tqdm(total=100, desc="Baking") as pbar:
            num_to_bake = len(self.to_bake)
            while self.to_bake:
                max_time = MAX_BAKING_TIME[self.to_bake[0].size]
                sleep(random.randint(1, max_time))
                pbar.update(100 / (num_to_bake * 3))
                self.to_bake[0].bake()
                self.to_bake.pop(0)
                sleep(random.randint(1, max_time))
                pbar.update(100 / (num_to_bake * 3))
                sleep(random.randint(1, max_time))
                pbar.update(100 / (num_to_bake * 3))

    @pizza_log("🛵 Доставили за {:.2f}с!")
    def get_order_delivered(self) -> None:
        """Метод доставляет пиццы, котовые к доставке"""

        if self.to_delivery:
            with tqdm(total=100, desc="Delivery") as pbar:
                num_to_delivery = len(self.to_delivery)
                while self.to_delivery:
                    sleep(random.randint(1, 4))
                    pbar.update(100 / (num_to_delivery * 3))
                    self.to_delivery.pop(0)
                    sleep(random.randint(1, 4))
                    pbar.update(100 / (num_to_delivery * 3))
                    sleep(random.randint(1, 4))
                    pbar.update(100 / (num_to_delivery * 3))

    @pizza_log("🏠 Забрали за {:.2f}с!")
    def get_order_takeaway(self) -> None:
        """Метод подготавливает к самовывозу готовые пиццы"""
        if self.to_takeaway:
            with tqdm(total=100, desc="Takeaway") as pbar:
                num_to_takeaway = len(self.to_takeaway)
                while self.to_takeaway:
                    sleep(random.randint(1, 4))
                    pbar.update(100 / (num_to_takeaway * 3))
                    self.to_takeaway.pop(0)
                    sleep(random.randint(1, 4))
                    pbar.update(100 / (num_to_takeaway * 3))
                    sleep(random.randint(1, 4))
                    pbar.update(100 / (num_to_takeaway * 3))

    def get_buisiness(
        self, order: str, delivery: bool = False, size: str = "L"
    ) -> None:
        """Метод запускает основные бизнес-процессы пиццерии:
        -прием заказов
        -готовка пицц
        -подготовка к самовывозу
        -доставка

        Parameters:
        order (str):
            Название пиццы из меню
        delivery (bool):
            Флаг, показывающий, нужна ли доставка
        size (str) (default = L):
            Размер желаемой пиццы
                (доступные размеры L или XL)
        """

        if not isinstance(order, str):
            raise TypeError("Pizza name must be string")

        if not isinstance(size, str):
            raise TypeError("Size name must be string")

        self.get_order(order, delivery=delivery, size=size.upper())
        self.bake()
        if self.to_delivery:
            self.get_order_delivered()
        else:
            self.get_order_takeaway()


if __name__ == "__main__":
    pizzaria = Pizzaria()
    pizzaria.get_buisiness("Hawaiian", delivery=True, size="XL")
