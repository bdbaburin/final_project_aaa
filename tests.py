import pytest
import pizzeria
import pizza_bones


def test_pizza():
    with pytest.raises(ValueError):
        pizza_bones.Margherita(size="S")


def test_equal():
    pizz1 = pizza_bones.Hawaiian(size="L")
    pizz2 = pizza_bones.Hawaiian(size="L")
    assert pizz1 == pizz2


def test_equal_fail():
    pizz1 = pizza_bones.Hawaiian(size="L")
    assert pizz1 != 1


def test_not_equal():
    pizz1 = pizza_bones.Hawaiian(size="L")
    pizz2 = pizza_bones.Pepperoni(size="XL")
    with pytest.raises(AssertionError):
        assert pizz1 == pizz2


def test_not_equal2():
    pizz1 = pizza_bones.Margherita(size="L")
    pizz2 = pizza_bones.Pepperoni(size="L")
    with pytest.raises(AssertionError):
        assert pizz1 == pizz2


def test_disp():
    pizz1 = pizza_bones.Hawaiian(size="L")
    expected = "Hawaiian 🍍"
    assert expected == pizz1.disp_name


def test_dict():
    expected = {"Hawaiian 🍍": ["tomato sauce", "mozzarella", "chicken", "pineapples"]}
    pizz1 = pizza_bones.Hawaiian(size="L")
    assert pizz1.dict() == expected


def test_bake():
    pizz1 = pizza_bones.Hawaiian(size="L")
    pizz1.bake()
    assert pizz1._is_baked is True


def test_pizzeria_instance():
    with pytest.raises(TypeError):
        pizzeria.Pizzaria(pizzas=[1, 2, 3])


def test_pizzeria_menu():
    pizzer = pizzeria.Pizzaria(pizzas=[pizza_bones.Hawaiian()])
    pizzer.name = "Пепперони рай"
    first_str = "Добро пожаловать в пиццерию Пепперони рай\nНаше меню:\n"
    second_str = "- Hawaiian 🍍 : tomato sauce, mozzarella, chicken, pineapples\n"
    assert pizzer.show_menu() == first_str + second_str


def test_get_order():
    pizzer = pizzeria.Pizzaria(pizzas=[pizza_bones.Hawaiian()])
    with pytest.raises(NameError):
        pizzer.get_order("Pepperoni")


def test_buisiness():
    pizzer = pizzeria.Pizzaria(pizzas=[pizza_bones.Hawaiian()])
    with pytest.raises(NameError):
        pizzer.get_buisiness(order="NNN")


def test_buisiness2():
    pizzer = pizzeria.Pizzaria(pizzas=[pizza_bones.Hawaiian()])
    with pytest.raises(TypeError):
        pizzer.get_buisiness(order=2)


if __name__ == "__main__":
    pass
