import webbrowser as web  # utilizar un sitio web
from time import sleep
from tqdm import tqdm
from colorama import Fore
from def_taller_mecanico import menu_principal
from def_taller_mecanico import reparacion_del_veiculo
from def_taller_mecanico import repuestos_y_objetos
from def_taller_mecanico import servis
from def_taller_mecanico import control_de_empleados
from def_taller_mecanico import gestionar_autos_en_espera
from def_taller_mecanico import chequeo_de_autos_antes_de_la_entrega
from def_taller_mecanico import mostrar_lista_de_veiculos

# variavles de eleccion 2 venta
productos = [("motor", 4000, 30), ("electro", 14, 20), ("bateria", 20, 40), ("rueda", 666, 50)]
heramientas = ["caja de heramientas", 10, 10]
# variavles de eleccion 3 stock y 1
empleados2 = []
trabajo_2 = []
hora_de_entrada2 = []
hora_de_salida2 = []
min_de_entrada2 = []
min_de_salida2 = []
# variables de eleccion 4 empleados
empleados = ["Tomas", "Lucas", "Martin", "Javier"]
trabajo = ["bateria", "motor", "electro", "motor"]
hora_de_entrada = [4, 10, 5, 9]
hora_de_salida = [12, 18, 13, 18]
min_de_entrada = [30, 15, 0, 45]
min_de_salida = [30, 15, 0, 0]
gnancia_por_hora = 6.4
ganancia_por_min = 0.1
# variabels de la eleccion 5
autos_en_estacionamiento = []
autos_en_taller = ["AA111BA"]
autos_en_servis = ["BB123AA"]
espacio_de_estacionamiento = 10
espacio_de_taller = 3
espacio_de_servis = 5
autos_trabajados = []
autos_trabajados_servis = []
# todo lo que este en esta linea sera solo de almacenamiento de informacion
# todo lo de esta seran if/elif de la eleccion pricipal
# todo lo de esta seran while para repetir las opciones
# finalmente esta seran if/elif para una sub eleccion
while True:
    print(menu_principal())
    eleccion_1 = int(input(">>>"))

    if eleccion_1 == 1:
        while True:

            print(reparacion_del_veiculo())
            eleccion_1_1 = int(input(">>>"))
            print(autos_en_taller)
            auto_para_arreglo = input("seleccionar el auto\n"
                                      ">>>")
            if auto_para_arreglo in autos_en_taller:
                pass
            else:
                eleccion_1_1 = -1
            if eleccion_1_1 == 1:
                objeto_2 = "motor"
            elif eleccion_1_1 == 2:
                objeto_2 = "bateria"
            elif eleccion_1_1 == 3:
                objeto_2 = "electro"
            elif eleccion_1_1 == 4:
                objeto_2 = "filtro"
            elif eleccion_1_1 == 5:
                objeto_2 = "radiador"
            elif eleccion_1_1 == -1:
                print("auto no esncontrado")

            if eleccion_1_1 != -1:
                contador = 0
                contador_2 = len(productos)
                while contador_2 > 0:
                    if objeto_2 in productos[contador]:
                        para_pago = contador
                        objeto = True
                    else:
                        pass
                    contador += 1
                    contador_2 -= 1
                if objeto:
                    print("veamos quien esta disponible para hacer el recambio")
                    if objeto_2 in trabajo:
                        busqueda_de_trabajador = trabajo.index("motor")
                        print("tenemos disponibe a", empleados[busqueda_de_trabajador])
                        print("el pago sera de", productos[para_pago][1], "dolares")
                        productos_a_list = list(productos[para_pago])
                        productos_a_list[2] -= 1
                        list_a_prodocto = tuple(productos_a_list)
                        productos[para_pago] = list_a_prodocto
                        empleados2 += [empleados[busqueda_de_trabajador]]
                        trabajo_2 += [trabajo[busqueda_de_trabajador]]
                        hora_de_entrada2 += [hora_de_entrada[busqueda_de_trabajador]]
                        hora_de_salida2 += [hora_de_salida[busqueda_de_trabajador]]
                        min_de_entrada2 += [min_de_entrada[busqueda_de_trabajador]]
                        min_de_salida2 += [min_de_salida[busqueda_de_trabajador]]
                        del empleados[busqueda_de_trabajador]
                        del trabajo[busqueda_de_trabajador]
                        del hora_de_entrada[busqueda_de_trabajador]
                        del hora_de_salida[busqueda_de_trabajador]
                        del min_de_entrada[busqueda_de_trabajador]
                        del min_de_salida[busqueda_de_trabajador]
                        auto = autos_en_taller.index(auto_para_arreglo)
                        autos_trabajados += [auto_para_arreglo]
                        del autos_en_taller[auto]
                        heramientas[2] -= 1

                    else:
                        print("no hay nadie que pueda realizar el trabajo")

                else:
                    print("el objeto", objeto_2, "no se encuentra en la cadana o en stock\n"
                                                 "nos es imposible hacer el recambio ahora")

            salida = input("algo mas (si/no)\n"
                           ">>>")
            if salida == "si":
                pass
            else:
                break

    elif eleccion_1 == 2:
        while True:
            print(repuestos_y_objetos())
            eleccion_2_1 = int(input(">>>"))
            if eleccion_2_1 == 1:  # buscar productos
                orden = int(input("buscar objeto por\n"
                                  "1.A-Z\n"
                                  "2.Z-A\n"
                                  "3.stock + a -\n"
                                  "4.stock - a +\n"
                                  "5.precio + a -\n"
                                  "6.precio - a +\n"
                                  ">>>"))
                if orden == 1:
                    print("ordenado de la A a la Z")
                    print(sorted(productos, key=lambda objetos: objetos[0]))
                elif orden == 2:
                    print("ordenado de la Z a la A")
                    print(sorted(productos, key=lambda objetos: objetos[0], reverse=True))
                elif orden == 3:
                    print("ordenado del stock + a -")
                    print(sorted(productos, key=lambda objetos: objetos[2]))
                elif orden == 4:
                    print("ordenado del stock - a +")
                    print(sorted(productos, key=lambda objetos: objetos[2], reverse=True))
                elif orden == 5:
                    print("ordenado del precio + a -")
                    print(sorted(productos, key=lambda objetos: objetos[1], reverse=True))
                elif orden == 6:
                    print("ordenado del precio - a +")
                    print(sorted(productos, key=lambda objetos: objetos[1]))
            if eleccion_2_1 == 2:  # agragar productos y sacarlos del mercado
                A_o_S = input("queires agregar o sacar productos (a/s)\n"
                              ">>>")
                if A_o_S == "a":
                    producto_nuevo = input("que producto nuevo sera\n"
                                           ">>>")
                    stock_nuevo = int(input("cual es el stonk del producto\n"
                                            ">>>"))
                    if stock_nuevo < 0:
                        print("secuencia invalida")
                        break
                    precio_nuevo = int(input("cual es el precio\n"
                                             ">>>"))
                    if precio_nuevo < 0:
                        print("secuencia invalida")
                        break
                    productos.append((producto_nuevo, stock_nuevo, precio_nuevo))
                    print(productos)
                if A_o_S == "s":
                    print(productos)
                    eliminar = int(input("decide que producto vas a eliminar definitivamente (seleccionar por nª)\n"
                                         ">>>"))
                    del productos[eliminar - 1]
                    print(productos)
            if eleccion_2_1 == 3:  # rellenar stock de un producto
                print("selecciona cual de los siguientes productos tienen nuevo stonk\n",
                      productos, "por numero")
                cadena_de_stonk = []
                while True:
                    stock_nuevo = int(input(">>>"))
                    cadena_de_stonk += [stock_nuevo - 1]
                    algo_mas = input("algun otro producto mas (si/no)\n"
                                     ">>>")
                    if algo_mas == "si":
                        pass
                    else:
                        break
                nuevo_stonk = len(cadena_de_stonk)
                contador = 0
                while nuevo_stonk > 0:
                    print(productos[cadena_de_stonk[contador]][0],
                          "cuantos productos nuevos llegron")
                    stock_nuevo = int(input(">>>"))
                    productos_a_list = list(productos[cadena_de_stonk[contador]])
                    productos_a_list[2] += stock_nuevo
                    list_a_prodocto = tuple(productos_a_list)
                    productos[cadena_de_stonk[contador]] = list_a_prodocto
                    nuevo_stonk -= 1
                    contador += 1
            if eleccion_2_1 == 4:  # reventa de productos
                print("selecciona cual de los siguientes productos van en el encargo\n",
                      productos, "\n>>>")
                cadena_de_stonk = []
                while True:
                    stock_nuevo = int(input(">>>"))
                    cadena_de_stonk += [stock_nuevo - 1]
                    algo_mas = input("algo mas (si/no)\n"
                                     ">>>")
                    if algo_mas == "si":
                        pass
                    else:
                        break
                nuevo_stonk = len(cadena_de_stonk)
                contador = 0
                while nuevo_stonk > 0:
                    print(productos[cadena_de_stonk[contador]][0],
                          "cuantos productos van en el envio")
                    stock_nuevo = int(input(">>>"))
                    if productos[cadena_de_stonk[contador]][2] > 0:
                        productos_a_list = list(productos[cadena_de_stonk[contador]])
                        productos_a_list[2] -= stock_nuevo
                        list_a_prodocto = tuple(productos_a_list)
                        productos[cadena_de_stonk[contador]] = list_a_prodocto
                        if productos[cadena_de_stonk[contador]][2] > -1:
                            pass
                        else:
                            print("no hay suficientes objetos para la venta")
                            productos_a_list = list(productos[cadena_de_stonk[contador]])
                            productos_a_list[2] += stock_nuevo
                            list_a_prodocto = tuple(productos_a_list)
                            productos[cadena_de_stonk[contador]] = list_a_prodocto
                        nuevo_stonk -= 1
                        contador += 1
                    else:
                        print("no hay unidades para vender")
                        nuevo_stonk -= 1
                        contador += 1
            if eleccion_2_1 == 5:
                print("selecciona cual de los siguientes productos cambiaran su precio\n",
                      productos, "\n>>>")
                cadena_de_precios = []
                while True:
                    precio_nuevo = int(input(">>>"))
                    cadena_de_precios += [precio_nuevo - 1]
                    algo_mas = input("algo mas (si/no)\n"
                                     ">>>")
                    if algo_mas == "si":
                        pass
                    else:
                        break
                nuevo_precio = len(cadena_de_precios)
                contador = 0
                while nuevo_precio > 0:
                    print(productos[cadena_de_precios[contador]][0],
                          "cual sea su nuevo precio")
                    precio_nuevo = int(input(">>>"))
                    productos_a_list = list(productos[cadena_de_precios[contador]])
                    productos_a_list[1] = precio_nuevo
                    list_a_prodocto = tuple(productos_a_list)
                    productos[cadena_de_precios[contador]] = list_a_prodocto
                    nuevo_precio -= 1
                    contador += 1
            if eleccion_2_1 == 6:
                web.open("https://blog.nhautopiezas.com.ar/2021/06/23/estamos-en-cordoba/?gclid"
                         "=Cj0KCQjwuuKXBhCRARIsAC-gM0jTWlqVcgOzjj6lFdY752vLCGgEI02OxBw"
                         "-bZcqx0db9mh9T_BrIkAaAsfvEALw_wcB")
            if eleccion_2_1 == 7:
                print("el numero de cajas de heramientas es", heramientas[1],
                      "y en uso estan", 10-heramientas[2])
            salida = input("algo mas (si/no)\n"
                           ">>>")
            if salida == "si":
                pass
            else:
                break

    elif eleccion_1 == 3:
        while True:
            print(servis())
            eleccion_3_1 = int(input(">>>"))
            print(autos_en_servis)
            auto_para_arreglo = input("seleccionar el auto\n"
                                      ">>>")
            if auto_para_arreglo in autos_en_servis:
                pass
            else:
                eleccion_3_1 = -1
            if eleccion_3_1 == 1:
                objeto = False
                chapista = int(input("que deseas que el chapista aregle\n"
                                     "1.cambio de ruedas\n"
                                     "2.reponer el paragolpes\n"
                                     "3.repuner la puerta\n"
                                     "4.reponer los vidrios\n"
                                     "5.reponer el espejo\n"
                                     ">>>"))
                if chapista == 1:
                    objeto_2 = "rueda"
                elif chapista == 2:
                    objeto_2 = "paragolpes"
                elif chapista == 3:
                    objeto_2 = "puerta"
                elif chapista == 4:
                    objeto_2 = "vidrio"
                elif chapista == 5:
                    objeto_2 = "espejo"

                contador = 0
                contador_2 = len(productos)
                while contador_2 > 0:
                    if objeto_2 in productos[contador]:
                        para_pago = contador
                        objeto = True
                    else:
                        pass
                    contador += 1
                    contador_2 -= 1
                if objeto:
                    print("veamos quien esta disponible para hacer el recambio")
                    if "chapista" in trabajo:
                        busqueda_de_trabajador = trabajo.index("chapista")
                        print("tenemos disponibe a", empleados[busqueda_de_trabajador])
                        print("el pago sera de", productos[para_pago][1], "dolares")
                        productos_a_list = list(productos[para_pago])
                        productos_a_list[2] -= 1
                        list_a_prodocto = tuple(productos_a_list)
                        productos[para_pago] = list_a_prodocto
                        empleados2 += [empleados[busqueda_de_trabajador]]
                        trabajo_2 += [trabajo[busqueda_de_trabajador]]
                        hora_de_entrada2 += [hora_de_entrada[busqueda_de_trabajador]]
                        hora_de_salida2 += [hora_de_salida[busqueda_de_trabajador]]
                        min_de_entrada2 += [min_de_entrada[busqueda_de_trabajador]]
                        min_de_salida2 += [min_de_salida[busqueda_de_trabajador]]
                        del empleados[busqueda_de_trabajador]
                        del trabajo[busqueda_de_trabajador]
                        del hora_de_entrada[busqueda_de_trabajador]
                        del hora_de_salida[busqueda_de_trabajador]
                        del min_de_entrada[busqueda_de_trabajador]
                        del min_de_salida[busqueda_de_trabajador]
                        auto = autos_en_servis.index(auto_para_arreglo)
                        autos_trabajados_servis += [auto_para_arreglo]
                        del autos_en_servis[auto]
                        heramientas[2] -= 1

                    else:
                        print("no hay nadie que pueda realizar el trabajo")

                else:
                    print("el objeto", objeto_2, " no se encuentra en la cadana o en stock\n"
                                                 "nos es imposible hacer el recambio ahora")
                salida = input("algo mas (si/no)\n"
                               ">>>")
                if salida == "si":
                    pass
                else:
                    break
            elif eleccion_3_1 == 2:
                objeto = False
                pintura = int(input("se necesita pintar el auto completo(1) o se necesita retocar la pintura del "
                                    "auto(2)\n "
                                    ">>>"))

                contador = 0
                contador_2 = len(productos)
                while contador_2 > 0:
                    if "pintura" in productos[contador]:
                        para_pago = contador
                        objeto = True
                    else:
                        pass
                    contador += 1
                    contador_2 -= 1
                if objeto:
                    if "pintura" in trabajo:
                        print("veamos quien esta disponible para ahcer el recambio")
                        busqueda_de_trabajador = trabajo.index("pintura")
                        print("tenemos disponibe a", empleados[busqueda_de_trabajador])
                        if pintura == 1:
                            print("el pago sera de", productos[para_pago][1], "dolares")
                        elif pintura == 2:
                            print("el pago sera de", productos[para_pago][1] / 2, "dolares")
                        productos_a_list = list(productos[para_pago])
                        productos_a_list[2] -= 1
                        list_a_prodocto = tuple(productos_a_list)
                        productos[para_pago] = list_a_prodocto
                        empleados2 += [empleados[busqueda_de_trabajador]]
                        trabajo_2 += [trabajo[busqueda_de_trabajador]]
                        hora_de_entrada2 += [hora_de_entrada[busqueda_de_trabajador]]
                        hora_de_salida2 += [hora_de_salida[busqueda_de_trabajador]]
                        min_de_entrada2 += [min_de_entrada[busqueda_de_trabajador]]
                        min_de_salida2 += [min_de_salida[busqueda_de_trabajador]]
                        del empleados[busqueda_de_trabajador]
                        del trabajo[busqueda_de_trabajador]
                        del hora_de_entrada[busqueda_de_trabajador]
                        del hora_de_salida[busqueda_de_trabajador]
                        del min_de_entrada[busqueda_de_trabajador]
                        del min_de_salida[busqueda_de_trabajador]
                        auto = autos_en_servis.index(auto_para_arreglo)
                        autos_trabajados_servis += [auto_para_arreglo]
                        del autos_en_servis[auto]
                        heramientas[2] -= 1

                    else:
                        print("no hay nadie que pueda realizar el trabajo")
                else:
                    print("el objeto pintura no esta disponible no se encuentra en la cadana o en stock\n"
                          "nos es imposible hacer el recambio ahora")
                salida = input("algo mas (si/no)\n"
                               ">>>")
                if salida == "si":
                    pass
                else:
                    break

            elif eleccion_3_1 == -1:
                print("auto no esncontrado")
                salida = input("algo mas (si/no)\n"
                               ">>>")
                if salida == "si":
                    pass
                else:
                    break

    elif eleccion_1 == 4:
        while True:
            print(control_de_empleados())
            elecion_4_1 = int(input(">>>"))
            if elecion_4_1 == 1:  # nombre de los empleados mas profecion
                v4 = len(empleados)
                v4_2 = 0
                while v4 > 0:
                    print(empleados[v4_2], "se especializa en", trabajo[v4_2])
                    v4 -= 1
                    v4_2 += 1
                v4 = len(empleados2)
                v4_2 = 0
                while v4 > 0:
                    print(empleados2[v4_2], "se especializa en", trabajo_2[v4_2])
                    v4 -= 1
                    v4_2 += 1
            elif elecion_4_1 == 2:  # contratar o despedir empleados
                v4 = input("se deve contratar o despedir a un empleado (c/d)\n"
                           ">>>")
                if v4 == "c":
                    nombre = str(input("digame el nombre\n"
                                       ">>>"))
                    especializacion = str(input("y ahora la especializacion del trabajador\n"
                                                ">>>"))
                    print("dime en el siguiente orden el horario de trabajo (hs de entrada, min de entrada, \n"
                          "hs de salida y min de salida). recordar que el hs de trabajo es de 4:00 a 18:00")
                    hse = int(input(">>>"))
                    mine = int(input(">>>"))
                    hss = int(input(">>>"))
                    mins = int(input(">>>"))
                    if hse < 4:
                        print("horario de trbajo no balido")
                    else:
                        if hss > 18 and mins > 0:
                            print("horario de trabajo no baido")
                        else:
                            empleados += [nombre]
                            trabajo += [especializacion]
                            hora_de_entrada += [hse]
                            hora_de_salida += [hss]
                            min_de_entrada += [mine]
                            min_de_salida += [mins]
                elif v4 == "d":
                    print(empleados)
                    eliminar = int(input("eliga la persona que quiere eliminar segun su nª\n"
                                         ">>>"))
                    del empleados[eliminar - 1]
                    del trabajo[eliminar - 1]
                else:
                    pass
            elif elecion_4_1 == 3:  # horario de trabajo
                v4 = len(empleados)
                v4_2 = 0
                while v4 > 0:
                    print(empleados[v4_2], "trabaja desde", hora_de_entrada[v4_2], ":", min_de_entrada[v4_2],
                          "hasta", hora_de_salida[v4_2], ":", min_de_salida[v4_2])
                    v4 -= 1
                    v4_2 += 1
                v4 = len(empleados2)
                v4_2 = 0
                while v4 > 0:
                    print(empleados2[v4_2], "trabaja desde", hora_de_entrada2[v4_2], ":", min_de_entrada2[v4_2],
                          "hasta", hora_de_salida2[v4_2], ":", min_de_salida2[v4_2])
                    v4 -= 1
                    v4_2 += 1
            elif elecion_4_1 == 4:  # pago por hs trabajadas
                print("para no molestar a quienes realizan una actividad solo contaremos con los empleados desocupados")
                v4 = len(empleados)
                v4_2 = 0
                while v4 > 0:
                    print(empleados[v4_2], "por las horas trabajadas gana",
                          gnancia_por_hora * (hora_de_salida[v4_2] - hora_de_entrada[v4_2]), "dolares")
                    v4 -= 1
                    v4_2 += 1
                print(empleados)
                trabajo_demas = input("hizo horas extra (si/no)")
                if trabajo_demas == "si":
                    cadena_de_trabajadores = []
                    print(empleados)
                    v4_2 = len(trabajo) - 1
                    while True:
                        hs_extra = int(input("quien hzo hs extra (ingrsar de uno a la vez e ingresar por nª)"))
                        cadena_de_trabajadores += [hs_extra - 1]
                        alguien_mas = input("alguien mas (si/no)")
                        if alguien_mas == "si":
                            pass
                        else:
                            break
                    pago_por_hs_extra = len(cadena_de_trabajadores)
                    pago_por_hs_extra_2 = 0
                    while pago_por_hs_extra > 0:
                        print(empleados[cadena_de_trabajadores[pago_por_hs_extra_2]],
                              "cuantos minutos mas trabajo")
                        minutos_extra = int(input(">>>"))
                        print(empleados[cadena_de_trabajadores[pago_por_hs_extra_2]], "gana",
                              ganancia_por_min * minutos_extra, "de las horas extra")
                        pago_por_hs_extra -= 1
                        pago_por_hs_extra_2 += 1

                else:
                    pass
            salida = input("algo mas (si/no)\n"
                           ">>>")
            if salida == "si":
                pass
            else:
                break

    elif eleccion_1 == 5:
        while True:
            print(gestionar_autos_en_espera())
            eleccion_5_1 = int(input(">>>"))
            if eleccion_5_1 == 1:
                if espacio_de_estacionamiento == 0:
                    print("no hay espacio")
                else:
                    print(autos_en_estacionamiento)
                    auto_nuevo = input("escribir patente del auto\n"
                                       ">>>")
                    if auto_nuevo in autos_en_estacionamiento or auto_nuevo in autos_en_taller or auto_nuevo in \
                            autos_en_servis:
                        print("el auto no puede registrase")
                    else:
                        autos_en_estacionamiento += [auto_nuevo]
                        espacio_de_estacionamiento -= 1
                salida = input("algo mas (si/no)\n"
                               ">>>")
                if salida == "si":
                    pass
                else:
                    break

            elif eleccion_5_1 == 2:
                if espacio_de_taller == 0:
                    print("no hay espacio")
                    s_n = input("quieres guardarlo en estacinonamiento (si/no)\n"
                                ">>>")
                    if s_n == "si":
                        if espacio_de_estacionamiento == 0:
                            print("no hay espacio")
                        else:
                            print(autos_en_estacionamiento)
                            auto_nuevo = input("escribir patente del auto\n"
                                               ">>>")
                            if auto_nuevo in autos_en_estacionamiento or auto_nuevo in autos_en_taller \
                                    or auto_nuevo in autos_en_servis:
                                print("el auto no puede registrase")
                            else:
                                autos_en_estacionamiento += [auto_nuevo]
                                espacio_de_estacionamiento -= 1
                else:
                    print(autos_en_taller)
                    auto_nuevo = input("escribir patente del auto\n"
                                       ">>>")
                    if auto_nuevo in autos_en_estacionamiento or auto_nuevo in autos_en_taller or auto_nuevo in \
                            autos_en_servis:
                        print("el auto no puede registrase")
                    else:
                        autos_en_taller += [auto_nuevo]
                        espacio_de_taller -= 1
                salida = input("algo mas (si/no)\n"
                               ">>>")
                if salida == "si":
                    pass
                else:
                    break
            elif eleccion_5_1 == 3:
                if espacio_de_servis == 0:
                    print("no hay espacio")
                    s_n = input("quieres guardarlo en estacinonamiento (si/no)\n"
                                ">>>")
                    if s_n == "si":
                        if espacio_de_estacionamiento == 0:
                            print("no hay espacio")
                        else:
                            print(autos_en_estacionamiento)
                            auto_nuevo = input("escribir patente del auto\n"
                                               ">>>")
                            if auto_nuevo in autos_en_estacionamiento or auto_nuevo in autos_en_taller \
                                    or auto_nuevo in autos_en_servis:
                                print("el auto no puede registrase")
                            else:
                                autos_en_estacionamiento += [auto_nuevo]
                                espacio_de_estacionamiento -= 1
                else:
                    print(autos_en_servis)
                    auto_nuevo = input("escribir patente del auto\n"
                                       ">>>")
                    if auto_nuevo in autos_en_estacionamiento or auto_nuevo in autos_en_taller or auto_nuevo in \
                            autos_en_servis:
                        print("el auto no puede registrase")
                    else:
                        autos_en_servis += [auto_nuevo]
                        espacio_de_servis -= 1
                salida = input("algo mas (si/no)\n"
                               ">>>")
                if salida == "si":
                    pass
                else:
                    break
            elif eleccion_5_1 == 4:
                if espacio_de_taller == 0:
                    print("no hay espacio")
                else:
                    print(autos_en_estacionamiento)
                    cambio = input("escribe el auto a mover\n"
                                   ">>>")
                    if cambio in autos_en_estacionamiento:
                        autos_en_taller += [cambio]
                        espacio_de_taller -= 1
                        auto_movido = autos_en_estacionamiento.index(cambio)
                        del autos_en_estacionamiento[auto_movido]
                        espacio_de_estacionamiento += 1
                salida = input("algo mas (si/no)\n"
                               ">>>")
                if salida == "si":
                    pass
                else:
                    break
            elif eleccion_5_1 == 5:
                if espacio_de_servis == 0:
                    print("no hay espacio")
                else:
                    print(autos_en_estacionamiento)
                    cambio = input("escribe el auto a mover\n"
                                   ">>>")
                    if cambio in autos_en_estacionamiento:
                        autos_en_servis += [cambio]
                        espacio_de_servis -= 1
                        auto_movido = autos_en_estacionamiento.index(cambio)
                        del autos_en_estacionamiento[auto_movido]
                        espacio_de_estacionamiento += 1
                salida = input("algo mas (si/no)\n"
                               ">>>")
                if salida == "si":
                    pass
                else:
                    break

    elif eleccion_1 == 6:
        while True:
            print(chequeo_de_autos_antes_de_la_entrega())
            eleccion_6_1 = int(input(">>>"))

            if eleccion_6_1 == 1:
                print(autos_trabajados)
                patente = input("selecciona el auto\n"
                                ">>>")
                if patente in autos_trabajados:
                    print("auto retirado con exito")
                    auto = autos_trabajados.index(patente)
                    espacio_de_taller += 1
                    del autos_trabajados[auto]
                    empleados += [empleados2[auto]]
                    trabajo += [trabajo_2[auto]]
                    hora_de_entrada += [hora_de_entrada2[auto]]
                    hora_de_salida += [hora_de_salida2[auto]]
                    min_de_entrada += [min_de_entrada2[auto]]
                    min_de_salida += [min_de_salida2[auto]]
                    del empleados2[auto]
                    del trabajo_2[auto]
                    del hora_de_entrada2[auto]
                    del hora_de_salida2[auto]
                    del min_de_entrada2[auto]
                    del min_de_salida2[auto]
                    heramientas[2] += 1

                else:
                    print("auto no registrado")
                salida = input("algo mas (si/no)\n"
                               ">>>")
                if salida == "si":
                    pass
                else:
                    break
            if eleccion_6_1 == 2:
                print(autos_trabajados_servis)
                patente = input("selecciona el auto\n"
                                ">>>")
                if patente in autos_trabajados_servis:
                    print("auto retirado con exito")
                    auto = autos_trabajados_servis.index(patente)
                    espacio_de_servis += 1
                    del autos_trabajados_servis[auto]
                    empleados += [empleados2[auto]]
                    trabajo += [trabajo_2[auto]]
                    hora_de_entrada += [hora_de_entrada2[auto]]
                    hora_de_salida += [hora_de_salida2[auto]]
                    min_de_entrada += [min_de_entrada2[auto]]
                    min_de_salida += [min_de_salida2[auto]]
                    del empleados2[auto]
                    del trabajo_2[auto]
                    del hora_de_entrada2[auto]
                    del hora_de_salida2[auto]
                    del min_de_entrada2[auto]
                    del min_de_salida2[auto]
                    heramientas[2] += 1
                else:
                    print("auto no registrado")
                salida = input("algo mas (si/no)\n"
                               ">>>")
                if salida == "si":
                    pass
                else:
                    break

    elif eleccion_1 == 7:
        while True:
            print(mostrar_lista_de_veiculos())
            eleccion_7_1 = int(input(">>>"))
            if eleccion_7_1 == 1:
                print(autos_en_estacionamiento)
            elif eleccion_7_1 == 2:
                print(autos_en_taller)
                print(autos_trabajados)
            elif eleccion_7_1 == 3:
                print(autos_en_servis)
                print(autos_trabajados_servis)
            salida = input("algo mas (si/no)\n"
                           ">>>")
            if salida == "si":
                pass
            else:
                break

    elif eleccion_1 == 8:
        print(Fore.RED + "entendido\n"
                         "finalizando la secion")
        for i in tqdm(range(10)):
            sleep(1)
        break

    else:
        print("eleccion no valida")
