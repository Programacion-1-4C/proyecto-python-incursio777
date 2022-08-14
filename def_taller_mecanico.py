def menu_principal():
      print("biembenido señor: \n"
          "¿que va a hacer hoy? \n"
          "1-reparacion del veiculo\n"
          "2-repestos y objetos\n"
          "3-servis\n"
          "✔4-control de empleados\n"
          "5-gestionar autos en espera\n"
          "6-chequeo de los autos antes de la entrega\n"
          "7-mostrar la lista de veiculos\n"
          "✔8-salir del programa")
      return "---------------"
def reparacion_del_veiculo():
      print("llegamos a la zona de reparacion\n"
            "¿que quieres hacer?")
      return "---------------"
def repuestos_y_objetos():
      print("llegamos a la zona de ventas\n"
            "¿que quieres hacer?")
      return "1.buscar productos\n" \
             "2.agragar productos y sacarlos del mercado\n" \
             "3.rellenar el stokc de los productos\n" \
             "4.reventa de productos\n" \
             "5.cambiar el precio de un producto\n" \
             "6.buscar informacion en la web"
def servis():
      print("llegamos a la zona del servis\n"
            "¿que quieres hacer?")
      return "---------------"
def control_de_empleados():
      print("chequeamos a los empleados\n"
            "¿que quieres hacer?")
      return "1.nombre de empleados + profecion \n" \
             "2.contratar o despedir empleados \n" \
             "3.horario de trabajo (entraday salida) \n" \
             "4.escribir el pago por horas de trabajo * dia + las horas extra"
def gestionar_autos_en_espera():
      print("llegamos a la zona del almacen de autos\n"
            "¿que quieres hacer?")
      return "---------------"
def chequeo_de_autos_antes_de_la_entrega():
      print("seleccionar el auto para el control")
      return "---------------"
def mostrar_lista_de_veiculos():
      print("veiculos")
      return "---------------"


def ord_alf(cadena):
    alfabeto = {
        "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7,
        "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13,
        "n": 14, "ñ": 15, "o": 16, "p": 17, "q": 18, "r": 19,
        "s": 20, "t": 21, "u": 22, "v": 23, "w": 24, "x": 25,
        "y": 26, "z": 27,
    }
    codigos = []
    for letra in cadena:
        codigos.append(alfabeto[letra])
    return codigos


