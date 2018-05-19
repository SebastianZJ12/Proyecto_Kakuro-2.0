#Proyecto no.2 Kakuro.
#Profesor: William Mata Rodríguez.
#Sebastián Zamora Jiménez 2018170723.
from tkinter import *
from tkinter import messagebox
import random
import threading
import time
import pygame
import webbrowser
import os

pygame.mixer.init()
#Ventana principal.
raiz=Tk()
raiz.title("Menú principal del Kakuro")
raiz.resizable(0,0)
raiz.geometry("700x700+10+10")
raiz.config(relief="ridge", bg="grey", bd=10)

#Funciones
def salir(): #Funcion para cerrar el menú.
    """Funcion para cerrar el menú"""
    raiz.destroy()

def acerca_de(): #Funcion para desplegar el cuadro de "Acerca de".
    """Funcion para desplegar el cuadro de 'Acerca de'"""
    messagebox.showinfo("Acerca de:", "Proyecto no.2\nKakuro\nVersion Python 3.6.4\nFecha de creación:01-05-2018\nAutor: Sebastián Zamora Jiménez")

def ayuda(): #Funcion para desplegar el Manual de Usuario.
    os.startfile('Manual_de_Usuario_Kakuro 2018170723.pdf')

#Variables de la configuración.
neurona=1 #Variable que indica el nivel de dificultad.
nivel=StringVar()
nivel.set(str(neurona)+" Neuronas")
tiempo_juego="No" #Indicador del reloj
reloj=StringVar()
reloj.set(tiempo_juego)
contatimer=1
contareloj=0
timer="No" #Indicador del timer
#Variables donde se ingresarán la cantidad de horas, minutos y segundos, que se escojan del timer.
horas_timer=0
min_timer=0
min_timer2=0
seg_timer=0
seg_timer2=0
tiempo_de_partida=0
tiempo_jugado=0
multinivel=False

def configuracion(): #Función que despliega el menú para configurar la partida.
    config=Toplevel()
    config.title("Configuración del juego")
    config.geometry("400x480+10+10")
    config.config(relief="ridge", bg="green", bd=10)
    config.resizable(0,0)

    def neuronas_nivel(): #Función para seleccionar el nivel de dificultad.
        """Función para seleccionar el nivel de dificultad"""
        global nivel
        global neurona
        global multinivel
        if neurona==1:
            neurona+=1
        elif neurona==2:
            neurona+=1
        elif neurona==3:
            neurona+=1
            nivel.set("Multinivel")
            return
        else:
            neurona=1
        nivel.set(str(neurona)+" Neuronas")

    def activar_temporizador(): #Función que activa el temporizador.
        """Función que activa el temporizador"""
        global contatimer
        global tiempo_juego
        global timer
        global horas_timer
        global min_timer
        global min_timer2
        global seg_timer
        global seg_timer2
        if tiempo_juego=="No": #Verifica que la opción de Reloj esté desactivada.
            contatimer+=1
            if contatimer%2==0:
                horas.config(state="normal", bg="orange")
                minutos.config(state="normal", bg="orange")
                minutos2.config(state="normal", bg="orange")
                segundos.config(state="normal", bg="orange")
                segundos2.config(state="normal", bg="orange")
                timer="Si"
                tiempo_juego="No"
            else:
                horas.config(state="disabled", bg="green")
                minutos.config(state="disabled", bg="green")
                minutos2.config(state="disabled", bg="green")
                segundos.config(state="disabled", bg="green")
                segundos2.config(state="disabled", bg="green")
                timer="No"
                tiempo_juego=="Si"
                horas_timer=0
                min_timer=0
                min_timer2=0
                seg_timer=0
                seg_timer2=0
                horas.config(text=horas_timer)
                minutos.config(text=min_timer)
                minutos2.config(text=min_timer2)
                segundos.config(text=seg_timer)
                segundos2.config(text=seg_timer2)
                
    def activar_reloj(): #Función para activar el Reloj en pantalla.
        """Función para activar el Reloj en pantalla"""
        global contareloj
        global reloj
        global tiempo_juego
        global timer
        global horas_timer
        global min_timer
        global min_timer2
        global seg_timer
        global seg_timer2
        contareloj+=1
        if contareloj%2==0:
            tiempo_juego="No"
            timer="Si"
        else:
            tiempo_juego="Si"
            timer="No"
            horas.config(state="disabled", bg="green")
            minutos.config(state="disabled", bg="green")
            minutos2.config(state="disabled", bg="green")
            segundos.config(state="disabled", bg="green")
            segundos2.config(state="disabled", bg="green")
            horas_timer=0
            min_timer=0
            min_timer2=0
            seg_timer=0
            seg_timer2=0
            horas.config(text=horas_timer)
            minutos.config(text=min_timer)
            minutos2.config(text=min_timer2)
            segundos.config(text=seg_timer)
            segundos2.config(text=seg_timer2)
        reloj.set(tiempo_juego)

    def definir_timer(x): #Función para determinar la cantidad de horas, minutos y segundos del timer.
        global horas_timer
        global min_timer
        global seg_timer
        global min_timer2
        global seg_timer2
        if x==1:
            if horas_timer==0:
                horas_timer=1
            elif horas_timer==1:
                horas_timer=2
            else:
                horas_timer=0
            horas.config(text=horas_timer)
        elif x==2:
            if min_timer>=0:
                min_timer+=1
            if min_timer>5:
                min_timer=0
            minutos.config(text=min_timer)
        elif x==3:
            if min_timer2>=0:
                min_timer2+=1
            if min_timer2>9:
                min_timer2=0
            minutos2.config(text=min_timer2)
        elif x==4:
            if seg_timer>=0:
                seg_timer+=1
            if seg_timer>5:
                seg_timer=0
            segundos.config(text=seg_timer)
        elif x==5:
            if seg_timer2>=0:
                seg_timer2+=1
            if seg_timer2>9:
                seg_timer2=0
            segundos2.config(text=seg_timer2)

    def segundos_totales(): #Convierte a segundos todas las horas, minutos y segundos del timer.
        """Convierte a segundos todas las horas, minutos y segundos del timer"""
        global horas_timer
        global min_timer
        global seg_timer
        global min_timer2
        global seg_timer2
        global tiempo_de_partida
        horas=horas_timer*3600
        minutos=(min_timer*10+min_timer2)*60
        segundos=seg_timer*10+seg_timer2
        seg_totales=horas+minutos+segundos
        tiempo_de_partida=seg_totales
        return seg_totales

    def guardar_config(): #Guarda la configuración en un archivo para posteriormente ser leída cuando se inicie la partida.
        """Guarda la configuración en un archivo para posteriormente ser leída cuando se inicie la partida"""
        global timer
        global tiempo_juego
        global neurona
        nivel=str(neurona)
        f=open("kakuro2018config.txt","w")
        seg=segundos_totales()
        if seg!=0:
            seg=str(seg)
            tiempo_juego="No"
            if neurona==1:
                lista_par=str(['1','Timer',seg])
                f.write(lista_par)
            elif neurona==2:
                lista_par=str(['2','Timer',seg])
                f.write(lista_par)
            else:
                lista_par=str(['3','Timer',seg])
                f.write(lista_par)
        else:
            timer="No"
            if tiempo_juego=="Si":
                if neurona==1:
                    f.write("['1','Si','0']")
                elif neurona==2:
                    f.write("['2','Si','0']")
                else:
                    f.write("['3','Si','0']")
            else:
                if neurona==1:
                    f.write("['1','No','0']")
                elif neurona==2:
                    f.write("['2','No','0']")
                else:
                    f.write("['3','No','0']")
        f.close()

    #Botones
    #Dificultad
    dificultad=Button(config, width="15", text="Dificultad", font=('Bahnschrift SemiBold', 20), fg="black", bg="orange", command=lambda: neuronas_nivel())
    dificultad.pack()

    Label(config, width="15", textvariable=nivel, font=('Bahnschrift SemiBold', 20), fg="black", bg="orange").pack(padx=10,pady=10)

    #Tiempo
    #Reloj
    reloj_boton=Button(config, width="15", text="Reloj", font=('Bahnschrift SemiBold', 20), fg="black", bg="orange", command=lambda: activar_reloj()).pack()
    Label(config, width="15", textvariable=reloj, font=('Bahnschrift SemiBold', 20), fg="black", bg="orange").pack(padx=10,pady=10)

    #Temporizador
    temporizador=Button(config, width="15", text="Temporizador", font=('Bahnschrift SemiBold', 20), fg="black", bg="orange", command=lambda: activar_temporizador()).pack()

    #Botones para configurar el timer
    horas=Button(config, width="3", font=('Bahnschrift SemiBold', 15), fg="black", bg="green", state="disabled", text=0, command=lambda: definir_timer(1))
    horas.place(x=40, y=325)
    Label(config, width="5", font=('Bahnschrift SemiBold', 13), fg="black", bg="green", text="Horas").place(x=37, y=295)
    
    minutos=Button(config, width="3", font=('Bahnschrift SemiBold', 15), fg="black", bg="green", state="disabled", text=0, command=lambda: definir_timer(2))
    minutos.place(x=127, y=325)
    
    minutos2=Button(config, width="3", font=('Bahnschrift SemiBold', 15), fg="black", bg="green", state="disabled", text=0, command=lambda: definir_timer(3))
    minutos2.place(x=170, y=325)
    Label(config, width="6", font=('Bahnschrift SemiBold', 13), fg="black", bg="green", text="Minutos").place(x=140, y=295)
    
    segundos=Button(config, width="3", font=('Bahnschrift SemiBold', 15), fg="black", bg="green", state="disabled", text=0, command=lambda: definir_timer(4))
    segundos.place(x=260, y=325)

    segundos2=Button(config, width="3", font=('Bahnschrift SemiBold', 15), fg="black", bg="green", state="disabled", text=0, command=lambda: definir_timer(5))
    segundos2.place(x=303, y=325)
    Label(config, width="8", font=('Bahnschrift SemiBold', 12), fg="black", bg="green", text="Segundos").place(x=264, y=295)

    #Guardar configuracion
    guardar_opciones=Button(config, width="20", text="Guadar\nConfiguración", font=('Bahnschrift SemiBold', 15), fg="black", bg="orange", command=lambda: guardar_config())
    guardar_opciones.place(x=73, y=385)



