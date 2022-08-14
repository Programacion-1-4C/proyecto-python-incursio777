import webbrowser as web
from def_taller_mecanico import menu_principal
from def_taller_mecanico import reparacion_del_veiculo
from def_taller_mecanico import repuestos_y_objetos
from def_taller_mecanico import servis
from def_taller_mecanico import control_de_empleados
from def_taller_mecanico import gestionar_autos_en_espera
from def_taller_mecanico import chequeo_de_autos_antes_de_la_entrega
from def_taller_mecanico import mostrar_lista_de_veiculos

# variavles de eleccion 2 venta
productos = [("motor", 4000, 30), ("electro", 14, 20), ("bateria", 20, 40)]

# variables de eleccion 4 empleados
empleados = ["Tomas", "Lucas", "Martin"]
trabajo = ["bareia", "motor", "electro"]
hora_de_entrada = [4, 10, 5]
hora_de_salida = [12, 18, 13]
min_de_entrada = [30, 15, 0]
min_de_salida = [30, 15, 0]
gnancia_por_hora = 6.4
ganancia_por_min = 0.1
#todo lo que este en esta linea sera solo de almacenamiento de informacion
    #todo lo de esta seran if/elif de la eleccion pricipal
        #todo lo de esta seran while para repetir las opciones
            #finalmente esta seran if/elif para una sub eleccion
while True:
    print(menu_principal())
    eleccion_1 = int(input(">>>"))

    if eleccion_1 == 1:
        print(reparacion_del_veiculo())
        eleccion_1_1 = int(input(">>>"))



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
                    print(sorted(productos, key=lambda objeto: objeto[0]))
                elif orden == 2:
                    print("ordenado de la Z a la A")
                    print(sorted(productos, key=lambda objeto: objeto[0], reverse=True))
                elif orden == 3:
                    print("ordenado del stock + a -")
                    print(sorted(productos, key=lambda objeto: objeto[1]))
                elif orden == 4:
                    print("ordenado del stock - a +")
                    print(sorted(productos, key=lambda objeto: objeto[1], reverse=True))
                elif orden == 5:
                    print("ordenado del precio + a -")
                    print(sorted(productos, key=lambda objeto: objeto[2]))
                elif orden == 6:
                    print("ordenado del precio - a +")
                    print(sorted(productos, key=lambda objeto: objeto[2], reverse=True))
            if eleccion_2_1 == 2:  # agragar productos y sacarlos del mercado
                A_o_S = input("queires agregar o sacar productos (a/s)")
                if A_o_S == "a":
                    producto_nuevo = input("que producto nuevo sera")
                    stock_nuevo = int(input("cual es el stonk del producto"))
                    if stock_nuevo < 0:
                        print("secuencia imbalida")
                        break
                    precio_nuevo = int(input("cual es el procio"))
                    if precio_nuevo < 0:
                        print("secuencia imbalida")
                        break
                    productos.append((producto_nuevo, stock_nuevo, precio_nuevo))
                    print(productos)
                if A_o_S == "s":
                    print(productos)
                    eliminar = int(input("decide que producto vas a eliminar definitivamente (seleccionar por nª)"))
                    del productos[eliminar - 1]
                    print(productos)
            if eleccion_2_1 == 3:  # rellenar stock de un producto
                print("selecciona cual de los siguientes productos tienen nuevo stonk\n",
                      productos)
                cadena_de_stonk = []
                while True:
                    stock_nuevo = int(input(">>>"))
                    cadena_de_stonk += [stock_nuevo - 1]
                    algo_mas = input("algo mas (si/no)")
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
                    productos_a_list= list(productos[cadena_de_stonk[contador]])
                    productos_a_list[2] += stock_nuevo
                    list_a_prodocto=tuple(productos_a_list)
                    productos[cadena_de_stonk[contador]] = list_a_prodocto
                    nuevo_stonk -= 1
                    contador += 1
            if eleccion_2_1 == 4:  # reventa de productos
                print("selecciona cual de los siguientes productos van en el encargo\n",
                      productos)
                cadena_de_stonk = []
                while True:
                    stock_nuevo = int(input(">>>"))
                    cadena_de_stonk += [stock_nuevo - 1]
                    algo_mas = input("algo mas (si/no)")
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
                    productos_a_list[2] -= stock_nuevo
                    list_a_prodocto = tuple(productos_a_list)
                    productos[cadena_de_stonk[contador]] = list_a_prodocto
                    nuevo_stonk -= 1
                    contador += 1
            if eleccion_2_1 == 5:
                print("selecciona cual de los siguientes productos cambiaran su precio\n",
                      productos)
                cadena_de_precios = []
                while True:
                    precio_nuevo = int(input(">>>"))
                    cadena_de_precios += [precio_nuevo - 1]
                    algo_mas = input("algo mas (si/no)")
                    if algo_mas == "si":
                        pass
                    else:
                        break
                nuevo_precio = len(cadena_de_precios)
                contador = 0
                while nuevo_precio > 0:
                    print(productos[cadena_de_precios[contador]][0],
                          "cuantos productos nuevos llegron")
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
            salida = input("algo mas (si/no)\n"
                           ">>>")
            if salida == "si":
                pass
            else:
                break

    elif eleccion_1 == 3:
        print(servis())
        eleccion_3_1 = int(input(">>>"))



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
            elif elecion_4_1 == 4:  # pago por hs trabajadas
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
        print(gestionar_autos_en_espera())
        eleccion_5_1 = int(input(">>>"))



    elif eleccion_1 == 6:
        print(chequeo_de_autos_antes_de_la_entrega())
        eleccion_6_1 = int(input(">>>"))



    elif eleccion_1 == 7:
        print(mostrar_lista_de_veiculos())
        eleccion_7_1 = int(input(">>>"))



    elif eleccion_1 == 8:
        print("entendido\n"
              "finalizando la secion")
        break
    else:
        print("eleccion no valida")
