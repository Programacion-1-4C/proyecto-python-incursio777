def menu_principal():
    print("biembenido señor: \n"
          "¿que va a hacer hoy? \n"
          "✔1-reparacion del veiculo\n"
          "✔2-repestos y objetos\n"
          "✔3-servis\n"
          "✔4-control de empleados\n"
          "✔5-gestionar autos en espera\n"
          "✔6-chequeo de los autos antes de la entrega\n"
          "✔7-mostrar la lista de veiculos\n"
          "✔8-salir del programa")
    return "---------------"


def reparacion_del_veiculo():
    print("llegamos a la zona de reparacion\n"
          "¿que quieres hacer?")
    return "1.remplazar el motor\n" \
           "2.remplazar la bateria\n" \
           "3.remplazar el electro\n" \
           "4.remplazar el filtro de acite\n" \
           "5.remplazar el radiador"


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
    return "1.chapista\n" \
           "2.pintura"


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
    return "1.meter autos en estacionamiento\n" \
           "2.meter autos en taller\n" \
           "3.meter autos en el servis\n" \
           "4.mover auto de est a taller\n" \
           "5.mover auto de est a servis"


def chequeo_de_autos_antes_de_la_entrega():
    print("seleccionar el auto para el control")
    return "1.retirrar autos del taller\n" \
           "2.retirar autos del servis"


def mostrar_lista_de_veiculos():
    print("de que zona deseas ver los veiculos")
    return "1.estacionamiento\n" \
           "2.taller\n" \
           "3.servis"
