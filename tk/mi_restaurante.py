from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox


precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

operador = ''

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END) 

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''

def revisar_check():
    x = 0
    for c in cuadro_comida:
        if variable_comida[x].get() == 1:
            cuadro_comida[x].config(state=NORMAL)
            if cuadro_comida[x].get() == '0':
                cuadro_comida[x].delete(0, END)
            cuadro_comida[x].focus()
        else:
            cuadro_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1
        
    x = 0
    for c in cuadro_bebida:
        if variable_bebida[x].get() == 1:
            cuadro_bebida[x].config(state=NORMAL)
            if cuadro_bebida[x].get() == '0':
                cuadro_bebida[x].delete(0, END)
            cuadro_bebida[x].focus()
        else:
            cuadro_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1

    x = 0
    for c in cuadro_postre:
        if variable_postre[x].get() == 1:
            cuadro_postre[x].config(state=NORMAL)
            if cuadro_bebida[x].get() == '0':
                cuadro_bebida[x].delete(0, END)
            cuadro_postre[x].focus()
        else:
            cuadro_postre[x].config(state=DISABLED)
            texto_postre[x].set('0')
        x += 1

def total():
    sub_total_comida = 0
    p= 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
    p += 1

    sub_total_bebida = 0
    p= 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
    p += 1

    sub_total_postre = 0
    p= 0
    for cantidad in texto_postre:
        sub_total_postre = sub_total_postre + (float(cantidad.get()) * precios_postres[p])
    p += 1
    
    
    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre
    impuestos = sub_total * 0.07
    total = sub_total + impuestos
    
    var_costos_comida.set(f'${round(sub_total_comida, 2)}')
    var_costos_bebidas.set(f'${round(sub_total_bebida, 2)}')
    var_costos_postre.set(f'${round(sub_total_postre, 2)}')
    var_costos_subtotal.set(f'${round(sub_total, 2)}')
    var_costos_impuesto.set(f'${round(impuestos, 2)}')
    var_costos_total.set(f'${round(total, 2)}')
    
def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f"N# - {random.randint(1000, 9999)}"
    fecha = datetime.datetime.now()
    fecha_recibo = f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}"
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END,'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')
    
    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t'
                                f'$ {int(comida.get()) * precios_comida[x]}\n')
        x += 1
    
    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t'
                                f'$ {int(bebida.get()) * precios_bebida[x]}\n')
        x += 1
    
    x = 0
    for postre in texto_postre:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t'
                                f'$ {int(postre.get()) * precios_postres[x]}\n')
        x += 1
    
    
    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END,f' Costo de la Comida: \t\t\t{var_costos_comida.get()}\n')
    texto_recibo.insert(END,f' Costo de la Bebida: \t\t\t{var_costos_bebidas.get()}\n')
    texto_recibo.insert(END,f' Costo del Postre : \t\t\t{var_costos_postre.get()}\n')
    
    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END,f' Subtotal : \t\t\t{var_costos_subtotal.get()}\n')
    texto_recibo.insert(END,f' Impuesto : \t\t\t{var_costos_impuesto.get()}\n')
    texto_recibo.insert(END,f' Total : \t\t\t{var_costos_total.get()}\n')
    
    
def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(modo='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo ha sido guardado')


def resetear():
    texto_recibo.delete(0.1, END)
    
    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')
        
    for cuadro in cuadro_comida:
        cuadro.config(state=DISABLED)    
    for cuadro in cuadro_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadro_postre:
        cuadro.config(state=DISABLED)
        
    for v in variable_comida:
        v.set(0)
    for v in variable_bebida:
        v.set(0)
    for v in variable_postre:
        v.set(0)
        
    var_costos_comida.set('')    
    var_costos_bebidas.set('')    
    var_costos_postre.set('')    
    var_costos_subtotal.set('')    
    var_costos_impuesto.set('')    
    var_costos_total.set('')    
    
        
        
        
        
# iniciar tkinter 
aplicacion = Tk()

# tamaño de la ventana
aplicacion.geometry('1020x630+0+0')



#evitar maximizar
# aplicacion.resizable(0, 0)


#Tituto de la ventana
aplicacion.title("Mi restaurante-Sistema de facturación")

#color de fondo de la ventana
aplicacion.config(bg='burlywood')

#panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

#etiqueta titulo
etiqueta_titulo = Label(panel_superior,text='Sistema de Facturación', fg='azure4',
                        font=('Dosis', 50), bg='burlywood', width=27)
etiqueta_titulo.grid(row=0, column=0)

# Panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=140)
panel_costos.pack(side=BOTTOM)

# Panel de comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# Panel de bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='bebidas', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)


# Panel de postres
panel_postres = LabelFrame(panel_izquierdo, text='postres', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)


# Panel derecha
panel_derecha = LabelFrame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)