#Variables globales para el juego.
nombre_jugador=StringVar()
nombre="" #Variable donde se guarda el nombre del jugador.
numero_seleccionado="" #Variable donde se guarda el número que se selecciona.
num_seleccionado=StringVar()
terminado=False #Bandera que verifica si el juego se completó correctamente.
juego_iniciado=False #Bandera que indica si el juego se inició.
kakuro2=[] #Lista que recibe la matriz de juego del kakuro.
lista_botones2=[] #Lista que recibe la lista de botones y etiquetas del tablero dinámico.
jugadas=[] #Lista que guarda las jugadas. Se usa para borrar jugadas.
recuperar_jugadas=[]
contenido=() #Tupla que recibe el contenido de la partida.
juego_anterior=[] #Lista que posee el juego anterior para no ser repetido si se inicia otro juego.
        
def leer_archivo(): #Función que lee las partidas de cada nivel según el grado de dificultad seleccionado.
    """Función que lee las partidas de cada nivel según el grado de dificultad seleccionado"""
    global neurona
    global juego_anterior
    global multinivel
    f=open("kakuro2018partidas.txt", "r")
    cont=0
    if neurona==4:
        multinivel=True
        neurona=1
    if neurona==1:
        while cont!=1:
            contenido= f.readline()
            cont+=1
    if neurona==2:
        while cont!=2:
            contenido= f.readline()
            cont+=1
    if neurona==3:
        while cont!=3:
            contenido= f.readline()
            cont+=1
    contenido=eval(contenido)
    contenido2=random.choice(contenido)
    if juego_anterior==[]: #Aqui verifica si existía alguna partida anterior
        juego_anterior+=[contenido2]
    if juego_anterior!=[]: #Si si existía, verifica que la próxima partida no sea la misma
        if contenido2==juego_anterior[0]:
            while contenido2==juego_anterior[0]:
                contenido2=random.choice(contenido)
        juego_anterior[0]=contenido2
    f.close()
    return contenido2


def top_10(): #Función que despliega los mejores tiempos del kakuro de sus respectivos niveles
    """Función que despliega los mejores tiempos del kakuro de sus respectivos niveles"""
    top=Toplevel()
    top.title("Top 10")
    top.geometry("1000x600+10+10")
    top.config(relief="ridge", bg="red", bd=10)
    top.resizable(0,0)                
    Label(top, bg="red", width="10").grid(row=0,column=0)
    Label(top, bg="red", width="10").grid(row=0,column=1)
    Label(top, bg="red", width="15").grid(row=1,column=1, columnspan=2)
    Label(top, bg="red", width="15").grid(row=1,column=5, columnspan=2)
    Label(top, font=("Gang of Three", 35), fg="white", bg="red", text="TOP 1O").grid(row=0,column=4)
      
    Label(top, font=("Gang of Three", 30), fg="white", bg="red", text="Neurona 1").grid(row=1,column=0)
    Label(top, font=("Gang of Three", 18), fg="white", bg="red", text="Jugador", justify="l").grid(row=2,column=0)
    Label(top, font=("Gang of Three", 18), fg="white", bg="red", text="Tiempo", justify="l").grid(row=2,column=1)
    
    Label(top, font=("Gang of Three", 30), fg="white", bg="red", text="Neurona 2").grid(row=1,column=4)
    Label(top, font=("Gang of Three", 18), fg="white", bg="red", text="Jugador", justify="l").grid(row=2,column=4)
    Label(top, font=("Gang of Three", 18), fg="white", bg="red", text="Tiempo", justify="l").grid(row=2,column=5)
      
    Label(top, font=("Gang of Three", 30), fg="white", bg="red", text="Neurona 3").grid(row=1,column=8)
    Label(top, font=("Gang of Three", 18), fg="white", bg="red", text="Jugador", justify="l").grid(row=2,column=8)
    Label(top, font=("Gang of Three", 18), fg="white", bg="red", text="Tiempo", justify="l").grid(row=2,column=9)
    
    matriz_jugador=[["#","#","#","#","#","#","#","#","#","#"],
                    ["#","#","#","#","#","#","#","#","#","#"],
                    ["#","#","#","#","#","#","#","#","#","#"]]
        
    matriz_tiempo=[["#","#","#","#","#","#","#","#","#","#"],
                   ["#","#","#","#","#","#","#","#","#","#"],
                   ["#","#","#","#","#","#","#","#","#","#"]]

    top_10_arch=open("kakurotop10.txt",'r')
    lineas=top_10_arch.readlines()
    lista_ganadores=[]
    for nivel in lineas: #Aqui guarda en una lista las listas de los diferentes niveles
        lista_ganadores.append(eval(nivel))
    top_10_arch.close()
    lista_num=["0","1","2","3","4","5","6","7","8","9"]
    nivel=1
    fila=3
    for lista in lista_ganadores:
        cont_jugador2=0
        cont_tiempo2=0
        for elemento in lista:
            nombre_top=str(elemento[0])
            tiempo=int(elemento[1])
            horas=tiempo//3600
            minutos=(tiempo%3600)//60
            segundos=(tiempo%3600)%60
            if str(horas) in lista_num:
                horas="0"+str(horas)
            else:
                horas=str(horas)
            if str(minutos) in lista_num:
                minutos="0"+str(minutos)
            else:
                minutos=str(minutos)
            if str(segundos) in lista_num:
                segundos="0"+str(segundos)
            else:
                segundos=str(segundos)
            variable_tiempo=horas+":"+minutos+":"+segundos
            if nivel==1:
                matriz_jugador[0][cont_jugador2]=Label(top, font=("Gang of Three", 15), fg="white", bg="red", text=nombre_top)
                matriz_jugador[0][cont_jugador2].grid(row=fila,column=0)
                matriz_tiempo[0][cont_tiempo2]=Label(top, font=("Gang of Three", 15), fg="white", bg="red", text=variable_tiempo)
                matriz_tiempo[0][cont_tiempo2].grid(row=fila,column=1)
            elif nivel==2:
                matriz_jugador[1][cont_jugador2]=Label(top, font=("Gang of Three", 15), fg="white", bg="red", text=nombre_top)
                matriz_jugador[1][cont_jugador2].grid(row=fila,column=4)
                matriz_tiempo[1][cont_tiempo2]=Label(top, font=("Gang of Three", 15), fg="white", bg="red", text=variable_tiempo)
                matriz_tiempo[1][cont_tiempo2].grid(row=fila,column=5)
            elif nivel==3:
                matriz_jugador[2][cont_jugador2]=Label(top, font=("Gang of Three", 15), fg="white", bg="red", text=nombre_top)
                matriz_jugador[2][cont_jugador2].grid(row=fila,column=8)
                matriz_tiempo[2][cont_tiempo2]=Label(top, font=("Gang of Three", 15), fg="white", bg="red", text=variable_tiempo)
                matriz_tiempo[2][cont_tiempo2].grid(row=fila,column=9)
            cont_jugador2+=1
            cont_tiempo2+=1
            fila+=1
        fila=3
        nivel+=1

