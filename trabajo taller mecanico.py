from def_taller_mecanico import menu_principal
from def_taller_mecanico import reparacion_del_veiculo
from def_taller_mecanico import repuestos_y_objetos
from def_taller_mecanico import servis
from def_taller_mecanico import control_de_empleados
from def_taller_mecanico import gestionar_autos_en_espera
from def_taller_mecanico import chequeo_de_autos_antes_de_la_entrega
from def_taller_mecanico import mostrar_lista_de_veiculos

# variables de eleccion 4 mecanico
empleados = ["Tomas", "Lucas", "Martin"]
trabajo = ["bareia", "motor", "electro"]
hora_de_entrada = [4, 10, 5]
hora_de_salida = [12, 18, 13]
min_de_entrada = [30, 15, 0]
min_de_salida = [30, 15, 0]
gnancia_por_hora = 200
ganancia_por_min = 5
variable_inutil = True
while variable_inutil:
    print(menu_principal())
    eleccion_1 = int(input(">>>"))



    if eleccion_1 == 1:
        print(reparacion_del_veiculo())
        eleccion_1_1 = int(input(">>>"))



    elif eleccion_1 == 2:
        print(repuestos_y_objetos())
        eleccion_2_1 = int(input(">>>"))



    elif eleccion_1 == 3:
        print(servis())
        eleccion_3_1 = int(input(">>>"))



    elif eleccion_1 == 4:
        while variable_inutil:
            print(control_de_empleados())
            elecion_4_1 = int(input(">>>"))
            if elecion_4_1 == 1:  # nombre de los empleados mas profecion
                v4 = len(empleados)
                v4_2 = 0
                while v4 > 0:
                    print(empleados[v4_2], "se especializa en", trabajo[v4_2])
                    v4 -= 1
                    v4_2 += 1
                salida = input("quiere continuar con control de empleados (si/no)\n"
                               ">>>")
                if salida == "si":
                    pass
                else:
                    break
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
                else:
                    print(empleados)
                    v4_2 = len(trabajo) - 1
                    eliminar = int(input("eliga la persona que quiere eliminar segun su nª\n"
                                         ">>>"))
                    del empleados[eliminar]
                    del trabajo[eliminar]
                salida = input("quiere continuar con control de empleados (si/no)\n"
                               ">>>")
                if salida == "si":
                    pass
                else:
                    break
            elif elecion_4_1 == 3:  # horario de trabajo
                v4 = len(empleados)
                v4_2 = 0
                while v4 > 0:
                    print(empleados[v4_2], "trabaja desde", hora_de_entrada[v4_2], ":", min_de_entrada[v4_2],
                          "hasta", hora_de_salida[v4_2], ":", min_de_salida[v4_2])
                    v4 -= 1
                    v4_2 += 1
                salida = input("quiere continuar con control de empleados (si/no)\n"
                               ">>>")
                if salida == "si":
                    pass
                else:
                    break
            elif elecion_4_1 == 4:  # pago por hs trabajadas
                v4 = len(empleados)
                v4_2 = 0
                while v4 > 0:
                    print(empleados[v4_2], "por las horas trabajadas gana",
                          gnancia_por_hora * (hora_de_salida[v4_2] - hora_de_entrada[v4_2]), "pesos")
                    v4 -= 1
                    v4_2 += 1
                print(empleados)
                trabajo_demas = input("hizo horas extra (si/no)")
                if trabajo_demas == "si":
                    cadena_de_trabajadores = []
                    print(empleados)
                    v4_2 = len(trabajo) - 1
                    variable_inutil_2 = True
                    while variable_inutil_2:
                        hs_extra = int(input("quien hzo hs extra (ingrsar de uno a la vez e ingresar por nª)"))
                        cadena_de_trabajadores += [hs_extra - 1]
                        alguien_mas = input("alguien mas (si/no)")
                        if alguien_mas == "si":
                            pass
                        else:
                            variable_inutil_2 = False
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

                salida = input("quiere continuar con control de empleados (si/no)\n"
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
