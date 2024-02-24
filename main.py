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
        
        
        #aqui se crean las clases
        class clases: 
            def __init__(self, no_init, data, A, unidad_min, decimales_despues_del_punto, decimales_para_LR, no_data_T, list_fi, list_hi):
                
                self.LI = no_init
                self.LS = round(no_init + A - unidad_min, decimales_despues_del_punto)
                self.LRI = round((self.LS - A + self.LI) / 2, decimales_para_LR)
                self.LRS = round((self.LS + self.LI + A) / 2, decimales_para_LR)
                
                data_f_c = [x for x in data if x > self.LRI and x < self.LRS]
                
                self.x = round((self.LRS + self.LRI) / 2, decimales_para_LR)
                self.f = len(data_f_c)
                self.h = round(self.f / no_data_T * 100, decimales_despues_del_punto)
                self.F = round(sum(list_fi) + self.f, decimales_despues_del_punto)
                self.H = round(self.F / no_data_T * 100, decimales_despues_del_punto)
                
                self.xi_x_fi = round(self.x * self.f, decimales_para_LR)
                
                #se crea la variable numero de decimales para usar en los demas metodos
                self.no =decimales_para_LR
            
            def p2(self, M, list_x, list_fi, i):
                self.xi_menos_media = abs(round(list_x[i] - M, self.no))
                self.D_x_fi = round(self.xi_menos_media * list_fi[i], self.no)
                self.xi_menos_media_al_2 = round(self.xi_menos_media ** 2, self.no)
                self.D_al_2_x_fi = round(self.xi_menos_media_al_2 * list_fi[i], self.no)
        
        obtencion = datos_form.datos.data
        obtencion = ' '.join(obtencion.split())
        obtencion = ' '.join(obtencion.split(','))
        decimales_despues_del_punto = datos_form.punto.data
        
        if obtencion != '' and decimales_despues_del_punto != '':
        

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
            
            # creando el diccipnario con todos los datos de la tabla para enviar al index.html
            mi_diccionario = {}

            list_x = []
            list_fi = []
            list_hi = []


            list_D_x_fi = []
            list_D_al_2_x_fi = []

            #impresion de la lista ordenada
            print('así queda la lista ordenada: ',lista)

            print('')

            #definición de decimales despues de punto y unidades minimas

            no_de_datos = len(lista)


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
                A = round(R/K, decimales_despues_del_punto)
                decimales_para_LR = decimales_despues_del_punto + 1
                
                cantidad_ceros = int(decimales_despues_del_punto)
                cantidad_ceros_menos_uno = cantidad_ceros - 1
                ceros = '0' * cantidad_ceros_menos_uno
                unidad_min_en_cadena = f'0.{ceros}1'
                
                unidad_min = float(unidad_min_en_cadena)
                
            else:
                A = round(R/K, decimales_despues_del_punto)
                decimales_para_LR = decimales_despues_del_punto + 1

            #definicion de variable n

            print('rango=',R)
            print('numero de clases=',K)
            print('amplitud=',A)


            #  --------------inicia la tabla----------------------

            no_init = lista[0]
            num = 1

            while no_init <= lista[no_de_datos - 1]:
                
                
                clase = clases(no_init, lista, A, unidad_min, decimales_despues_del_punto, decimales_para_LR, len(lista), list_fi, list_hi)
                
                mi_diccionario[f'clase{num}'] = [clase.LI, 
                                                clase.LS,
                                                clase.LRI,
                                                clase.LRS,
                                                clase.x,
                                                clase.f,
                                                clase.h,
                                                clase.F,
                                                clase.H,
                                                clase.xi_x_fi]
                
                list_x.append(clase.x)
                list_fi.append(clase.f)
                list_hi.append(clase.h)
                
                no_init += A
                num += 1
                
            media = round(sum(list_x) / no_de_datos, decimales_para_LR)

            for i in range(len(list_x)):
                
                clase.p2(media, list_x, list_fi, i)
                
                mi_diccionario[f'clase{i+1}'].append(clase.xi_menos_media)
                mi_diccionario[f'clase{i+1}'].append(clase.D_x_fi)
                mi_diccionario[f'clase{i+1}'].append(clase.xi_menos_media_al_2)
                mi_diccionario[f'clase{i+1}'].append(clase.D_al_2_x_fi)
                
                list_D_x_fi.append(clase.D_x_fi)
                list_D_al_2_x_fi.append(clase.D_al_2_x_fi)
                

            #se calcula desviación media
            DM = round(sum(list_D_x_fi)/no_de_datos, decimales_para_LR)

            #se calcula varianza
            Var = round(sum(list_D_al_2_x_fi)/no_de_datos, decimales_para_LR)

# estructura del diccionario:
# diccionario = {
#     'clase{i}' : [LI, LS, LRI, LRS, x, fi, hi, Fi, Hi, xi_x_fi, xi_menos_media, D_x_fi, xi_menos_media_al_2, D_al_2_x_fi]
# }

            _dm = f'Desviación media = {DM}'
            _varianza = f'Varianza = {Var}'
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
    app.run(debug=True, port=80, host="0.0.0.0")