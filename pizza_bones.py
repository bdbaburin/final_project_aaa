class PizzaGeneral:
    """Общий макет пиццы. Основа любой пиццы.
    Attributes:
        size (str):
            Размер пиццы (L или XL)

        _ingridients (List[str]):
            Ингридиенты пиццы

        _name (str):
            Название пиццы

        _emoji (str):
            Эмоджи, используемый для пиццы

    Methods:
        disp_name(self) -> str: (property)
            Метод выводит название пиццы в формате: название + смайлик

        dict(self) -> dict
            Метод выводит рецепт пиццы в виде словаря
    """

    def __init__(self, size: str) -> None:
        """Инициализирует базовую пиццу с помощью размера

        Attributes:
            size (str):
                размер пиццы
        Raizes:
            ValueError:
                Если размер пиццы не соответствует XL или L
        """

        if size not in set(["L", "XL"]):
            raise ValueError(
                f"Your pizza size is not available!!! Available sizes are {'L, XL'}"
            )

        self.size = size

        self._ingridients = ["tomato sauce", "mozzarella"]

        self._name = "Basic Pizza"

        self._emoji = "🍕"

        self._is_baked = False

    @property
    def disp_name(self) -> str:
        """
        Свойство выводит название пиццы в формате: название + смайлик
        """
        return self._name + " " + self._emoji

    def __eq__(self, other: object) -> bool:
        """
        dunder метод для реализации сравнения пицц

        Raizes:
            TypeError:
                Если объект, сравнивваемый с пиццей, пиццей не является
        """
        if not isinstance(other, PizzaGeneral):
            return NotImplemented

        return (
            self.size == other.size
            and self._emoji == other._emoji
            and self._ingridients == other._ingridients
            and self._name == other._name
        )

    def dict(self) -> dict:
        """
        Метод выводит рецепт пиццы в виде словаря
        """
        return {self.disp_name: self._ingridients}

    def bake(self) -> None:
        if not self._is_baked:
            self._is_baked = True


class Margherita(PizzaGeneral):
    """
    Пицца маргарита
    """

    def __init__(self, size: str = "L") -> None:
        super().__init__(size=size)
        self._emoji = "🧀"
        self._name = "Margherita"
        self._ingridients.extend(["tomatoes"])


class Pepperoni(PizzaGeneral):
    """
    Пицца пеперони
    """

    def __init__(self, size: str = "L") -> None:
        super().__init__(size=size)
        self._emoji = "🍕"
        self._name = "Pepperoni"
        self._ingridients.extend(["pepperoni"])


class Hawaiian(PizzaGeneral):
    """
    Гавайская пицца (которая с ананасами)
    """

    def __init__(self, size: str = "L") -> None:
        super().__init__(size=size)
        self._emoji = "🍍"
        self._name = "Hawaiian"
        self._ingridients.extend(["chicken", "pineapples"])


if __name__ == "__main__":
    pass