def a_jugar(): #Funcion para deplegar el tablero de juego.
    """Funcion para deplegar el tablero de juego"""
    juego=Toplevel()
    juego.title("Kakuro")
    juego.geometry("850x750+10+10")
    juego.config(relief="ridge", bg="light grey", bd=10)
    juego.resizable(0,0)
    kakuro=[[0,0,0,0,0,0,0,0,0], #Matriz que contiene todos los datos del tablero de juego
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]


    lista_botones=[["#/#", "#/#","#/#", "#/#","#/#", "#/#", "#/#", "#/#", "#/#"], #Matriz en la cual se posicionan los botones y etiquetas del tablero 
                   ["#/#", "#/#","#/#", "#/#","#/#", "#/#", "#/#", "#/#", "#/#"],
                   ["#/#", "#/#","#/#", "#/#","#/#", "#/#", "#/#", "#/#", "#/#"],
                   ["#/#", "#/#","#/#", "#/#","#/#", "#/#", "#/#", "#/#", "#/#"],
                   ["#/#", "#/#","#/#", "#/#","#/#", "#/#", "#/#", "#/#", "#/#"],
                   ["#/#", "#/#","#/#", "#/#","#/#", "#/#", "#/#", "#/#", "#/#"],
                   ["#/#", "#/#","#/#", "#/#","#/#", "#/#", "#/#", "#/#", "#/#"],
                   ["#/#", "#/#","#/#", "#/#","#/#", "#/#", "#/#", "#/#", "#/#"],
                   ["#/#", "#/#","#/#", "#/#","#/#", "#/#", "#/#", "#/#", "#/#"]]
        
    #Funciones de juego
    contenido2=leer_archivo() #Se llama a la funcion de leer el archivo para posteriormente crear el tablero
    def crear_tablero(contenido2): #Función que crea el tablero dinámicamente según la partida seleccionada aleatoriamente
        """Función que crea el tablero dinámicamente según la partida seleccionada aleatoriamente"""
        global kakuro2
        global lista_botones2
        for datos in contenido2: #Aquí verifica cada tupla de la partida seleccionada
            fila_columna=datos[0] #Variable que indica si la clave es de fila o columna
            clave=datos[1] #Variable que toma el valor de la clave
            fila=datos[2] #Variable que indica en que fila se posiciona la clave
            columna=datos[3] #Variable que indica en que columna se posiciona la clave
            casillas=datos[4] #Variable que indica cuantas casillas hay para dicha clave
            clave2=""
            if fila_columna==1: #Si la variable es 1, quiere decir que la clave es de fila 
                if kakuro[fila-1][columna-1]!=0: #Aqui verifica si la clave tiene más de un valor, es decir, si tiene un valor de columna
                    for i in kakuro[fila-1][columna-1]:
                        i=str(i)
                        if i=="\\" or i in "1234567890":
                            clave2+=str(i)
                    clave=str(clave)
                    clave=clave2+clave
                else:
                    clave=str(clave)
                    clave="#\\"+clave
                kakuro[fila-1][columna-1]=clave
                clave2=""
                for x in clave:
                    if x=="\\" or x in "1234567890":
                        clave2+=x
                if type(lista_botones[fila-1][columna-1])==Label:
                    lista_botones[fila-1][columna-1].destroy()
                lista_botones[fila-1][columna-1]=Label(juego, bg="black", fg="white", width="6", height="2", text=clave2, justify="right", font=('Bahnschrift SemiBold', 10))
                lista_botones[fila-1][columna-1].grid(row=fila, column=columna)
            if fila_columna==2: #Si la variable es 2, quiere decir que la clave es de columna
                if kakuro[fila-1][columna-1]!=0:#Aqui verifica si la clave tiene más de un valor, es decir, si tiene un valor de fila
                    for i in kakuro[fila-1][columna-1]:
                        i=str(i)
                        if i=="\\" or i in "1234567890":
                            clave2+=str(i)
                    clave=str(clave)+clave2
                else:
                    clave=str(clave)+"\#"                
                kakuro[fila-1][columna-1]=clave
                clave2=""
                for x in clave:
                    if x=="\\" or x in "1234567890":
                        clave2+=x
                if type(lista_botones[fila-1][columna-1])==Label:
                    lista_botones[fila-1][columna-1].destroy()
                lista_botones[fila-1][columna-1]=Label(juego, bg="black", fg="white", width="6", height="2", text=clave2, justify="right", font=('Bahnschrift SemiBold', 10))
                lista_botones[fila-1][columna-1].grid(row=fila, column=columna)
            while casillas>0: #Este ciclo va creando la cantidad de casillas especificadas para cada clave
                if fila_columna==1:
                    columna+=1
                if fila_columna==2:
                    fila+=1
                i=fila-1
                j=columna-1
                if type(lista_botones[i][j])==Button:
                    lista_botones[i][j].destroy()
                lista_botones[i][j]=Button(juego, width="6", height="2",command=lambda i=i, j=j: kakuro_juego(i,j), font=('Bahnschrift SemiBold', 10), state="disabled")
                lista_botones[i][j].grid(row=i+1, column=j+1)
                kakuro[i][j]="#"
                casillas-=1
        for fila in range(0,9): #Este for crea las tuplas de los valores de clave para manipularlos de una manera más sencilla
            num_columna=0
            num_fila=0
            for columna in range(0,9):
                if kakuro[fila][columna]!=0 and kakuro[fila][columna]!="#":
                    bandera=True
                    for datos in kakuro[fila][columna]:
                        if datos=="\\":
                            bandera=False
                        if bandera==True:
                            if datos in "1234567890":
                                num_columna=num_columna*10+int(datos)
                            if datos=="#":
                                num_columna=0
                        else:
                            if datos in "1234567890":
                                num_fila=num_fila*10+int(datos)
                            if datos=="#":
                                num_fila=0
                    kakuro[fila][columna]=(num_columna,num_fila)
                    num_fila=0
                    num_columna=0
        for i in range(0,9): #Crea etiquetas negras en todo el tablero antes de crear las claves y botones
            for j in range(0,9):
                if lista_botones[i][j]=="#/#":
                    lista_botones[i][j]=Label(juego, bg="black", fg="white", width="6", height="2", font=('Bahnschrift SemiBold', 10))
                    lista_botones[i][j].grid(row=i+1, column=j+1)
        kakuro2=kakuro[:] #Copia la matriz del kakuro en la global
        lista_botones2=lista_botones[:] #Copia la matriz de botones en la global
        return contenido2

    #Variables que reinician la partida cada vez que se inicia desde 0
    global contenido
    global nombre
    global nombre_jugador
    global numero_seleccionado
    global num_seleccionado
    global juego_iniciado
    numero_seleccionado=""
    num_seleccionado.set(numero_seleccionado)
    nombre=""
    nombre_jugador.set(nombre)
    contenido=crear_tablero(contenido2)
    juego_iniciado=False
    
    def numero_selec(x): #Función que selecciona el número para ingresarlo a la casilla
        """Función que selecciona el número para ingresarlo a la casilla"""
        global numero_seleccionado
        global num_seleccionado
        global juego_iniciado
        if juego_iniciado==True: #Verifica que el juego ya haya empezado
            if x==1:
                numero_seleccionado=1
            elif x==2:
                numero_seleccionado=2
            elif x==3:
                numero_seleccionado=3
            elif x==4:
                numero_seleccionado=4
            elif x==5:
                numero_seleccionado=5
            elif x==6:
                numero_seleccionado=6
            elif x==7:
                numero_seleccionado=7
            elif x==8:
                numero_seleccionado=8
            elif x==9:
                numero_seleccionado=9
            num_seleccionado.set(numero_seleccionado)
        else: #Si no ha empezado, envía esta señal
            messagebox.showinfo("AVISO", "No se ha iniciado la partida\nHaz click en el botón 'Iniciar Juego'")
        
    def kakuro_juego(i,j): #Función que ingresa valores a la matriz y verifica si se completó el juego
        """Función que ingresa valores a la matriz y verifica si se completó el juego"""
        global jugadas
        global kakuro2
        global lista_botones2
        global numero_seleccionado
        global terminado
        global nombre
        global ultima_jugada
        if numero_seleccionado!="": #Verifica que se haya seleccionado un número
            esta=False
            bandera=True
            bandera2=False
            tupla1=0
            tupla2=0
            tupla3=0
            tupla4=0
            ubicacion_tup1=0
            ubicacion_tup2=0
            ubicacion_tup3=0
            ubicacion_tup4=0
            for numero1 in range(j,-1,-1): #Recorre la matriz hasta encontrarse con una tupla en la misma fila
                if isinstance(kakuro[i][numero1],tuple):
                    if kakuro[i][numero1][1]!=0:
                        tupla1=kakuro[i][numero1]
                        ubicacion_tup1=numero1
                        break
            for numero2 in range(8,j,-1): #Recorre la matriz hasta encontrarse con una tupla en la misma fila, esta vez de atrás para adelante
                if isinstance(kakuro[i][numero2],tuple):
                    if kakuro[i][numero2][1]!=0:
                        tupla2=kakuro[i][numero2]
                        ubicacion_tup2=numero2
                        break
            if ubicacion_tup2==0 or ubicacion_tup1==ubicacion_tup2: #Aqui verifica si encontró o no una tupla
                ubicacion_tup2=9
            if j>ubicacion_tup2: #Aqui verifica si la ubicacion de la columna es mayor a la ubicación de la segunda tupla, para unicamente revisar desde esa tupla hacia la izquierda
                tupla1=tupla2
                tupla2=0
                bandera=False
            if bandera==False: #Bandera que indica si hay más de una tupla en la misma fila, para que revise después de la indicada
                for posicion1 in range(ubicacion_tup2, 9):
                    if kakuro[i][posicion1]==numero_seleccionado and posicion1!=i:
                        messagebox.showinfo("AVISO", "El número ya existe en la fila")
                        esta=True
                        break
            if bandera==True: #Si no hay, verifica en la misma fila completa
                for posicion1 in range(ubicacion_tup1, ubicacion_tup2):
                    if kakuro[i][posicion1]==numero_seleccionado and posicion1!=i:
                        messagebox.showinfo("AVISO", "El número ya existe en la fila")
                        esta=True
                        break
            for numero3 in range(i,-1,-1): #Recorre la matriz de abajo hacia arriba hasta encontrarse con una tupla de la columna
                if isinstance(kakuro[numero3][j], tuple):
                    if kakuro[numero3][j][0]!=0:
                        tupla3=kakuro[numero3][j]
                        ubicacion_tup3=numero3
                        break
            for numero4 in range(i,9): #Recorre la matriz de arriba hacia abajo para buscar la tupla de la columna
                if isinstance(kakuro[numero4][j], tuple):
                    if kakuro[numero4][j][0]!=0:
                        tupla4=kakuro[numero4][j]
                        ubicacion_tup4=numero4
                        break
            if ubicacion_tup4==0 or ubicacion_tup3==ubicacion_tup4: #Verifica si se encontró una segunda tupla, para verificar en toda la columna
                ubicacion_tup4=9
            if i>ubicacion_tup4: #Si la fila en la que se encuentra es mayor a la de la segunda tupla encontrada, verifica hasta esa segunda tupla
                tupla3=tupla4
                tupla4=0
            for posicion2 in range(ubicacion_tup3,ubicacion_tup4): #Verifica si el numero ingresado ya estaba en la columna
                if kakuro[posicion2][j]==numero_seleccionado and posicion2!=i:
                    messagebox.showinfo("AVISO", "El número ya existe en la columna")
                    esta=True
                    break
            if esta==False: #Bandera que indica que no estaba en la misma fila y columna
                suma_fila=numero_seleccionado
                suma_columna=numero_seleccionado
                suma=True
                if numero_seleccionado>tupla1[1]: #Primero verifica que el número no sea mayor al valor de la clave
                    messagebox.showinfo("AVISO", "La sumatoria es mayor a la clave de fila")
                    suma=False
                if j>ubicacion_tup2 and suma==True:
                    for casilla_l in range(ubicacion_tup2,9): #Verifica cada valor de la casilla y los suma para verificar que no se pasó del valor indicado
                        if isinstance(kakuro[i][casilla_l],int):
                            suma_fila+=kakuro[i][casilla_l]
                            if suma_fila>tupla1[1]:
                                messagebox.showinfo("AVISO", "La sumatoria es mayor a la clave de fila")
                                suma=False
                                break
                if ubicacion_tup1<j<ubicacion_tup2 and suma==True: #Verifica cada valor de la casilla y los suma para verificar que no se pasó del valor indicado
                    for casilla_l in range(ubicacion_tup1,ubicacion_tup2):
                        if isinstance(kakuro[i][casilla_l],int):
                            suma_fila+=kakuro[i][casilla_l]
                            if suma_fila>tupla1[1]:
                                messagebox.showinfo("AVISO", "La sumatoria es mayor a la clave de fila")
                                suma=False
                                break
                if numero_seleccionado>tupla3[0]: #Primero verifica que el número no sea mayor al valor de la clave
                    messagebox.showinfo("AVISO", "La sumatoria es mayor a la clave de la columna")
                    suma=False
                if i>ubicacion_tup4 and suma==True: #Verifica cada valor de la casilla y los suma para verificar que no se pasó del valor indicado
                    for casilla_c in range(ubicacion_tup4,9):
                        if isinstance(kakuro[casilla_c][j],int):
                            suma_columna+=kakuro[casilla_c][j]
                            if suma_columna>tupla3[0]:
                                messagebox.showinfo("AVISO", "La sumatoria es mayor a la clave de columna")
                                suma=False
                                break
                if ubicacion_tup3<i<ubicacion_tup4 and suma==True: #Verifica cada valor de la casilla y los suma para verificar que no se pasó del valor indicado
                    for casilla_c in range(ubicacion_tup3,ubicacion_tup4):
                        if isinstance(kakuro[casilla_c][j],int):
                            suma_columna+=kakuro[casilla_c][j]
                            if suma_columna>tupla3[0]:
                                messagebox.showinfo("AVISO", "La sumatoria es mayor a la clave de columna")
                                suma=False
                                break                
                if suma==True: #Bandera que indica si la suma era menor o igual al valor de la clave
                    jugadas+=[[i,j,numero_seleccionado]] #Agrega la ubicación de la casilla a las jugadas
                    lista_botones[i][j].configure(text=str(numero_seleccionado)) #Cambia el valor del botón
                    kakuro[i][j]=numero_seleccionado #Ingresa el número a la matriz del kakuro
                    kakuro2=kakuro[:] 
                    lista_botones2=lista_botones[:]
                    for fila in range(0,9): #Revisa si ya se completó el kakuro
                        for columna in range(0,9):
                            if kakuro[fila][columna]=="#":
                                bandera2=False
                                break
                            else:
                                bandera2=True
                        if bandera2==False:
                            break
                    if bandera2==True: #Si ya se completó el tablero, pasará a verificar que todos los valores sean correctos
                        terminado=False
                        bandera3=False
                        bandera4=True
                        bandera5=True
                        suma_filas=0
                        suma_columnas=0
                        for fila in range(0,9):
                            if bandera5==True:
                                for columna in range(0,9):
                                    if bandera4==True:
                                        if isinstance(kakuro[fila][columna],tuple): #Verifica si el elemento en la matriz es una tupla
                                            if kakuro[fila][columna][0]!=0: #Verifica si la tupla tiene clave de columna, asi revisa todas las filas 
                                                suma_columnas=0
                                                for fila2 in range(fila+1,9):
                                                    if isinstance(kakuro[fila2][columna],int): #Si se encuentra un entero, lo suma a la variable de la suma de las columnas
                                                        suma_columnas+=kakuro[fila2][columna]
                                                    elif isinstance(kakuro[fila2][columna],tuple): #Si se encuentra con otra tupla, verifica si la suma es igual al valor, si no, envía el mensaje de que casi lo completa al 100%
                                                        if suma_columnas==kakuro[fila][columna][0]:
                                                            bandera3=True
                                                            suma_columnas=0
                                                            break
                                                        else:
                                                            bandera3=False
                                                            suma_columnas=0
                                                            break
                                                if bandera3==False:
                                                    messagebox.showinfo("AVISO", "¡CASI!, NO COMPLETASTE EL KAKURO CORRECTAMENTE\nREVISALO E INTENTALO DE NUEVO")
                                                    bandera4=False
                                                    break
                                            if kakuro[fila][columna][1]!=0: #Verifica si la tupla tiene clave de fila, asi revisa todas las columnas
                                                suma_filas=0
                                                for columna2 in range(columna+1,9): #Si se encuentra un entero, lo suma a la variable de la suma de las filas
                                                    if isinstance(kakuro[fila][columna2],int):
                                                        suma_filas+=kakuro[fila][columna2]
                                                    elif isinstance(kakuro[fila][columna2],tuple):#Si se encuentra con otra tupla, verifica si la suma es igual al valor, si no, envía el mensaje de que casi lo completa al 100%
                                                        if suma_filas==kakuro[fila][columna][1]:
                                                            bandera3=True
                                                            suma_filas=0
                                                            break
                                                        else:
                                                            suma_filas=0
                                                            bandera3=False
                                                            break
                                                if bandera3==False:
                                                    messagebox.showinfo("AVISO", "¡CASI!, NO COMPLETASTE EL KAKURO CORRECTAMENTE\nREVISALO E INTENTALO DE NUEVO")
                                                    bandera4=False
                                                    break
                                    else:
                                        bandera5=False
                                        break
                            else:
                                break              
                        if bandera3==True and bandera4==True and bandera5==True: #Aqui verifica que todas las banderas estén correctamente
                            terminado=True #Aqui indica que ya terminó el tablero correctamente
                            pygame.mixer.music.load("smb_stage_clear.wav") #Toca la cancioncita de Mario Bros
                            pygame.mixer.music.play()
                            aviso="¡FELICIDADES "+str(nombre)+"!, COMPLETASTE CORRECTAMENTE EL KAKURO"
                            messagebox.showinfo("AVISO", aviso) #Envia el mensaje que se completó correctamente el tablero
                            escribir_top10()
        else:
            messagebox.showinfo("AVISO", "¡No has seleccionado un número!")

    def escribir_top10():
        global tiempo_partida
        global tiempo_jugado
        global nombre
        top=open("kakurotop10.txt",'r') #Lee el archivo del top 10
        lineas=top.readlines()
        lista_ganadores=[]
        for nivel in lineas: #Agarra los elementos del archivo de texto
            lista_ganadores.append(eval(nivel))
        top.close()
        archivo_config=open("kakuro2018config.txt","r") #Lee los datos del archivo de la configuracion de la partida
        dato=archivo_config.readline()
        dato=eval(dato)
        nivel=eval(dato[0])
        indicador_timer_reloj=dato[1]
        tiempo1=eval(dato[2])
        bandera=False
        if indicador_timer_reloj=="Timer": #Verifica si usaba timer
            diferencia=tiempo_partida-tiempo_jugado
            if nivel==1: #Verifica si el nivel jugado era el 1
                for jugador in lista_ganadores[0]:
                    if jugador[1]>diferencia: #Revisa en la primer lista si el tiempo fue mejor a alguno
                        indice=lista_ganadores[0].index(jugador)
                        lista_ganadores[0].insert(indice,[nombre,diferencia])
                        bandera=True
                        break
                if bandera==False: #Si no fue mejor, lo mete de último
                    lista_ganadores[0].append([nombre,diferencia])
                if len(lista_ganadores[0])>10: #Revisa a ver si la lista se excedió de 10 elementos
                    lista_ganadores[0].pop()
            elif nivel==2: #Verifica si el nivel era el 2
                for jugador in lista_ganadores[1]:
                    if jugador[1]>diferencia: #Revisa en la segunda lista si el tiempo fue mejor a alguno
                        indice=lista_ganadores[1].index(jugador)
                        lista_ganadores[1].insert(indice,[nombre,diferencia])
                        bandera=True
                        break
                if bandera==False: #Si no fue mejor, lo mete de último
                    lista_ganadores[1].append([nombre,diferencia])
                if len(lista_ganadores[1])>10: #Revisa a ver si la lista se excedió de 10 elementos
                    lista_ganadores[1].pop()
            else:
                for jugador in lista_ganadores[2]:
                    if jugador[1]>diferencia:  #Revisa en la tercer lista si el tiempo fue mejor a alguno
                        indice=lista_ganadores[2].index(jugador)
                        lista_ganadores[2].insert(indice,[nombre,diferencia])
                        bandera=True
                        break
                if bandera==False: #Si no fue mejor, lo mete de último
                    lista_ganadores[2].append([nombre,diferencia])
                if len(lista_ganadores[2])>10: #Revisa a ver si la lista se excedió de 10 elementos
                    lista_ganadores[2].pop()
        elif indicador_timer_reloj=="Si": #Realiza el proceso anterior pero esta vez con el tiempo del reloj
            if nivel==1:
                for jugador in lista_ganadores[0]:
                    if jugador[1]>tiempo_jugado:
                        indice=lista_ganadores[0].index(jugador)
                        lista_ganadores[0].insert(indice,[nombre,tiempo_jugado])
                        bandera=True
                        break
                if bandera==False:
                    lista_ganadores[0].append([nombre,tiempo_jugado])
                if len(lista_ganadores[0])>10:
                    lista_ganadores[0].pop()
            elif nivel==2:
                for jugador in lista_ganadores[1]:
                    if jugador[1]>tiempo_jugado:
                        indice=lista_ganadores[1].index(jugador)
                        lista_ganadores[1].insert(indice,[nombre,tiempo_jugado])
                        bandera=True
                        break
                if bandera==False:
                    lista_ganadores[1].append([nombre,tiempo_jugado])
                if len(lista_ganadores[1])>10:
                    lista_ganadores[1].pop()
            else:
                for jugador in lista_ganadores[2]:
                    if jugador[1]>tiempo_jugado:
                        indice=lista_ganadores[2].index(jugador)
                        lista_ganadores[2].insert(indice,[nombre,tiempo_jugado])
                        bandera=True
                        break
                if bandera==False:
                    lista_ganadores[2].append([nombre,tiempo_jugado])
                if len(lista_ganadores[2])>10:
                    lista_ganadores[2].pop()
        top_2=open("kakurotop10.txt",'w')
        for elemento in lista_ganadores: #Sobreescribe el archivo de nuevo
            top_2.write(str(elemento)+"\n")
        top_2.close()
        archivo_config.close()

    def deshacer_jugadas(): #Función que borra las jugadas anteriores
        """Función que borra las jugadas anteriores"""
        global lista_botones2
        global kakuro2
        global jugadas
        global recuperar_jugadas
        global juego_iniciado
        if juego_iniciado==True:
            if len(jugadas)>=1: #Veirifica si hay jugadas por borrar
                pygame.mixer.music.load("smb_kick.wav")
                pygame.mixer.music.play()
                fila_matriz=jugadas[-1][0]
                columna_matriz=jugadas[-1][1]
                lista_botones[fila_matriz][columna_matriz].configure(text="")
                kakuro[fila_matriz][columna_matriz]="#"
                lista_botones2=lista_botones[:]
                kakuro2=kakuro[:]
                recuperar_jugadas+=[jugadas[-1]]
                del jugadas[-1] #Borra la última jugada
            else:
                messagebox.showinfo("AVISO", "¡No hay jugadas por borrar!")
        else:
            messagebox.showinfo("AVISO", "¡No se ha iniciado la partida!\nHaz click en el botón 'Iniciar Juego'")

    def rehacer_jugadas(): #Función que rehace las jugadas anteriormente borradas
        """Función que rehace las jugadas anteriormente borradas"""
        global lista_botones2
        global kakuro2
        global jugadas
        global recuperar_jugadas 
        global juego_iniciado
        if juego_iniciado==True:
            if len(recuperar_jugadas)>=1: #Veirifica si hay jugadas por recuperar
                pygame.mixer.music.load("mario-coin.mp3")
                pygame.mixer.music.play()
                fila_matriz=recuperar_jugadas[-1][0]
                columna_matriz=recuperar_jugadas[-1][1]
                lista_botones[fila_matriz][columna_matriz].configure(text=recuperar_jugadas[-1][2])
                kakuro[fila_matriz][columna_matriz]=recuperar_jugadas[-1][2]
                lista_botones2=lista_botones[:]
                kakuro2=kakuro[:]
                jugadas+=[recuperar_jugadas[-1]]
                del recuperar_jugadas[-1] #Recupera la última jugada
            else:
                messagebox.showinfo("AVISO", "¡No hay jugadas por recuperar!")
        else:
            messagebox.showinfo("AVISO", "¡No se ha iniciado la partida!\nHaz click en el botón 'Iniciar Juego'")

    def borrar_juegototal(): #Función que borra todas las jugadas
        """Función que borra todas las jugadas"""
        global jugadas
        global juego_iniciado
        if juego_iniciado==True: #Verifica si ya se inició la partida
            continuar_jugando=messagebox.askquestion("Borrar todo el juego","¿Querés borrar todo el juego?")
            if continuar_jugando=="yes": #Si el usuario selecciona que si, empieza desde 0 el juego
                if len(jugadas)>=1: #Verifica si hay jugadas por borrar
                    while jugadas!=[]:
                        pygame.mixer.music.load("smb_kick.wav")
                        pygame.mixer.music.play()
                        fila_matriz,columna_matriz=jugadas[-1]
                        lista_botones[fila_matriz][columna_matriz].configure(text="")
                        kakuro[fila_matriz][columna_matriz]="#"
                        lista_botones2=lista_botones[:]
                        kakuro2=kakuro[:]
                        del jugadas[-1]
                else:
                    messagebox.showinfo("AVISO", "¡No hay jugadas por borrar!")
        else:
            messagebox.showinfo("AVISO", "No se ha iniciado la partida\nHaz click en el botón 'Iniciar Juego'")
        
    def iniciar_partida(): #Función que se ejecuta cuando se selecciona el botón "Iniciar Juego"
        """Función que se ejecuta cuando se selecciona el botón "Iniciar Juego"""
        """Inicia el tiempo y habilita los botones para que se puedan ingresar números"""
        global lista_botones2
        global juego_iniciado
        global nombre
        global nombre_jugador
        nombre=nombre_jugador.get()
        if nombre!="": #Verifica si se ingresó un nombre
            if len(nombre)<=30: #Verifica que el nombre posea un máximo de 30 caracteres
                pygame.mixer.music.load("Cancion_juego.mp3") #Toca una cancioncita para transmitir buena vibra :3
                pygame.mixer.music.play()
                saludo_usuario="Buena suerte "+str(nombre)+" :)" 
                messagebox.showinfo("PARTIDA INICIADA", saludo_usuario) #Saluda al usuario y le desea buena suerte
                entrar_nombre.config(state="disabled")
                juego_iniciado=True
                for fila in range(0,9):
                    for columna in range(0,9):
                        if type(lista_botones[fila][columna])==Button: #Verifica todas las filas y columnas de la lista de botones y los habilita
                            lista_botones[fila][columna].config(state="normal")
                lista_botones2=lista_botones[:]
                funcion_de_reloj=threading.Thread(name="Reloj_hilo",target=inicio_tiempo) #Crea un hilo para ejecutar el timer o el reloj
                funcion_de_reloj.start()
            else:
                messagebox.showinfo("AVISO", "Ingrese un nombre con 30 caracteres o menos")
        else:
            messagebox.showinfo("AVISO", "Ingrese su nombre antes de comenzar")

    def inicio_tiempo(): #Funcion que inicializa el proceso para desplegar el reloj o el timer
        """Funcion que inicializa el proceso para desplegar el reloj o el timer"""
        global tiempo_de_partida
        archivo_config=open("kakuro2018config.txt","r") #Lee los datos del archivo de la configuracion de la partida
        dato=archivo_config.readline()
        dato=eval(dato)
        indicador_timer_reloj=dato[1]
        tiempo1=eval(dato[2])
        if indicador_timer_reloj=="Timer": #Verifica si se escogió timer o reloj
            reloj_pantalla(indicador_timer_reloj,tiempo1)
        else:
            tiempo1=0
            reloj_pantalla(indicador_timer_reloj,tiempo1)
            return   
        archivo_config.close()

    def reloj_pantalla(indicador, contador): #Función que va convirtiendo los segundos totales a horas, minutos y segundos
        """Función que va convirtiendo los segundos totales a horas, minutos y segundos"""
        global tiempo_de_partida
        global terminado
        global tiempo_jugado
        global juego_iniciado
        try:
            tiempo_partida=contador
            lista_num=["0","1","2","3","4","5","6","7","8","9"] #Lista de numeros individuales 
            if indicador=="Si": #Si el indicador es si, quiere decir que el usuario desea ver el reloj en pantalla
                contador=0
                while contador<=10800 and terminado==False and juego_iniciado==True: #Verifica que el juego no se haya terminado todavía
                    time.sleep(1)
                    horas=contador//3600
                    minutos=(contador%3600)//60
                    segundos=(contador%3600)%60
                    contador+=1
                    if str(horas) in lista_num:
                        horas="0"+str(horas)
                    else:
                        horas=str(horas)
                    if str(minutos) in lista_num:
                        minutos="0"+str(minutos)
                    else:
                        minutos=str(minutos)
                    if str(segundos) in lista_num:
                        segundos="0"+str(segundos)
                    else:
                        segundos=str(segundos)
                    variable_tiempo=horas+":"+minutos+":"+segundos
                    tiempo.config(text=variable_tiempo)
                if terminado==True: #Si el juego ya se completó al 100%, envia el tiempo actual a una variable global
                    tiempo_jugado=contador
                if terminado==False and juego_inciado==True: #Si no ha completado el juego al 100%, envía una alerta
                    messagebox.showinfo("Run out of time","Se ha acabado el tiempo :(")
                    for fila in range(0,9):
                        for columna in range(0,9): #Desahibilita todos los botones para que el usuario no pueda seguir jugando
                            if type(lista_botones[fila][columna])==Button:
                                lista_botones[fila][columna].config(state="disabled")
            elif indicador=="Timer": #Si el indicador es Timer, entonces quiere decir que el usuario ingresó un tiempo especifico
                while contador>=0 and terminado==False and juego_iniciado==True:
                    time.sleep(1)
                    horas=contador//3600
                    minutos=(contador%3600)//60
                    segundos=(contador%3600)%60
                    contador-=1
                    if str(horas) in lista_num:
                        horas="0"+str(horas)
                    else:
                        horas=str(horas)
                    if str(minutos) in lista_num:
                        minutos="0"+str(minutos)
                    else:
                        minutos=str(minutos)
                    if str(segundos) in lista_num:
                        segundos="0"+str(segundos)
                    else:
                        segundos=str(segundos)
                    variable_tiempo=horas+":"+minutos+":"+segundos
                    tiempo.config(text=variable_tiempo)
                if terminado==True: #Si el juego ya se completó al 100%, envia el tiempo actual a una variable global
                    tiempo_jugado=contador
                if terminado==False and juego_inciado==True:#Si no ha completado el juego al 100%, envía una alerta
                    continuar_jugando=messagebox.askquestion("Run out of time","Se terminó el tiempo :(\n¿Quieres seguir jugando?")
                    if continuar_jugando=="no":#Si no quiere seguir jugando, cierra el juego
                        juego.destroy()
        except:
            messagebox.showinfo("Partida Cancelada","Hasta pronto!")
            
                
    def guardar_partida(): #Función que guarda la partida en un archivo de texto
        """Función que guarda la partida en un archivo de texto"""
        global kakuro2
        global nombre
        global jugadas
        string_matriz=str(kakuro2)
        string_nombre=str(nombre)
        string_jugadas=str(jugadas)
        borra_partida=open('Partida Guardada.txt','w')
        borra_partida.close()
        partida=open('Partida Guardada.txt','a')
        partida.write(string_matriz+"\n"+string_nombre+"\n"+string_jugadas)
        messagebox.showinfo("AVISO", "La partida se ha guardado correctamente")
        partida.close()

    def cargar_juego(): #Función que carga la partida guardada
        """Función que carga la partida guardada"""
        global contenido
        global kakuro2
        global lista_botones2
        global juego_iniciado
        global nombre
        global nombre_jugador
        global jugadas
        partida=open('Partida Guardada.txt','r')
        lineas=partida.readlines()
        cont=0
        kakuro3=0
        name=""
        jugadas_1=0
        for dato in lineas: #Este ciclo extrae cada una de los datos de la partida guardada
            if cont==0:
                kakuro3=dato
                cont+=1
            elif cont==1:
                name=dato
                cont+=1
            else:
                jugadas_1=dato
        nombre=name
        nombre_jugador.set(nombre)
        jugadas_1=eval(jugadas_1)
        jugadas=[]
        jugadas=jugadas_1[:]
        kakuro3=eval(kakuro3)
        juego_iniciado=False
        for fila in range(0,9): 
            for columna in range(0,9): #Aqui se encarga de destruir el juego anterior para crear el nuevo tablero
                lista_botones[fila][columna].destroy()
                lista_botones[fila][columna]="#/#"
                kakuro[fila][columna]=0
        for fila in range(0,9):
            for columna in range(0,9): #En este ciclo crea de nuevo las etiquetas y botones según los valores de la matriz guardada
                kakuro[fila][columna]=kakuro3[fila][columna] #Aqui asigna a el kakuro ya reiniciado, el valor del kakuro guardado
                if kakuro3[fila][columna]==0: #Si es un 0, quiere decir que es un label en negro
                    lista_botones[fila][columna]=Label(juego, bg="black", fg="white", width="6", height="2", font=('Bahnschrift SemiBold', 10))
                    lista_botones[fila][columna].grid(row=fila+1, column=columna+1)
                elif isinstance(kakuro3[fila][columna],tuple): #Si es una tupla, quiere decir que va un label con clave
                    clave=""
                    if kakuro3[fila][columna][0]!=0:
                        clave=str(kakuro3[fila][columna][0])+"\\"
                    if kakuro3[fila][columna][1]!=0:
                        if clave=="":
                            clave="\\"+str(kakuro3[fila][columna][1])
                        else:
                            clave+=str(kakuro3[fila][columna][1])
                    lista_botones[fila][columna]=Label(juego, text=clave, bg="black", fg="white", width="6", height="2", font=('Bahnschrift SemiBold', 10))
                    lista_botones[fila][columna].grid(row=fila+1, column=columna+1)
                else:
                    i=fila
                    j=columna
                    if kakuro3[fila][columna]=="#": #Si está un numeral quiere decir que no se ha ingresado valores en ese botón
                        lista_botones[fila][columna]=Button(juego, width="6", height="2",command=lambda i=i, j=j: kakuro_juego(i,j), font=('Bahnschrift SemiBold', 10), state="disabled")
                        lista_botones[fila][columna].grid(row=i+1, column=j+1)
                    else: #La otra opción es que tenga un número entonces se le asigna directamente al botón
                        texto=str(kakuro3[fila][columna])
                        lista_botones[fila][columna]=Button(juego, width="6", height="2",command=lambda i=i, j=j: kakuro_juego(i,j), text=texto, font=('Bahnschrift SemiBold', 10), state="disabled")
                        lista_botones[fila][columna].grid(row=i+1, column=j+1)
        partida.close()
        
    def terminar_de_jugar(): #Función que finaliza el juego cuando el usuario lo desee
        """Función que finaliza el juego cuando el usuario lo desee"""
        global juego_iniciado
        global numero_seleccionado
        global num_seleccionado
        global nombre
        global nombre_jugador
        if juego_iniciado==True:
            continuar_jugando=messagebox.askquestion("Terminar Juego","¿Quieres terminar de jugar?")
            if continuar_jugando=="yes": #Si el usuario dice que si, crea otra ventana nueva
                numero_seleccionado=""
                num_seleccionado.set(numero_seleccionado)
                nombre=""
                nombre_jugador.set(nombre)
                juego.destroy()
                a_jugar()
        else:
            messagebox.showinfo("AVISO", "No se ha iniciado la partida\nHaz click en el botón 'Iniciar Juego'")
    #Parte gráfica    
    #Numeros
    numero1=Button(juego, width="8", height="2", text="1", fg="black", bg="red", font=('Bahnschrift SemiBold', 10), command=lambda: numero_selec(1))
    numero1.grid(row=2, column=12)

    numero2=Button(juego, width="8", height="2", text="2", fg="black", bg="blue", font=('Bahnschrift SemiBold', 10), command=lambda: numero_selec(2))
    numero2.grid(row=3, column=12)

    numero3=Button(juego, width="8", height="2", text="3", fg="black", bg="green", font=('Bahnschrift SemiBold', 10), command=lambda: numero_selec(3))
    numero3.grid(row=4, column=12)

    numero4=Button(juego, width="8", height="2", text="4", fg="black", bg="yellow", font=('Bahnschrift SemiBold', 10), command=lambda: numero_selec(4))
    numero4.grid(row=5, column=12)

    numero5=Button(juego, width="8", height="2", text="5", fg="black", bg="turquoise", font=('Bahnschrift SemiBold', 10), command=lambda: numero_selec(5))
    numero5.grid(row=6, column=12)

    numero6=Button(juego, width="8", height="2", text="6", fg="black", bg="pink", font=('Bahnschrift SemiBold', 10), command=lambda: numero_selec(6))
    numero6.grid(row=7, column=12)

    numero7=Button(juego, width="8", height="2", text="7", fg="black", bg="plum", font=('Bahnschrift SemiBold', 10), command=lambda: numero_selec(7))
    numero7.grid(row=8, column=12)

    numero8=Button(juego, width="8", height="2", text="8", fg="black", bg="brown", font=('Bahnschrift SemiBold', 10), command=lambda: numero_selec(8))
    numero8.grid(row=9, column=12)

    numero9=Button(juego, width="8", height="2", text="9", fg="black", bg="gold", font=('Bahnschrift SemiBold', 10), command=lambda: numero_selec(9))
    numero9.grid(row=10, column=12)

    #Ingreso de nombre
    entrar_nombre=Entry(juego, textvariable=nombre_jugador, width="40", bg="orange", fg="black", font=('Bahnschrift SemiBold', 10))
    entrar_nombre.grid(row=11, column=2, columnspan=6)

    #Numero seleccionado
    seleccion=Label(juego, textvariable=num_seleccionado, width="8", height="2", bg="silver", font=('Bahnschrift SemiBold', 10), fg="black")
    seleccion.grid(row=1, column=12)

    #Botones de partida
    #Iniciar juego
    inicio_juego=Button(juego, width="8", height="2", text="Iniciar\nJuego", fg="black", bg="gold", font=('Bahnschrift SemiBold', 10), command=lambda: iniciar_partida())
    inicio_juego.grid(row=12, column=1)

    #Deshacer jugada
    deshacer_jugada=Button(juego, width="8", height="2", text="Deshacer\nJugada", fg="black", bg="light blue", font=('Bahnschrift SemiBold', 10), command=lambda: deshacer_jugadas())
    deshacer_jugada.grid(row=12, column=3)

    rehacer_jugada=Button(juego, width="8", height="2", text="Rehacer\nJugada", fg="black", bg="red", font=('Bahnschrift SemiBold', 10), command=lambda: rehacer_jugadas())
    rehacer_jugada.grid(row=12, column=5)

    #Terminar juego
    terminar_juego=Button(juego, width="8", height="2", text="Terminar\nJuego", fg="black", bg="light green", font=('Bahnschrift SemiBold', 10), command=lambda: terminar_de_jugar())
    terminar_juego.grid(row=12, column=7)

    #Borrar juego
    borrar_juego=Button(juego, width="8", height="2", text="Borrar\nJuego", fg="black", bg="dark turquoise", font=('Bahnschrift SemiBold', 10), command=lambda: borrar_juegototal())
    borrar_juego.grid(row=12, column=9)

    #Top 10
    top10=Button(juego, width="8", height="2", text="Top\n10", fg="black", bg="white", font=('Bahnschrift SemiBold', 10), command=lambda: top_10())
    top10.grid(row=12, column=12)

    #Tiempo
    Label(juego, width="7", fg="black", bg="light grey", font=('Bahnschrift SemiBold', 10), text="Tiempo").grid(row=13, column=1, columnspan=3)

    #Guardar partida
    guardar_juego=Button(juego, width="8", height="2", text="Guardar\nPartida", fg="black", bg="blue", font=('Bahnschrift SemiBold', 10), command=lambda: guardar_partida()).grid(row=14, column=9)

    #Cargar partida
    cargar_partida=Button(juego, width="8", height="2", text="Cargar\nPartida", fg="black", bg="blue", font=('Bahnschrift SemiBold', 10), command=lambda: cargar_juego()).grid(row=15, column=9)

    #Etiquetas donde se desplegará las horas
    tiempo=Label(juego, width="20", height="2", fg="black", bg="white", font=('Bahnschrift SemiBold', 10))
    tiempo.grid(row=14, column=1, columnspan=3)


    #Etiquetas para mejorar la interfaz
    Label(juego, width="4", bg="light grey", height="2").grid(row=12, column=0)
    Label(juego, width="8", bg="light grey", height="2").grid(row=2, column=11)
    Label(juego, width="3", bg="light grey").grid(row=1, column=0)
    Label(juego, width="8", height="3", bg="light grey").grid(row=0, column=1)
    Label(juego, width="18", height="3", bg="light grey", text="Nombre del jugador:", fg="black", font=('Bahnschrift SemiBold', 10)).grid(row=11, column=0, columnspan=2)
    


