# SRP responsabilidad de principio simple.
# si yo tengo un problema complejo, lo divido en problemas sencillos.

def formatear_texto(valor: str | int | float, tamano: int) -> str:
    largo = tamano - len(str(valor))  # apple, 10-5 = 5, samsung, 10-7 = 3
    valorfinal = str(valor) + ' ' * largo
    return valorfinal


def encabezado() -> None:
    print("-" * 34)
    print("|" + formatear_texto('Producto', 10) + "|" +
          formatear_texto('Cantidad', 10) + "|" +
          formatear_texto("Precio", 10) + "|")
    print("-" * 34)


def pie() -> None:
    print("-" * 34)


def tabla_alumnos(alumnos: list) -> None:
    print("-" * 54)
    fila_alumno({'nombre': 'Nombre',
                 'castellano': 'Castellano',
                 'matematica': 'Matematica',
                 'historia': 'Historia'})
    for alumno in alumnos:
        fila_alumno(alumno)
    print("-" * 54)


def fila_alumno(alumno: dict) -> None:
    print("|" + formatear_texto(alumno['nombre'], 10) + "|" +
          formatear_texto(alumno['castellano'], 10) + "|" +
          formatear_texto(alumno['matematica'], 10) + "|" +
          formatear_texto(alumno['historia'], 10) + "|" +
          formatear_texto(promedio(alumno), 8) + "|"
          )


def promedio(alumno: dict) -> float | str:
    if isinstance(alumno['castellano'], str):
        return ''
    else:
        prom = (alumno['castellano'] + alumno['matematica'] + alumno['historia']) / 3
        return round(prom, 1)


def tabla(compras: list) -> None:
    encabezado()
    for compra in compras:
        print("|" + formatear_texto(compra['prod'], 10) + "|"
              + formatear_texto(compra['cant'], 10) + "|"
              + formatear_texto(compra['precio'], 10) + "|")
    pie()
