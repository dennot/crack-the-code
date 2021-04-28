# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 13:14:17 2021

@author: agsan
"""
import random
import PySimpleGUI as sg

def randomNumberLock():
    lock_code = random.sample(range(0, 9), 3)
    return lock_code

def pista1(Code):                                 #Crear funcion pista 1 (Numero esta bien y bien ubicado)
    
    correct_number = random.choice(Code)          #random.choice elige un numero al azar de la lista de Codigo, 
                                                  #generando un numero correcto que se le es asignado a correct_number.
    
    sample_list = list(range(10))                 #Crea lista inicial, en el siguiente for loop se remueven los 
    for i in Code:                                #elementos del Codigo para que no sean repetidos en el momento
        sample_list.remove(i)                     #de asignarlos a la pista.  
        
    pista1 = random.sample(sample_list, 2)        #De la lista anterior, se toman 2 numeros para asignarle a la pista
    pista1.append((correct_number))               #y se le asigna el numero correcto al final de la lista.

    for n in Code:                                              #Este nested for loop compara individualmente cada 
        for i in range(len(pista1)):                            #numero en Code con todos los numeros de la pista1
            if n == pista1[i]:                                  #para encontrar el numero correcto y posicionarlo
                j = Code.index(n)                               #en la posicion correcta mediante los indices.
                pista1[i], pista1[j] = pista1[j], pista1[i]
                break

    return pista1

def pista2(Code):                                 #Crear funcion pista 2 (Numero esta bien pero mal ubicado)
    
    global correct_number2                        #Se declara la variable como global para la pista 4
    
    correct_number2 = random.choice(Code)         #random.choice elige un numero al azar de la lista de Codigo, 
                                                  #generando un numero correcto que se le es asignado a correct_number.
    
    sample_list = list(range(10))                 #Crea lista inicial, en el siguiente for loop se remueven los 
    for i in Code:                                #elementos del Codigo para que no sean repetidos en el momento
        sample_list.remove(i)                     #de asignarlos a la pista.  
        
    pista2 = random.sample(sample_list, 2)        #De la lista anterior, se toman 2 numeros para asignarle a la pista
    pista2.append((correct_number2))              #y se le asigna el numero correcto al final de la lista, despues de
    random.shuffle(pista2)                        #eso se mueven los valores de forma aleatoria con el proposito de
                                                  #que el numero correcto no quede en la ultima posicion.
    
    for i in range(len(Code)):                    #Dentro de este for loop se checa si el numero correcto no queda en
        while pista2[i] == Code[i]:               #la misma posicion que un numero dentro del codigo original, si se
            random.shuffle(pista2)                #cumple True, se vuelven a mover los valores.
          
    return pista2

def pista3(Code):                                 #Crear funcion pista 3 (Ningun numero esta bien)
    
    sample_list = list(range(10))                 #Crea lista inicial, en el siguiente for loop se remueven los 
    for i in Code:                                #elementos del Codigo para que no sean repetidos en el momento
        sample_list.remove(i)                     #de asignarlos a la pista. 

    pista3 = random.sample(sample_list, 3)        #Asigna 3 numeros aleatorios de la lista.
           
    return pista3

def pista4(Code):                                 #Crear funcion pista 4 (Numero esta bien pero mal ubicado)
    
    numbers = random.sample(Code, 3)              #Se crea una nueva lista conteniendo los numeros del codigo y se
    global correct_number2                        #llama a la funcion global para quitar de la lista el numero que
    numbers.remove(correct_number2)               #se utilizo para la pista 2.
    
    correct_number = random.choice(numbers)       #random.choice elige un numero al azar de la nueva lista numbers y se 
                                                  #generando un numero correcto que se le es asignado a correct_number.
    
    sample_list = list(range(10))                 #Crea lista inicial, en el siguiente for loop se remueven los 
    for i in Code:                                #elementos del Codigo para que no sean repetidos en el momento
        sample_list.remove(i)                     #de asignarlos a la pista.  
        
    pista4 = random.sample(sample_list, 2)        #De la lista anterior, se toman 2 numeros para asignarle a la pista
    pista4.append((correct_number))               #y se le asigna el numero correcto al final de la lista, despues de
    random.shuffle(pista4)                        #eso se mueven los valores de forma aleatoria con el proposito de
                                                  #que el numero correcto no quede en la ultima posicion.
    
    for i in range(len(Code)):                    #Dentro de este for loop se checa si el numero correcto no queda en
        while pista4[i] == Code[i]:               #la misma posicion que un numero dentro del codigo original, si se
            random.shuffle(pista4)                #cumple True, se vuelven a mover los valores.
          
    return pista4

def pista5(Code):                                 #Crear funcion pista 5 (Dos numeros estan bien pero mal ubicados)
    
    pista5 = random.sample(Code, 2)               #Crea una lista con 2 numeros aleatorios de Code, al usar la funcion
                                                  #sample los numeros no se repiten.
    
    sample_list = list(range(10))                 #Crea lista inicial, en el siguiente for loop se remueven los 
    for i in Code:                                #elementos del Codigo para que no sean repetidos en el momento
        sample_list.remove(i)                     #de asignarlos a la pista.  
        
    random_number = random.choice(sample_list)    #De la lista anterior, se toma 1 numero para asignarle a la pista
    pista5.append((random_number))                #y se le asigna el numero incorrecto al final de la lista.
    
    for i in range(len(Code)):                    #Dentro de este for loop se checa si los numeros correctos no quedan
        while pista5[i] == Code[i]:               #en la misma posicion que los numeros dentro del codigo original, si 
            random.shuffle(pista5)                #se cumple True, se vuelven a mover los valores.
          
    return pista5

Code = randomNumberLock()
user_tries = 0
user_code = []
print(Code)

sg.theme('BluePurple')

layout = [[sg.Text('La pista 1 (Un numero esta bien y bien ubicado) es:'), sg.Text(size=(15,1))],
          [sg.Text(pista1(Code)), sg.Text(size=(15,1))],
          [sg.Text('La pista 2 (Un numero esta bien pero mal ubicado) es:'), sg.Text(size=(15,1))],
          [sg.Text(pista2(Code)), sg.Text(size=(15,1))],
          [sg.Text('La pista 3 (Ningun numero esta bien) es:'), sg.Text(size=(15,1))],
          [sg.Text(pista3(Code)), sg.Text(size=(15,1))],
          [sg.Text('La pista 4 (Un numero esta bien pero mal ubicado) es:'), sg.Text(size=(15,1))],
          [sg.Text(pista4(Code)), sg.Text(size=(15,1))],
          [sg.Text('La pista 5 (Dos numeros estan bien pero mal ubicados) es:'), sg.Text(size=(15,1))],
          [sg.Text(pista5(Code)), sg.Text(size=(15,1))],
          
          [sg.Text('Ingresa un codigo de 3 digitos: '), sg.Text(size=(15,1), key='-OUTPUT-')],
          
          [sg.Button('1'), sg.Button('2'), sg.Button('3'),
           sg.Button('4'), sg.Button('5'), sg.Button('6'),
           sg.Button('7'), sg.Button('8'), sg.Button('9'),
           sg.Button('0'), sg.Button('Check'), sg.Button('Exit')]]

window = sg.Window('Crack The Code', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    if event in ('0123456789'):
               
        if len(user_code) < 3:
            user_code.append(event)
            print(user_code)
            
    elif event == 'Check':
        
        if len(user_code) == 3:
            user_code = [int(x) for x in user_code]
            
            if user_code == Code:
                sg.popup('¡Felicidades, ganaste!')
                window.close()
            
            elif user_tries == 2:
                user_tries +=1
                sg.popup('Te has quedado sin intentos')
                window.close()
            
            else:
                user_tries +=1
                sg.popup(('Tienes', 3 - user_tries, 'intento/s para resolver el codigo.'))
                user_code = []
                
        else:
            sg.popup(('Ingresa un codigo valido de 3 digitos',
                      'Tu codigo:', user_code))
                
        

window.close()