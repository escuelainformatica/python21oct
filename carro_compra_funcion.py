def mostrar_productos(productos_arg: list) -> None:
    for producto in productos_arg:
        print(f"{producto['prod']},{producto['cant']},{producto['precio']}")


def cantidad_productos(productos_arg: list) -> int:
    contador = 0
    for producto in productos_arg:
        contador = contador + producto['cant']
    return contador


def total(productos_arg: list) -> int:
    sumatoria = 0
    for producto in productos_arg:
        sumatoria = sumatoria + producto['cant'] * producto['precio']
    return sumatoria


