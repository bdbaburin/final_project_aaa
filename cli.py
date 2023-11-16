import click
from pizzeria import Pizzaria


@click.group()
def cli():
    pass


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.option("--size", default="L")
@click.argument("pizza", nargs=1)
def order(pizza: str, delivery: bool, size: str):
    """Готовит и доставляет пиццу"""
    pizzeria.get_buisiness(order=pizza, delivery=delivery, size=size)


@cli.command()
def menu():
    """Выводит меню"""
    print(pizzeria.show_menu())


if __name__ == "__main__":
    pizzeria = Pizzaria()
    cli()
