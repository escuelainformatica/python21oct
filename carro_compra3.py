import carro_compra_funcion

compras=[
    {'prod':"samsung",'cant':5,'precio':50000},
    {'prod':"apple",'cant':2,'precio':80000},
    {'prod':"microsoft",'cant':3,'precio':60000}
]

carro_compra_funcion.mostrar_productos(compras)

print(f"la cantidad de productos es {carro_compra_funcion.cantidad_productos(compras)} ")