# Panel calculadora
panel_calculadora = LabelFrame(panel_derecha,bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

# Panel recibo
panel_recibo = LabelFrame(panel_derecha,bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# Panel botones
panel_botones = LabelFrame(panel_derecha,bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()


# Lista de productos
lista_comidas = ['pollo', 'cordero', 'lomo','merluza','milanesa','costeleta','hamburguesas','papas']
lista_bebidas = ['coca-cola', 'pepsi', 'cerveza','agua','mirinda','fanta','doble-cola','pretty']
lista_postres = ['ensalada-frutas', 'budin', 'helado','bombon','gelatina','pastel','vainilla-split','mandarina']

# generar items comida
variable_comida= []
cuadro_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    
    #crear los checkbutton
    variable_comida.append('')
    variable_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, 
                         text=comida.title(), 
                         font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0, 
                         variable=variable_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador, 
                column=0, 
                sticky=W)
    
    #crear los cuadros de entrada
    cuadro_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadro_comida[contador]= Entry(panel_comidas,
                                    font=('Dosis',18, 'bold'),
                                    bd= 1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_comida[contador])
    cuadro_comida[contador].grid(row=contador,
                                 column=1)
    
    contador +=1

# generar items bebida
variable_bebida= []
cuadro_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    
    #crear los checkbutton
    
    variable_bebida.append('')
    variable_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, 
                         text=bebida.title(), 
                         font=('Dosis', 19, 'bold'),
                         onvalue=1, 
                         offvalue=0, 
                         variable=variable_bebida[contador],
                         command=revisar_check)
    bebida.grid(row=contador, 
                column=0, 
                sticky=W)
    
    #crear los cuadros de entrada
    cuadro_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadro_bebida[contador]= Entry(panel_bebidas,
                                    font=('Dosis',18, 'bold'),
                                    bd= 1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_bebida[contador])
    cuadro_bebida[contador].grid(row=contador,
                                 column=1)
    
    contador +=1


# generar items postre
variable_postre= []
cuadro_postre = []
texto_postre = []
contador = 0
for postre in lista_postres:
    
    #crear los checkbutton
    
    
    variable_postre.append('')
    variable_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres, 
                         text=postre.title(), 
                         font=('Dosis', 19, 'bold'),
                         onvalue=1, 
                         offvalue=0, 
                         variable=variable_postre[contador],
                         command=revisar_check)
    postre.grid(row=contador, 
                column=0, 
                sticky=W)
    
    #crear los cuadros de entrada
    cuadro_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadro_postre[contador]= Entry(panel_postres,
                                    font=('Dosis',18, 'bold'),
                                    bd= 1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_postre[contador])
    cuadro_postre[contador].grid(row=contador,
                                 column=1)
    
    contador +=1

#Variables
var_costos_comida= StringVar()
var_costos_bebidas= StringVar()
var_costos_postre= StringVar()
var_costos_subtotal= StringVar()
var_costos_impuesto= StringVar()
var_costos_total= StringVar()





# etiquetas de costos y campos de entreda
etiqueta_costos_comida = Label(panel_costos,
                               text='costo comida',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')

etiqueta_costos_comida.grid(row=0, column=0)

texto_costos_comida = Entry(panel_costos,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costos_comida)

texto_costos_comida.grid(row=0, column=1,padx=41)

#Etiqueta de bebida


etiqueta_costos_bebida = Label(panel_costos,
                               text='costo bebida',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')

etiqueta_costos_bebida.grid(row=1, column=0)

texto_costos_bebida = Entry(panel_costos,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costos_bebidas)

texto_costos_bebida.grid(row=1, column=1,padx=41)


#Etiqueta de postre


etiqueta_costos_postre = Label(panel_costos,
                               text='costo postre',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')

etiqueta_costos_postre.grid(row=2, column=0)

texto_costos_postre = Entry(panel_costos,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costos_postre)

texto_costos_postre.grid(row=2, column=1,padx=41)


#Etiqueta de subtotal


etiqueta_costos_subtotal = Label(panel_costos,
                               text='costo subtotal',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')

etiqueta_costos_subtotal.grid(row=0, column=2)

texto_costos_subtotal = Entry(panel_costos,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costos_subtotal)

texto_costos_subtotal.grid(row=0, column=3,padx=41)


#Etiqueta de impuesto


etiqueta_costos_impuesto = Label(panel_costos,
                               text='costo impuesto',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')

etiqueta_costos_impuesto.grid(row=1, column=2)

texto_costos_impuesto = Entry(panel_costos,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costos_impuesto)

texto_costos_impuesto.grid(row=1, column=3,padx=41)

#Etiqueta de total


etiqueta_costos_total = Label(panel_costos,
                               text='costo total',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')

etiqueta_costos_total.grid(row=2, column=2)

texto_costos_total = Entry(panel_costos,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costos_total)

texto_costos_total.grid(row=2, column=3,padx=41)

#botones

botones = ['total', 'recibo', 'guardar', 'resetear']
botones_creados = []

columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis',14,'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)
    botones_creados.append(boton)
    boton.grid(row=0,
               column=columnas)
    columnas +=1
    
botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)




# area de ricibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis',12,'bold'),
                    bd=1,
                    width=22,
                    height=10)

texto_recibo.grid(row=0,
                  column=0)

#Calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          width=32,
                          bd=1)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

botones_calculadora = ['7','8','9','+','4','5','6','-','1','2','3','x','R','B','0','/']


botones_guardados =[]

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 16, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=8)

    botones_guardados.append(boton)

    boton.grid(row=fila,
               column=columna)

    if columna ==3:
        fila +=1
        
    columna +=1
    
    if columna == 4:
        columna = 0


botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))

#evitar que la pantalla se cierre
aplicacion.mainloop()