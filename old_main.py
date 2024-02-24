from flask import Flask
from flask import render_template
import form
from flask import request

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    datos_form = form.CommentForm(request.form)
    # valores por defecto
    _dm = ""
    _varianza = ""
    _media = ""
    _rango = ""
    _amplitud_de_clase = ""
    
    
    # se crea el diccionario que se enviara al index
    mi_diccionario = {}
    
    if request.method == 'POST' and datos_form.validate():
        print(datos_form.datos.data)
        print(datos_form.punto.data)
        
        
        
        
        
        
        
        
        
        # ------------------- AQUI EMPIEZA EL PROGRAMA --------------------------
        obtencion = datos_form.datos.data
        obtencion = ' '.join(obtencion.split())
        obtencion = ' '.join(obtencion.split(','))
        decimales_despues_del_punto = datos_form.punto.data
        
        if obtencion != '' and decimales_despues_del_punto != '':
        
            # creando el diccionario con los datos

            print('')
            print('asi queda la string sin repeticiones de comas o espacios', obtencion)

            #ordenación, verificacion y reemplazo de espacios

            if ',' not in obtencion:
                lista = obtencion.split(' ')

            else:
                lista = obtencion.split(',')

            lista = list(filter(bool, lista))
            lista = [float(elemento) for elemento in lista]

            lista.sort()

            #impresion de la lista ordenada
            print('así queda la lista ordenada: ',lista)

            print('')

            #definición de decimales despues de punto y unidades minimas

            no_de_datos = len(lista)
            mitad_de_datos = no_de_datos / 2

            decimales_despues_del_punto = int(decimales_despues_del_punto)

            if decimales_despues_del_punto == 0:
                unidad_min = 1

            else:
                cantidad_ceros = int(decimales_despues_del_punto)
                cantidad_ceros_menos_uno = cantidad_ceros - 1
                ceros = '0' * cantidad_ceros_menos_uno
                unidad_min_en_cadena = f'0.{ceros}1'
                
                unidad_min = float(unidad_min_en_cadena)


            #A,K y R
            #R
            R = round(lista[no_de_datos - 1] - lista[0],3)

            #K
            from math import log10
            logaritmo = round(log10(no_de_datos),3)
            K = round(3.32 * logaritmo + 1)

            #A
            A = R / K

            if A < 1:
                decimales_despues_del_punto = decimales_despues_del_punto + 1
                A = round(R/K,decimales_despues_del_punto)
                decimales_para_LR = decimales_despues_del_punto + 1
                
                cantidad_ceros = int(decimales_despues_del_punto)
                cantidad_ceros_menos_uno = cantidad_ceros - 1
                ceros = '0' * cantidad_ceros_menos_uno
                unidad_min_en_cadena = f'0.{ceros}1'
                
                unidad_min = float(unidad_min_en_cadena)
                
            else:
                A = round(R/K,decimales_despues_del_punto)
                decimales_para_LR = decimales_despues_del_punto + 1

            print('rango=',R)
            print('numero de clases=',K)
            print('amplitud=',A)
            print('numero de datos=', no_de_datos)

            
            clase1 = []
            
            #limites, marcas de clase y frecuencias
            LI1 = lista[0]
            #   print('limite inferior1: ', LI1)

            LS1 = round(A + LI1 - unidad_min,decimales_despues_del_punto)
            #   print('limite superior 1: ',LS1)

            numeradorLRI1 = round(LS1 - A + LI1,decimales_despues_del_punto)
            LRI1 = round(numeradorLRI1 / 2,decimales_para_LR)
            #   print('limite real inferior 1: ',LRI1)

            numeradorLRS1 = round(LS1 + LI1 + A,decimales_despues_del_punto) 
            LRS1 = round(numeradorLRS1 / 2,decimales_para_LR)
            #   print('limite real superior 1: ',LRS1)

            numeradorXi1 = round(LRI1 + LRS1,decimales_despues_del_punto)
            Xi_1 = round(numeradorXi1 / 2,decimales_para_LR)
            #   print('marca de clase 1: ',Xi_1)

            #definición de frecuencias de clase 1
            datos_de_clase1 = []

            for num in lista:
                if num > LRI1 and num < LRS1:
                    datos_de_clase1.append(num)
            f1 = len(datos_de_clase1)

            h1 = round((f1 / no_de_datos) * 100,2)

            F1 = f1

            H1 = h1

            x1 = round(Xi_1 * f1,decimales_para_LR)


            #impresion de los datos de la clase 1
            print('---datos de la clase 1---')
            print('LI-1= ',LI1)
            print('LS-1= ',LS1)
            print('LRI-1= ',LRI1)
            print('LRS-1= ',LRS1)
            print('Xi-1= ',Xi_1)
            print('f-1= ',f1)
            print('h-1= ',h1)
            print('F-1= ',F1)
            print('H-1= ',H1)
            print(f'Xi * fi -1= {x1}')
            
            
            

            if LRS1 >= lista[no_de_datos - 1] :
                media = round(Xi_1  / no_de_datos,decimales_despues_del_punto)
                
            
            else: 
                
                clase2 = []
                
                LI2 = round(LI1 + A,decimales_despues_del_punto)
                #   print('limite inferior 2: ',LI2)

                LS2 = round(LS1 + A,decimales_despues_del_punto)
                #   print('limite superior 2: ',LS2)
                
                numeradorLRI2 = round(LS2 - A + LI2,decimales_despues_del_punto)
                LRI2 = round(numeradorLRI2 / 2,decimales_para_LR)
                #   print('limite real inferior 2: ',LRI2)
                
                numeradorLRS2 = round(LS2 + LI2 + A,decimales_despues_del_punto) 
                LRS2 = round(numeradorLRS2 / 2,decimales_para_LR)
                #   print('limite real superior 2: ',LRS2)
                
                numeradorXi2 = round(LRI2 + LRS2,decimales_despues_del_punto)
                Xi_2 = round(numeradorXi2 / 2,decimales_para_LR)
                #   print('marca de clase 2: ',Xi_2)
                
                #definición de frecuencias de clase 2
                datos_de_clase2 = []

                for num in lista:
                    if num > LRI2 and num < LRS2:
                        datos_de_clase2.append(num)
                f2 = len(datos_de_clase2)
                
                h2 = round(f2 / no_de_datos * 100,2)
                
                F2 = f1 + f2
                
                H2 = round(F2 / no_de_datos * 100,2)
                
                x2 = round(Xi_2 * f2,decimales_para_LR)
                
                #impresión de los datos de la clase 2
                print('---datos de la clase 2---')
                print('LI-2= ',LI2)
                print('LS-2= ',LS2)
                print('LRI-2= ',LRI2)
                print('LRS-2= ',LRS2)
                print('Xi-2= ',Xi_2)
                print('f-2= ',f2)
                print('h-2= ',h2)
                print('F-2= ',F2)
                print('H-2= ',H2)
                print(f'Xi * fi -2= {x2}')
                
                
                
                if LRS2 >= lista[no_de_datos - 1] :
                    X = Xi_1 + Xi_2
                    media = round(X / no_de_datos,decimales_para_LR)
            
                else:
                    
                    clase3 = []
                    
                    LI3 = round(LI2 + A,decimales_despues_del_punto)
                    #   print('limite inferior 3: ',LI3)

                    LS3 = round(LS2 + A,decimales_despues_del_punto)
                    #   print('limite superior 3: ',LS3)
                    
                    numeradorLRI3 = round(LS3 - A + LI3,decimales_despues_del_punto)
                    LRI3 = round(numeradorLRI3 / 2,decimales_para_LR)
                    #   print('limite real inferior 3: ',LRI3)
                    
                    numeradorLRS3 = round(LS3 + LI3 + A,decimales_despues_del_punto) 
                    LRS3 = round(numeradorLRS3 / 2,decimales_para_LR)
                    #   print('limite real superior 3: ',LRS3)
                    
                    numeradorXi3 = round(LRI3 + LRS3,decimales_despues_del_punto)
                    Xi_3 = round(numeradorXi3 / 2,decimales_para_LR)
                    #   print('marca de clase 3: ',Xi_3)
                    
                    #definición de frecuencias de clase 3
                    
                    datos_de_clase3 = []

                    for num in lista:
                        if num > LRI3 and num < LRS3:
                            datos_de_clase3.append(num)
                    f3 = len(datos_de_clase3)
                    
                    h3 = round(f3 / no_de_datos * 100,2)
                    
                    F3 = f1 + f2 + f3
                    
                    H3 = round(F3 / no_de_datos * 100,2)
                    
                    x3 = round(Xi_3 * f3,decimales_para_LR)
                    
                    #impresión de los datos de la clase 3
                    print('---datos de la clase 3---')
                    print('LI-3= ',LI3)
                    print('LS-3= ',LS3)
                    print('LRI-3= ',LRI3)
                    print('LRS-3= ',LRS3)
                    print('Xi-3= ',Xi_3)
                    print('f-3= ',f3)
                    print('h-3= ',h3)
                    print('F-3= ',F3)
                    print('H-3= ',H3)
                    print(f'Xi * fi -3= {x3}')
                    
                    if LRS3 >= lista[no_de_datos - 1] :
                        X = Xi_1 + Xi_2 + Xi_3
                        media = round(X / no_de_datos,decimales_para_LR)

                    else:
                        
                        clase4 = []
                        
                        LI4 = round(LI3 + A,decimales_despues_del_punto)
                        #   print('limite inferior 4: ',LI4)

                        LS4 = round(LS3 + A,decimales_despues_del_punto)
                        #   print('limite superior 4: ',LS4)
                        
                        numeradorLRI4 = round(LS4 - A + LI4,decimales_despues_del_punto)
                        LRI4 = round(numeradorLRI4 / 2,decimales_para_LR)
                        #   print('limite real inferior 4: ',LRI4)
                        
                        numeradorLRS4 = round(LS4 + LI4 + A,decimales_despues_del_punto) 
                        LRS4 = round(numeradorLRS4 / 2,decimales_para_LR)
                        #   print('limite real superior 4: ',LRS4)
                        
                        numeradorXi4 = round(LRI4 + LRS4,decimales_despues_del_punto)
                        Xi_4 = round(numeradorXi4 / 2,decimales_para_LR)
                        #   print('marca de clase 4: ',Xi_4)
                        
                        #definición de frecuencias de clase 4
                        datos_de_clase4 = []

                        for num in lista:
                            if num > LRI4 and num < LRS4:
                                datos_de_clase4.append(num)
                        f4 = len(datos_de_clase4)
                        
                        h4 = round(f4 / no_de_datos * 100,2)
                        
                        F4 = f1 + f2 + f3 + f4
                        
                        H4 = round(F4 / no_de_datos * 100,2)
                        
                        x4 = round(Xi_4 * f4,decimales_para_LR)
                        
                        #impresión de los datos de la clase 4
                        print('---datos de la clase 4---')
                        print('LI-4= ',LI4)
                        print('LS-4= ',LS4)
                        print('LRI-4= ',LRI4)
                        print('LRS-4= ',LRS4)
                        print('Xi-4= ',Xi_4)
                        print('f-4= ',f4)
                        print('h-4= ',h4)
                        print('F-4= ',F4)
                        print('H-4= ',H4)
                        print(f'Xi * fi -4= {x4}')
                        
                        if LRS4 >= lista[no_de_datos - 1] :
                            X = Xi_1 + Xi_2 + Xi_3 + Xi_4
                            media = round(X / no_de_datos,decimales_para_LR)
                    
                        else:
                            
                            clase5 = []
                            
                            LI5 = round(LI4 + A,decimales_despues_del_punto)
                            #   print('limite inferior 5: ',LI5)

                            LS5 = round(LS4 + A,decimales_despues_del_punto)
                            #   print('limite superior 5: ',LS5)
                            
                            numeradorLRI5 = round(LS5 - A + LI5,decimales_despues_del_punto)
                            LRI5 = round(numeradorLRI5 / 2,decimales_para_LR)
                            #   print('limite real inferior 5: ',LRI5)
                            
                            numeradorLRS5 = round(LS5 + LI5 + A,decimales_despues_del_punto) 
                            LRS5 = round(numeradorLRS5 / 2,decimales_para_LR)
                            #   print('limite real superior 5: ',LRS5)
                            
                            numeradorXi5 = round(LRI5 + LRS5,decimales_despues_del_punto)
                            Xi_5 = round(numeradorXi5 / 2,decimales_para_LR)
                            #   print('marca de clase 5: ',Xi_5)
                            
                            #definición de frecuencias de clase 5
                            datos_de_clase5 = []

                            for num in lista:
                                if num > LRI5 and num < LRS5:
                                    datos_de_clase5.append(num)
                            f5 = len(datos_de_clase5)
                            
                            h5 = round(f5 / no_de_datos * 100,2)
                            
                            F5 = f1 + f2 + f3 + f4 + f5
                            
                            H5 = round(F5 / no_de_datos * 100,2)
                            
                            x5 = round(Xi_5 * f5,decimales_para_LR)
                            
                            #impresión de los datos de la clase 5
                            print('---datos de la clase 5---')
                            print('LI-5= ',LI5)
                            print('LS-5= ',LS5)
                            print('LRI-5= ',LRI5)
                            print('LRS-5= ',LRS5)
                            print('Xi-5= ',Xi_5)
                            print('f-5= ',f5)
                            print('h-5= ',h5)
                            print('F-5= ',F5)
                            print('H-5= ',H5)
                            print(f'Xi * fi -5= {x5}')
                            
                            if LRS5 >= lista[no_de_datos - 1] :
                                X = Xi_1 + Xi_2 + Xi_3 + Xi_4 + Xi_5
                                media = round(X / no_de_datos,decimales_para_LR)
                        
                            else:
                                
                                clase6 = []
                                
                                LI6 = round(LI5 + A,decimales_despues_del_punto)
                                #   print('limite inferior 6: ',LI6)

                                LS6 = round(LS5 + A,decimales_despues_del_punto)
                                #   print('limite superior 6: ',LS6)
                                
                                numeradorLRI6 = round(LS6 - A + LI6,decimales_despues_del_punto)
                                LRI6 = round(numeradorLRI6 / 2,decimales_para_LR)
                                #   print('limite real inferior 6: ',LRI6)
                                
                                numeradorLRS6 = round(LS6 + LI6 + A,decimales_despues_del_punto) 
                                LRS6 = round(numeradorLRS6 / 2,decimales_para_LR)
                                #   print('limite real superior 6: ',LRS6)
                                
                                numeradorXi6 = round(LRI6 + LRS6,decimales_despues_del_punto)
                                Xi_6 = round(numeradorXi6 / 2,decimales_para_LR)
                                #   print('marca de clase 6: ',Xi_6)
                                
                                #definición de frecuencias de clase 6
                                datos_de_clase6 = []

                                for num in lista:
                                    if num > LRI6 and num < LRS6:
                                        datos_de_clase6.append(num)
                                f6 = len(datos_de_clase6)
                                
                                h6 = round(f6 / no_de_datos * 100,2)
                                
                                F6 = f1 + f2 + f3 + f4 + f5 + f6
                                
                                H6 = round(F6 / no_de_datos * 100,2)
                                
                                x6 = round(Xi_6 * f6,decimales_para_LR)
                                
                                #impresión de los datos de la clase 6
                                print('---datos de la clase 6---')
                                print('LI-6= ',LI6)
                                print('LS-6= ',LS6)
                                print('LRI-6= ',LRI6)
                                print('LRS-6= ',LRS6)
                                print('Xi-6= ',Xi_6)
                                print('f-6= ',f6)
                                print('h-6= ',h6)
                                print('F-6= ',F6)
                                print('H-6= ',H6)
                                print(f'Xi * fi -6= {x6}')
                                
                                if LRS6 >= lista[no_de_datos - 1] :
                                    X = Xi_1 + Xi_2 + Xi_3 + Xi_4 + Xi_5 + Xi_6
                                    media = round(X / no_de_datos,decimales_para_LR)
                            
                                else:
                                    
                                    clase7 = []
                                    
                                    LI7 = round(LI6 + A,decimales_despues_del_punto)
                                    #   print('limite inferior 7: ',LI7)

                                    LS7 = round(LS6 + A,decimales_despues_del_punto)
                                    #   print('limite superior 7: ',LS7)
                                    
                                    numeradorLRI7 = round(LS7 - A + LI7,decimales_despues_del_punto)
                                    LRI7 = round(numeradorLRI7 / 2,decimales_para_LR)
                                    #   print('limite real inferior 7: ',LRI7)
                                    
                                    numeradorLRS7 = round(LS7 + LI7 + A,decimales_despues_del_punto) 
                                    LRS7 = round(numeradorLRS7 / 2,decimales_para_LR)
                                    #   print('limite real superior 7: ',LRS7)
                                    
                                    numeradorXi7 = round(LRI7 + LRS7,decimales_despues_del_punto)
                                    Xi_7 = round(numeradorXi7 / 2,decimales_para_LR)
                                    #   print('marca de clase 7: ',Xi_7)

                                    #definición de frecuencias de clase 7
                                    datos_de_clase7 = []

                                    for num in lista:
                                        if num > LRI7 and num < LRS7:
                                            datos_de_clase7.append(num)
                                    f7 = len(datos_de_clase7)
                                    
                                    h7 = round(f7 / no_de_datos * 100,2)
                                    
                                    F7 = f1 + f2 + f3 + f4 + f5 + f6 + f7
                                    
                                    H7 = round(F7 / no_de_datos * 100,2)
                                    
                                    x7 = round(Xi_7 * f7,decimales_para_LR)
                                    
                                    #impresión de los datos de la clase 7
                                    print('---datos de la clase 7---')
                                    print('LI-7= ',LI7)
                                    print('LS-7= ',LS7)
                                    print('LRI-7= ',LRI7)
                                    print('LRS-7= ',LRS7)
                                    print('Xi-7= ',Xi_7)
                                    print('f-7= ',f7)
                                    print('h-7= ',h7)
                                    print('F-7= ',F7)
                                    print('H-7= ',H7)
                                    print(f'Xi * fi -7= {x7}')
                                    
                                    if LRS7 >= lista[no_de_datos - 1] :
                                        X = Xi_1 + Xi_2 + Xi_3 + Xi_4 + Xi_5 + Xi_6 + Xi_7
                                        media = round(X / no_de_datos,decimales_para_LR)
                                
                                    else:
                                        
                                        clase8 = []
                                        
                                        LI8 = round(LI7 + A,decimales_despues_del_punto)
                                        #   print('limite inferior 8: ',LI8)

                                        LS8 = round(LS7 + A,decimales_despues_del_punto)
                                        #   print('limite superior 8: ',LS8)
                                        
                                        numeradorLRI8 = round(LS8 - A + LI8,decimales_despues_del_punto)
                                        LRI8 = round(numeradorLRI8 / 2,decimales_para_LR)
                                        #   print('limite real inferior 8: ',LRI8)
                                        
                                        numeradorLRS8 = round(LS8 + LI8 + A,decimales_despues_del_punto) 
                                        LRS8 = round(numeradorLRS8 / 2,decimales_para_LR)
                                        #   print('limite real superior 8: ',LRS8)
                                        
                                        numeradorXi8 = round(LRI8 + LRS8,decimales_despues_del_punto)
                                        Xi_8 = round(numeradorXi8 / 2,decimales_para_LR)
                                        #   print('marca de clase 8: ',Xi_8)
                                        
                                        #definición de frecuencias de clase 8
                                        datos_de_clase8 = []

                                        for num in lista:
                                            if num > LRI8 and num < LRS8:
                                                datos_de_clase8.append(num)
                                        f8 = len(datos_de_clase8)
                                        
                                        h8 = round(f8 / no_de_datos * 100,2)
                                        
                                        F8 = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8
                                        
                                        H8 = round(F8 / no_de_datos * 100,2)
                                        
                                        x8 = round(Xi_8 * f8,decimales_para_LR)
                                        
                                        #impresión de los datos de la clase 8
                                        print('---datos de la clase 8---')
                                        print('LI-8= ',LI8)
                                        print('LS-8= ',LS8)
                                        print('LRI-8= ',LRI8)
                                        print('LRS-8= ',LRS8)
                                        print('Xi-8= ',Xi_8)
                                        print('f-8= ',f8)
                                        print('h-8= ',h8)
                                        print('F-8= ',F8)
                                        print('H-8= ',H8)
                                        print(f'Xi * fi -8= {x8}')
                                        
                                        if LRS8 >= lista[no_de_datos - 1] :
                                            X = Xi_1 + Xi_2 + Xi_3 + Xi_4 + Xi_5 + Xi_6 + Xi_7 + Xi_8
                                            media = round(X / no_de_datos,decimales_para_LR)
                                    
                                        else:
                                            
                                            clase9 = []
                                            
                                            LI9 = round(LI8 + A,decimales_despues_del_punto)
                                            #   print('limite inferior 9: ',LI9)

                                            LS9 = round(LS8 + A,decimales_despues_del_punto)
                                            #   print('limite superior 9: ',LS9)
                                            
                                            numeradorLRI9 = round(LS9 - A + LI9,decimales_despues_del_punto)
                                            LRI9 = round(numeradorLRI9 / 2,decimales_para_LR)
                                            #   print('limite real inferior 9: ',LRI9)
                                            
                                            numeradorLRS9 = round(LS9 + LI9 + A,decimales_despues_del_punto) 
                                            LRS9 = round(numeradorLRS9 / 2,decimales_para_LR)
                                            #   print('limite real superior 9: ',LRS9)
                                            
                                            numeradorXi9 = round(LRI9 + LRS9,decimales_despues_del_punto)
                                            Xi_9 = round(numeradorXi9 / 2,decimales_para_LR)
                                            #   print('marca de clase 9: ',Xi_9)
                                            
                                            #definición de frecuencias de clase 9
                                            datos_de_clase9 = []

                                            for num in lista:
                                                if num > LRI9 and num < LRS9:
                                                    datos_de_clase9.append(num)
                                            f9 = len(datos_de_clase9)
                                            
                                            h9 = round(f9 / no_de_datos * 100,2)
                                            
                                            F9 = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9
                                            
                                            H9 = round(F9 / no_de_datos * 100,2)
                                            
                                            x9 = round(Xi_9 * f9,decimales_para_LR)
                                            
                                            #impresión de los datos de la clase 9
                                            print('---datos de la clase 9---')
                                            print('LI-9= ',LI9)
                                            print('LS-9= ',LS9)
                                            print('LRI-9= ',LRI9)
                                            print('LRS-9= ',LRS9)
                                            print('Xi-9= ',Xi_9)
                                            print('f-9= ',f9)
                                            print('h-9= ',h9)
                                            print('F-9= ',F9)
                                            print('H-9= ',H9)
                                            print(f'Xi * fi -9= {x9}')
                                            
                                            if LRS9 >= lista[no_de_datos - 1] :
                                                X = Xi_1 + Xi_2 + Xi_3 + Xi_4 + Xi_5 + Xi_6 + Xi_7 + Xi_8 + Xi_9
                                                media = round(X / no_de_datos,decimales_para_LR)
                                        
                                            else:
                                                
                                                clase10 = []
                                                
                                                LI10 = round(LI9 + A,decimales_despues_del_punto)
                                                #   print('limite inferior 10: ',LI10)

                                                LS10 = round(LS9 + A,decimales_despues_del_punto)
                                                #   print('limite superior 10: ',LS10)
                                                
                                                numeradorLRI10 = round(LS10 - A + LI10,decimales_despues_del_punto)
                                                LRI10 = round(numeradorLRI10 / 2,decimales_para_LR)
                                                #   print('limite real inferior 10: ',LRI10)
                                                
                                                numeradorLRS10 = round(LS10 + LI10 + A,decimales_despues_del_punto) 
                                                LRS10 = round(numeradorLRS10 / 2,decimales_para_LR)
                                                #   print('limite real superior 10: ',LRS10)
                                                
                                                numeradorXi10 = round(LRI10 + LRS10,decimales_despues_del_punto)
                                                Xi_10 = round(numeradorXi10 / 2,decimales_para_LR)
                                                #   print('marca de clase 10: ',Xi_10)
                                                
                                                #definición de frecuencias de clase 10
                                                datos_de_clase10 = []

                                                for num in lista:
                                                    if num > LRI10 and num < LRS10:
                                                        datos_de_clase10.append(num)
                                                f10 = len(datos_de_clase10)
                                                
                                                h10 = round(f10 / no_de_datos * 100,2)
                                                
                                                F10 = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10
                                                
                                                H10 = round(F10 / no_de_datos * 100,2)
                                                
                                                x10 = round(Xi_10 * f10,decimales_para_LR)
                                                
                                                #impresión de los datos de la clase 10
                                                print('---datos de la clase 10---')
                                                print('LI-10= ',LI10)
                                                print('LS-10= ',LS10)
                                                print('LRI-10= ',LRI10)
                                                print('LRS-10= ',LRS10)
                                                print('Xi-10= ',Xi_10)
                                                print('f-10= ',f10)
                                                print('h-10= ',h10)
                                                print('F-10= ',F10)
                                                print('H-10= ',H10)
                                                print(f'Xi * fi -10= {x10}')
                                                
                                                X = Xi_1 + Xi_2 + Xi_3 + Xi_4 + Xi_5 + Xi_6 + Xi_7 + Xi_8 + Xi_9 + Xi_10
                                                media = round(X / no_de_datos,decimales_para_LR)
                                                
            #imprimir la media
            print('la media es de= ',media)

            #continuación de la tabla para la desviación
            D1 = abs(round(Xi_1 - media,decimales_para_LR))
            casiDM1 = round(D1 * f1,decimales_para_LR)
            D1_cuadrado = round(D1 ** 2,decimales_para_LR)
            casivarianza1 = round(D1_cuadrado * f1,decimales_para_LR)

            print(f'grupo 1: (Xi - X)= {D1}     (D * f)= {casiDM1}     ((Xi - X)^2)= {D1_cuadrado}     (D^2 * fi)= {casivarianza1}')
            clase1.extend([LI1, LS1, LRI1, LRS1, Xi_1, f1, h1, F1, H1, x1, D1, casiDM1, D1_cuadrado, casivarianza1])
            mi_diccionario['clase1'] = clase1

            if LRS1 >= lista[no_de_datos - 1] :
                DM = round(casiDM1,decimales_para_LR)
                DMfinal = round(D1/no_de_datos,decimales_para_LR)
                numvarianza = round(casivarianza1,decimales_para_LR)
                varianza = round(numvarianza / no_de_datos,decimales_para_LR)

            else: 
                D2 = abs(round(Xi_2 - media,decimales_para_LR))
                casiDM2 = round(D2 * f2,decimales_para_LR)
                D2_cuadrado = round(D2 ** 2,decimales_para_LR)
                casivarianza2 = round(D2_cuadrado * f2,decimales_para_LR)
                
                print(f'grupo 2: (Xi - X)= {D2}      (D * f)= {casiDM2}      ((Xi - X)^2)= {D2_cuadrado}     (D^2 * fi)= {casivarianza2}')
                clase2.extend([LI2, LS2, LRI2, LRS2, Xi_2, f2, h2, F2, H2, x2, D2, casiDM2, D2_cuadrado, casivarianza2])
                mi_diccionario['clase2'] = clase2
                
                

                if LRS2 >= lista[no_de_datos - 1] :
                    DM = round(casiDM1 + casiDM2,decimales_para_LR)
                    DMfinal = round(DM/no_de_datos,decimales_para_LR)
                    numvarianza = round(casivarianza1 + casivarianza2,decimales_para_LR)
                    varianza = round(numvarianza / no_de_datos,decimales_para_LR)
                
                else: 
                    D3 = abs(round(Xi_3 - media,decimales_para_LR))
                    casiDM3 = round(D3 * f3,decimales_para_LR)
                    D3_cuadrado = round(D3 ** 2,decimales_para_LR)
                    casivarianza3 = round(D3_cuadrado * f3,decimales_para_LR)
                    
                    print(f'grupo 3: (Xi - X)= {D3}     (D * f)= {casiDM3}      ((Xi - X)^2)= {D3_cuadrado}     (D^2 * fi)= {casivarianza3}')
                    clase3.extend([LI3, LS3, LRI3, LRS3, Xi_3, f3, h3, F3, H3, x3, D3, casiDM3, D3_cuadrado, casivarianza3])
                    mi_diccionario['clase3'] = clase3

                    if LRS3 >= lista[no_de_datos - 1] :
                        DM = round(casiDM1 + casiDM2 + casiDM3,decimales_para_LR)
                        DMfinal = round(DM/no_de_datos,decimales_para_LR)
                        numvarianza = round(casivarianza1 + casivarianza2 + casivarianza3,decimales_para_LR)
                        varianza = round(numvarianza / no_de_datos,decimales_para_LR)
                    
                    else: 
                        D4 = abs(round(Xi_4 - media,decimales_para_LR))
                        casiDM4 = round(D4 * f4,decimales_para_LR)
                        D4_cuadrado = round(D4 ** 2,decimales_para_LR)
                        casivarianza4 = round(D4_cuadrado * f4,decimales_para_LR)
                        
                        print(f'grupo 4: (Xi - X)= {D4}     (D * f)= {casiDM4}      ((Xi - X)^2)= {D4_cuadrado}   (D^2 * fi)= {casivarianza4}')
                        clase4.extend([LI4, LS4, LRI4, LRS4, Xi_4, f4, h4, F4, H4, x4, D4, casiDM4, D4_cuadrado, casivarianza4])
                        mi_diccionario['clase4'] = clase4

                        if LRS4 >= lista[no_de_datos - 1] :
                            DM = round(casiDM1 + casiDM2 + casiDM3 + casiDM4,decimales_para_LR)
                            DMfinal = round(DM/no_de_datos,decimales_para_LR)
                            numvarianza = round(casivarianza1 + casivarianza2 + casivarianza3 + casivarianza4,decimales_para_LR)
                            varianza = round(numvarianza / no_de_datos,decimales_para_LR)
                            
                        else: 
                            D5 = abs(round(Xi_5 - media,decimales_para_LR))
                            casiDM5 = round(D5 * f5,decimales_para_LR)
                            D5_cuadrado = round(D5 ** 2,decimales_para_LR)
                            casivarianza5 = round(D5_cuadrado * f5,decimales_para_LR)
                            
                            print(f'grupo 5: (Xi - X)= {D5}     (D * f)= {casiDM5}      (Xi - X)^2= {D5_cuadrado}   (D^2 * fi)= {casivarianza5}')
                            clase5.extend([LI5, LS5, LRI5, LRS5, Xi_5, f5, h5, F5, H5, x5, D5, casiDM5, D5_cuadrado, casivarianza5])
                            mi_diccionario['clase5'] = clase5

                            if LRS5 >= lista[no_de_datos - 1] :
                                DM = round(casiDM1 + casiDM2 + casiDM3 + casiDM4 + casiDM5,decimales_para_LR)
                                DMfinal = round(DM/no_de_datos,decimales_para_LR)
                                numvarianza = round(casivarianza1 + casivarianza2 + casivarianza3 + casivarianza4 + casivarianza5,decimales_para_LR)
                                varianza = round(numvarianza / no_de_datos,decimales_para_LR)
                                
                            else: 
                                D6 = abs(round(Xi_6 - media,decimales_para_LR))
                                casiDM6 = round(D6 * f6,decimales_para_LR)
                                D6_cuadrado = round(D6 ** 2,decimales_para_LR)
                                casivarianza6 = round(D6_cuadrado * f6,decimales_para_LR)
                                
                                print(f'grupo 6: (Xi - X)= {D6}     (D * f)= {casiDM6}      ((Xi - X)^2)= {D6_cuadrado}     (D^2 * fi)= {casivarianza6}')
                                clase6.extend([LI6, LS6, LRI6, LRS6, Xi_6, f6, h6, F6, H6, x6, D6, casiDM6, D6_cuadrado, casivarianza6])
                                mi_diccionario['clase6'] = clase6

                                if LRS6 >= lista[no_de_datos - 1] :
                                    DM = round(casiDM1 + casiDM2 + casiDM3 + casiDM4 + casiDM5 + casiDM6,decimales_para_LR)
                                    DMfinal = round(DM/no_de_datos,decimales_para_LR)
                                    numvarianza = round(casivarianza1 + casivarianza2 + casivarianza3 + casivarianza4 + casivarianza5 + casivarianza6,decimales_para_LR)
                                    varianza = round(numvarianza / no_de_datos,decimales_para_LR)
                                    
                                else: 
                                    D7 = abs(round(Xi_7 - media,decimales_para_LR))
                                    casiDM7 = round(D7 * f7,decimales_para_LR)
                                    D7_cuadrado = round(D7 ** 2,decimales_para_LR)
                                    casivarianza7 = round(D7_cuadrado * f7,decimales_para_LR)
                                    
                                    print(f'grupo 7: (Xi - X)= {D7}     (D * f)= {casiDM7}      ((Xi - X)^2)= {D7_cuadrado}     (D^2 * fi)= {casivarianza7}')
                                    clase7.extend([LI7, LS7, LRI7, LRS7, Xi_7, f7, h7, F7, H7, x7, D7, casiDM7, D7_cuadrado, casivarianza7])
                                    mi_diccionario['clase7'] = clase7

                                    if LRS7 >= lista[no_de_datos - 1] :
                                        DM = round(casiDM1 + casiDM2 + casiDM3 + casiDM4 + casiDM5 + casiDM6 + casiDM7,decimales_para_LR)
                                        DMfinal = round(DM/no_de_datos,decimales_para_LR)
                                        numvarianza = round(casivarianza1 + casivarianza2 + casivarianza3 + casivarianza4 + casivarianza5 + casivarianza6 + casivarianza7,decimales_para_LR)
                                        varianza = round(numvarianza / no_de_datos,decimales_para_LR)
                                        
                                    else: 
                                        D8 = abs(round(Xi_8 - media,decimales_para_LR))
                                        casiDM8 = round(D8 * f8,decimales_para_LR)
                                        D8_cuadrado = round(D8 ** 2,decimales_para_LR)
                                        casivarianza8 = round(D8_cuadrado * f8,decimales_para_LR)
                                        
                                        print(f'grupo 8: (Xi - X)= {D8}     (D * f)= {casiDM8}      ((Xi - X)^2)= {D8_cuadrado}     (D^2 * fi)= {casivarianza8}')
                                        clase8.extend([LI8, LS8, LRI8, LRS8, Xi_8, f8, h8, F8, H8, x8, D8, casiDM8, D8_cuadrado, casivarianza8])
                                        mi_diccionario['clase8'] = clase8

                                        if LRS8 >= lista[no_de_datos - 1] :
                                            DM = round(casiDM1 + casiDM2 + casiDM3 + casiDM4 + casiDM5 + casiDM6 + casiDM7 + casiDM8,decimales_para_LR)
                                            DMfinal = round(DM/no_de_datos,decimales_para_LR)
                                            numvarianza = round(casivarianza1 + casivarianza2 + casivarianza3 + casivarianza4 + casivarianza5 + casivarianza6 + casivarianza7 + casivarianza8,decimales_para_LR)
                                            varianza = round(numvarianza / no_de_datos,decimales_para_LR)
                                            
                                        else: 
                                            D9 = abs(round(Xi_9 - media,decimales_para_LR))
                                            casiDM9 = round(D9 * f9,decimales_para_LR)
                                            D9_cuadrado = round(D9 ** 2,decimales_para_LR)
                                            casivarianza9 = round(D9_cuadrado * f9,decimales_para_LR)
                                            
                                            print(f'grupo 9: (Xi - X)= {D9}     (D * f)= {casiDM9}      ((Xi - X)^2)= {D9_cuadrado}     (D^2 * fi)= {casivarianza9}')
                                            clase9.extend([LI9, LS9, LRI9, LRS9, Xi_9, f9, h9, F9, H9, x9, D9, casiDM9, D9_cuadrado, casivarianza9])
                                            mi_diccionario['clase9'] = clase9

                                            if LRS9 >= lista[no_de_datos - 1] :
                                                DM = round(casiDM1 + casiDM2 + casiDM3 + casiDM4 + casiDM5 + casiDM6 + casiDM7 + casiDM8 + casiDM9,decimales_para_LR)
                                                DMfinal = round(DM/no_de_datos,decimales_para_LR)
                                                numvarianza = round(casivarianza1 + casivarianza2 + casivarianza3 + casivarianza4 + casivarianza5 + casivarianza6 + casivarianza7 + casivarianza8 + casivarianza9,decimales_para_LR)
                                                varianza = round(numvarianza / no_de_datos,decimales_para_LR)
                                                
                                            else: 
                                                D10 = abs(round(Xi_10 - media,decimales_para_LR))
                                                casiDM10 = round(D10 * f10,decimales_para_LR)
                                                D10_cuadrado = round(D10 ** 2,decimales_para_LR)
                                                casivarianza10 = round(D10_cuadrado * f10,decimales_para_LR)
                                                
                                                print(f'grupo 10: (Xi - X)= {D10}       (D * f)= {casiDM10}     ((Xi - X)^2)= {D10_cuadrado}    (D^2 * fi)= {casivarianza10}')
                                                clase10.extend([LI10, LS10, LRI10, LRS10, Xi_10, f10, h10, F10, H10, x10, D10, casiDM10, D10_cuadrado, casivarianza10])
                                                mi_diccionario['clase10'] = clase10
                                                
                                                DM = round(casiDM1 + casiDM2 + casiDM3 + casiDM4 + casiDM5 + casiDM6 + casiDM7 + casiDM8 + casiDM9 + casiDM10,decimales_para_LR)
                                                DMfinal = round(DM/no_de_datos,decimales_para_LR)
                                                numvarianza = round(casivarianza1 + casivarianza2 + casivarianza3 + casivarianza4 + casivarianza5 + casivarianza6 + casivarianza7 + casivarianza8 + casivarianza9 + casivarianza10,decimales_para_LR)
                                                varianza = round(numvarianza / no_de_datos,decimales_para_LR)

            print(f'Dm es igual a= {DMfinal}')
            print(f'varianza es igual a= {varianza}')
            print(f'diccionario: {mi_diccionario}')
            
            _dm = f'Desviación media = {DMfinal}'
            _varianza = f'Varianza = {varianza}'
            _media = f'Media = {media}'
            _rango = f'Rango = {R}'
            _amplitud_de_clase = f'Amplitud de clase = {A}'
            
            

            #final y cerrar el programa 
            # ------------------- AQUI TERMINA EL PROGRAMA --------------------------
        
        
        
        
        
        
        
        

    
    return render_template('index.html', 
                        forms = datos_form,  
                        _dm = _dm,
                        _varianza = _varianza,
                        _media = _media,
                        mi_diccionario = mi_diccionario,
                        _rango = _rango,
                        _amplitud_de_clase = _amplitud_de_clase)

if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")