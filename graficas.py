import matplotlib.pyplot as plt
import numpy as np

def grafica_mes(lista, tipo):
    largo = len(lista)
    if largo == 12:
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
                 "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        cantidad = lista
    else:
        meses = ["Enero", "Febrero", "Marzo"]
        cantidad = lista

    plt.bar(meses, cantidad, color="blue")
    plt.xlabel("Meses")
    plt.ylabel(tipo)
    plt.title("Grafico de " + tipo)
    plt.show()

def grafica_año(lista, tipo):
    años = ["2020", "2021", "2022", "2023"]
    cantidad = lista

    plt.bar(años, cantidad, color="blue")
    plt.xlabel("Años")
    plt.ylabel(tipo)
    plt.title("Grafico de " + tipo)
    plt.show()
