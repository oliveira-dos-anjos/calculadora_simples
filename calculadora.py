from distutils.log import debug
from tkinter import *

root = Tk()
root.title('calculadora')
root.resizable(False, False)
root['bg'] = 'lightgreen' 

img = PhotoImage(file='C:\\Users\\RAFAEL\\Desktop\\calculadora\\calculadora_simples\\png.png')
root.iconphoto(True, img)

def click_button(num):
    atual = visor.get()
    visor.delete(0, END)
    visor.insert(END, str(atual) + str(num))


def click_delete():
    visor.delete(0, END)


def click_ponto():
    tela = str(visor.get())
    if '.' in tela:
        ''
    else:
        if len(tela) == 0:
            visor.insert(END, '0')

        return visor.insert(END, '.')




def click_adição():
    primeiro_numero = str(visor.get())
    global p_numero
    global matematica
    matematica = 'adição'
    if '.' in primeiro_numero:
        p_numero = float(primeiro_numero)
    else:
        p_numero = int(primeiro_numero)
    
    visor.delete(0, END)


    

def click_divisão():
    primeiro_numero = str(visor.get())
    global p_numero
    global matematica
    matematica = 'divisão'
    if '.' in primeiro_numero:
        p_numero = float(primeiro_numero)
    else:
        p_numero = int(primeiro_numero)
    visor.delete(0, END)
    


def click_multiplicação():
    primeiro_numero = str(visor.get())
    global p_numero
    global matematica
    matematica = 'multiplicação'
    if '.' in primeiro_numero:
        p_numero = float(primeiro_numero)
    else:
        p_numero = int(primeiro_numero)
    visor.delete(0, END)
    


def click_subtração():
    primeiro_numero = str(visor.get())
    global p_numero
    global matematica
    matematica = 'subtração'
    if '.' in primeiro_numero:
        p_numero = float(primeiro_numero)
    else:
        p_numero = int(primeiro_numero)
    visor.delete(0, END)
    


def click_inversão():
    valor = str(visor.get())
    visor.delete(0, END)
    if '.' in valor:
        num = float(valor)
        return visor.insert(END,  float(num * (-1)))

    elif len(valor) == 0:
        return visor.insert(END, '-')

    else:
        num = int(valor)
        return visor.insert(END,  int(num * (-1)))                           


def click_igual():
    num = str(visor.get())
    if '.' in num:
        s_numero = float(num)
    else:
        s_numero = int(num)
    visor.delete(0, END)
    if matematica == 'adição':
       return visor.insert(0, p_numero + s_numero)

    if matematica == 'multiplicação':
       return visor.insert(0, p_numero * s_numero)

    if matematica == 'subtração':
       return visor.insert(0, p_numero - s_numero)

    if matematica == 'divisão':
        r = p_numero / s_numero
        i = r
        if i == int(r):
            return visor.insert(0, int(r))
        else:
            r = f"{float(i):.3f}"
            return f"{visor.insert(0, float(r))}"



def click_porcentagem():
    num = str(visor.get())
    if '.' in num:
        p_numero = float(num)
    else:
        p_numero = int(num)

    return p_numero



#dimensões da root principal
largura = 300
altura = 330

# resolução do sistema
largura_screen = root.winfo_screenwidth()
altura_screen = root.winfo_screenheight()

# faz com que a root principal sempre apareça no centro
posx = (largura_screen / 2) - (largura / 2)
posy = (altura_screen / 2) - (altura / 2)
root.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))
root.resizable(False, False)

btn = Button(root, text= '0', command= lambda: click_button(0), width=11, height=2, bd=3, bg= 'gray', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
btn.place(x=10, y=285)

btn = Button(root, text= '.',  command= click_ponto, width=11, height=2, bd=3, bg= 'gray', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
btn.place(x=105, y=285)

btn = Button(root, text= '=', command= click_igual, width=11, height=2, bd=3, bg= 'brown', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
btn.place(x=200, y=285)

btn = Button(root, text= '1', command= lambda: click_button(1), width=7, height=2, bd=3, bg= 'gray', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
btn.place(x=10, y=240)

btn = Button(root, text= '2', command= lambda: click_button(2), width=7, height=2, bd=3, bg= 'gray', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
btn.place(x=80, y=240)

btn = Button(root, text= '3', command= lambda: click_button(3), width=7, height=2, bd=3, bg= 'gray', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
btn.place(x=150, y=240)

btn = Button(root, text= '+', command= click_adição, width=7, height=2, bd=3, bg= 'brown', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
btn.place(x=227, y=240)

btn = Button(root, text= '4', command= lambda: click_button(4), width=7, height=2, bd=3, bg= 'gray', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
btn.place(x=10, y=195)

btn = Button(root, text= '5', command= lambda: click_button(5), width=7, height=2, bd=3, bg= 'gray', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
btn.place(x=80, y=195)

btn = Button(root, text= '6', command= lambda: click_button(6), width=7, height=2, bd=3, bg= 'gray', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
btn.place(x=150, y=195)

btn = Button(root, text= '-', command= click_subtração, width=7, height=2, bd=3, bg= 'brown', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
btn.place(x=227, y=195)

btn = Button(root, text= '7', command= lambda: click_button(7), width=7, height=2, bd=3, bg= 'gray', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
btn.place(x=10, y=150)

btn = Button(root, text= '8', command= lambda: click_button(8), width=7, height=2, bd=3, bg= 'gray', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
btn.place(x=80, y=150)

btn = Button(root, text= '9', command= lambda: click_button(9), width=7, height=2, bd=3, bg= 'gray', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
btn.place(x=150, y=150)

btn = Button(root, text= 'x', command= click_multiplicação, width=7, height=2, bd=3, bg= 'brown', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
btn.place(x=227, y=150)

btn = Button(root, text= 'c', command= click_delete, width=7, height=2, bd=3, bg= 'gray', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
btn.place(x=10, y=105)

btn = Button(root, text= '+/-', command= click_inversão,  width=7, height=2, bd=3, bg= 'gray', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
btn.place(x=80, y=105)

btn = Button(root, text= '%',  width=7, height=2, bd=3, bg= 'gray', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
btn.place(x=150, y=105)

btn = Button(root, text= '/', command= click_divisão, width=7, height=2, bd=3, bg= 'brown', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
btn.place(x=227, y=105)


visor = Entry(root, font=('Ivy 20 bold'))
visor.pack(side=TOP, ipadx=50, ipady=15, padx=5, pady=5)

root.mainloop()
