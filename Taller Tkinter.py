import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter import scrolledtext

def init_window():
    window = tk.Tk() #Crear la pantalla
    window.title('Calculadora SaninfomaxUN - v2.0') #Agregar titulo a la pantalla
    # Establecer tamaño de la pantalla (Ancho: 400px y largo: 250px)
    window.geometry('500x300')

    #Control de Pestañas
    tab_control = ttk.Notebook(window)
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab3 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Calculadora')
    tab_control.add(tab2, text='Historial')
    tab_control.add(tab3, text='Sugerencias')
    tab_control.grid(column=0, row=0)

    #Crear una etiqueta con fuente Arial Bold y Tamaño 15
    label = tk.Label(tab1, text='Calculadora', font=('Arial bold', 25), fg='gold2',padx=20)
    #Ubicar ala etiqueta en la columna y fila 0 de la pantalla
    label.grid(column = 0, row = 2)

    #Agregar dos campos de texto
    entrada1 = tk.Entry(tab1, width = 10)
    entrada2 = tk.Entry(tab1, width = 10)

    entrada1.grid(column = 1, row = 3)
    entrada2.grid(column = 1, row = 4)

    #Agregar dos etiquetas para indicarle al usuario los valores que debe ingresar
    label_entrada1 = tk.Label(tab1, text='Ingrese Primer Numero', font=('Arial bold', 10))
    label_entrada1.grid(column=0, row=3)

    label_entrada2 = tk.Label(tab1, text='Ingrese Segundo Numero', font=('Arial bold', 10))
    label_entrada2.grid(column=0, row=4)

    #Crear una etiqueta para el seleccionador (Combobox)
    label_operador = tk.Label(tab1, text='Escoja un operador', font=('Arial bold', 10))
    label_operador.grid(column=0, row=5)

    # Crear un seleccionador (Combobox)
    combo_operadores = ttk.Combobox(tab1)
    #Asignar los valores del seleccionador a traves de su atributo values
    combo_operadores['values'] = ['+', '-', '*', '/', 'pow']
    #Asignar por defecto una opcion seleccionada: 0 es el indice de los valores
    combo_operadores.current(0) #Set the selected item
    #Ubicar el seleccionador
    combo_operadores.grid(column=1, row=5)

    #Agregar etiqueta para mostrar el resultado de la operación en pantalla
    label_resultado = tk.Label(tab1, text='Resultado', font=('Arial bold', 15))
    label_resultado.grid(column=0, row=9)
    #variables
    Historial = []
    contador = 1
    # Boton calcular
    boton = tk.Button(tab1,
                      command=lambda: click_calcular(
                          label_resultado,
                          entrada1.get(),
                          entrada2.get(),
                          combo_operadores.get(),
                          entrada1,
                          entrada2,
                          tab2,
                          Historial,
                          contador),
                      text='Calcular',
                      font='bold 12',
                      bg="gold2",
                      fg="black",
                      padx=10)
    boton.grid(column=1, row=6)

    #Boton Resetear
    botonReset = tk.Button(tab1,
                           command=lambda: reset(
                               label_resultado, entrada1, entrada2
                           ),
                      text='AC',
                      font='bold 12',
                      bg="grey",
                      fg="white",
                      padx=10)
    botonReset.grid(column=2, row=6)


    # Crear una etiqueta para el seleccionador (Combobox)
    label_creator = tk.Label(tab1, text='Created by: SaninfomaxUN' + chr(169) , font=('Arial bold', 8))
    label_creator.grid(column=1, row=10)

#------------------------------------------------TAB 2------------------------------------------------
    # Crear una etiqueta con fuente Arial Bold y Tamaño 15
    label_titulo = tk.Label(tab2, text='Operaciones Recientes', font=('Arial bold', 25), fg='gold2', padx=20)
    # Ubicar ala etiqueta en la columna y fila 0 de la pantalla
    label_titulo.grid(column=0, row=0)

