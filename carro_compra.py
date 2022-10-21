from carro_compra_funcion import mostrar_productos
from carro_compra_funcion import cantidad_productos

productos = [
    {'prod': 'cocacola', 'cant': 10, 'precio': 2000},
    {'prod': 'fanta', 'cant': 3, 'precio': 2000},
    {'prod': 'sprite', 'cant': 4, 'precio': 4000},
]



mostrar_productos(productos)

print(cantidad_productos(productos))

