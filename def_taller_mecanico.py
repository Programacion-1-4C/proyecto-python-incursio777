from colorama import Fore


def menu_principal():
    print(Fore.WHITE + "biembenido señor: \n",
          "¿que va a hacer hoy? \n",
          Fore.YELLOW + "✔1-reparacion del veiculo\n",
          Fore.MAGENTA + "✔2-repestos y objetos\n",
          Fore.BLACK + "✔3-servis\n",
          Fore.BLUE + "✔4-control de empleados\n",
          Fore.GREEN + "✔5-gestionar autos en espera\n",
          Fore.LIGHTBLUE_EX + "✔6-chequeo de los autos antes de la entrega\n",
          Fore.LIGHTGREEN_EX + "✔7-mostrar la lista de veiculos\n",
          Fore.RED + "✔8-salir del programa")
    return Fore.WHITE + "---------------"


def reparacion_del_veiculo():
    print(Fore.YELLOW + "llegamos a la zona de reparacion\n"
                        "¿que quieres hacer?")
    return "1.remplazar el motor\n" \
           "2.remplazar la bateria\n" \
           "3.remplazar el electro\n" \
           "4.remplazar el filtro de acite\n" \
           "5.remplazar el radiador"


def repuestos_y_objetos():
    print(Fore.MAGENTA + "llegamos a la zona de ventas\n"
                         "¿que quieres hacer?")
    return "1.buscar productos\n" \
           "2.agregar productos y sacarlos del mercado\n" \
           "3.rellenar el stokc de los productos\n" \
           "4.reventa de productos\n" \
           "5.cambiar el precio de un producto\n" \
           "6.buscar informacion en la web\n" \
           "7.ver cajas de heramientas"


def servis():
    print(Fore.BLACK + "llegamos a la zona del servis\n"
                       "¿que quieres hacer?")
    return "1.chapista\n" \
           "2.pintura"


def control_de_empleados():
    print(Fore.BLUE + "chequeamos a los empleados\n"
                      "¿que quieres hacer?")
    return "1.nombre de empleados + profecion \n" \
           "2.contratar o despedir empleados \n" \
           "3.horario de trabajo (entraday salida) \n" \
           "4.escribir el pago por horas de trabajo * dia + las horas extra"


def gestionar_autos_en_espera():
    print(Fore.GREEN + "llegamos a la zona del almacen de autos\n"
                       "¿que quieres hacer?")
    return "1.meter autos en estacionamiento\n" \
           "2.meter autos en taller\n" \
           "3.meter autos en el servis\n" \
           "4.mover auto de est a taller\n" \
           "5.mover auto de est a servis"


def chequeo_de_autos_antes_de_la_entrega():
    print(Fore.LIGHTBLUE_EX + "seleccionar el auto para el control")
    return "1.retirrar autos del taller\n" \
           "2.retirar autos del servis"


def mostrar_lista_de_veiculos():
    print(Fore.LIGHTGREEN_EX + "de que zona deseas ver los veiculos")
    return "1.estacionamiento\n" \
           "2.taller\n" \
           "3.servis"