# ------------------------------------------------TAB 3------------------------------------------------
    # Crear una etiqueta con fuente Arial Bold y Tamaño 15
    label_titulo = tk.Label(tab3, text='Buzon de sugerencias', font=('Arial bold', 18), fg='gold2', padx=20)
    # Ubicar ala etiqueta en la columna y fila 0 de la pantalla
    label_titulo.grid(column=0, row=0)

    def btnemail():
        messagebox.showinfo('Buzon de Sugerencias', 'Correo ingresado Exitosamente!! \n Ya puedes escribir tu comentario!')
        txt.configure(state='normal')
    label_correo = Label(tab3,text='Ingresa tu correo para continuar!' )
    label_correo.grid(column=0, row=1)
    EntradaSug = Entry(tab3, width=30)
    EntradaSug.grid(column=0, row=2)
    btncorreo = Button(tab3, text='Ingresar', command=btnemail)
    btncorreo.grid(column=1, row=2)


    txt = scrolledtext.ScrolledText(tab3, width=40, height=10, state='disabled')
    txt.grid(column=0, row = 3)
    txt.insert('insert', 'Si tienes alguna sugerencia o inquietud, escribela aqui!')

    def btnsuger():
        resp = messagebox.askyesno('Buzon de sugerencias','Estas de acuerdo con nuestra politica de tratamiento de datos??')
        if resp:
            messagebox.showinfo('Buzon de Sugerencias','Comentario enviado Correctamente!!')
        else:
            messagebox.showwarning('Buzon de sugerencias','Lo sentimos, debes aceptar nuestras politicas para revisar tu comentario.')
    btnsugerencias = Button(tab3, text='Enviar', command=btnsuger)
    btnsugerencias.grid(column=1, row=4)

    window.mainloop()
#------------------------------------------------FUNCIONES-------------------------------------------
def calculadora(num1, num2, operador):
    if operador =='+':
        resultado = num1 + num2
    elif operador =='-':
        resultado = num1 - num2
    elif operador =='*':
        resultado = num1 * num2
    elif operador =='/':
        resultado = round(num1 / num2,2)
    else:
        resultado = num1 ** num2

    return resultado

def click_calcular(label, num1, num2, operador, entrada1, entrada2,tab2, Historial, contador):
    Historial.insert(0,num1)
    Historial.insert(1, operador)
    Historial.insert(2,num2)
    Historial.insert(3,'=')

    comprobacion = comprobar(num1,num2, entrada1, entrada2)
    if comprobacion[0] == True:
        #Conversion de valores
        valor1 = round(float(num1),8)
        valor2 = round(float(num2),8)

        # Calculo dados los valores y el operador
        res = calculadora(valor1, valor2, operador)

        #Enviar Historial
        Historial.insert(4,str(res))
        Historial.insert(5, '\n')
        historial(tab2, Historial)

        # Actualizacion del texto en la etiqueta
        label.configure(text='Resultado: ' + str(res))
    else:
        # Deshacer Color Rojo - Limpiar Campo 1
        if comprobacion[1]==False:
            messagebox.showerror('Caracter Incorrecto', 'Por favor ingrese un numero!!')
            entrada1.delete(0, 'end')
            entrada1.configure(bg='white')
        # Deshacer Color Rojo - Limpiar Campo 2
        if comprobacion[2]==False:
            messagebox.showerror('Caracter Incorrecto', 'Por favor ingrese un numero!!')
            entrada2.delete(0, 'end')
            entrada2.configure(bg='white')
        # Deshacer Color Rojo -  Campo 1 Vacio
        if comprobacion[3] == False:
            messagebox.showwarning('Campo Vacio', 'Por favor ingrese un numero!!')
            entrada1.delete(0, 'end')
            entrada1.configure(bg='white')
        # Deshacer Color Rojo -  Campo 2 Vacio
        if comprobacion[4] == False:
            messagebox.showwarning('Campo Vacio', 'Por favor ingrese un numero!!')
            entrada2.delete(0, 'end')
            entrada2.configure(bg='white')



#resetear resultado
def reset(label, entrada1, entrada2):
    label.configure(text= 'Resultado')
    entrada1.delete(0, 'end')
    entrada2.delete(0, 'end')


#comprobar valores ingresados
def comprobar(num1,num2, entrada1, entrada2):
    BanderaG = BanderaEnt1 = BanderaEnt2 = BanderaEsp1 = BanderaEsp2 = True
    if len(num1) ==0:
        entrada1.configure(bg='grey')
        BanderaEsp1 = False
        BanderaG = False
    if len(num2) ==0:
        entrada2.configure(bg='grey')
        BanderaEsp2 = False
        BanderaG = False
    for digito in num1:
        if ord(digito) >= 44 and ord(digito) <=57:
            continue
        else:
            entrada1.configure(bg='red')
            BanderaG = False
            BanderaEnt1 = False
    for digito in num2:
        if ord(digito) >= 44 and ord(digito) <=57:
            continue
        else:
            entrada2.configure(bg='red')
            BanderaEnt2 = False
            BanderaG = False
    return BanderaG, BanderaEnt1, BanderaEnt2,BanderaEsp1,BanderaEsp2

def historial(tab2,Historial):
    print(Historial)
    NewCaracter1 = tk.Label(tab2, text='Hola')
    NewCaracter1.grid(column=0, row=3)
    if len(Historial) > 36:
        Historial = Historial[:-6]
    Historial = "".join(Historial)
    NewCaracter1.config(text=Historial,font='bold 12',
                      fg="red",)

def main():
    init_window()
contador = 1
main()