#Frame
ventana_menu=Frame(raiz)
ventana_menu.config(width="690", height="690", bg="gold", relief="sunken", bd=10)
ventana_menu.pack()

#Saludo Inicial
saludo=Label(ventana_menu,font=("Gang of Three", 30), fg="black", bg="gold", text="Bienvenidos a Kakuro\n2.0").place(x=130, y=10)


#Botones funcionales
#Jugar
botonjugar=Button(ventana_menu, width="12", text= "A darle!", font=("Gang of Three", 20), bg="red", fg="black", command=lambda: a_jugar())
botonjugar.place(x=255, y=110)

#Configurar
botonconfig=Button(ventana_menu, width="16", text= "Configuración", font=("Gang of Three", 20), bg="silver", fg="black", command=lambda: configuracion())
botonconfig.place(x=220, y=200)

#Acerca de
botonacercade=Button(ventana_menu, width="12", text= "Acerca de", font=("Gang of Three", 20), bg="silver", fg="black", command=lambda: acerca_de())
botonacercade.place(x=255, y=300)

#Ayuda
botonayuda=Button(ventana_menu, width="12", text= "Ayuda", font=("Gang of Three", 20), bg="silver", fg="black", command=lambda: ayuda())
botonayuda.place(x=255, y=400)

#Salir
botonsalir=Button(ventana_menu, width="12", text= "Get me out", font=("Gang of Three", 20), bg="silver", fg="black", command=lambda: salir())
botonsalir.place(x=255, y=500)

raiz.mainloop()
