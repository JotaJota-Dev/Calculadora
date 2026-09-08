from tkinter import *
window = Tk()
window.geometry("450x450")
estado = 0

def click():
    global estado
    if estado == 0:
        boton.config(text="Ahora soy rojo", 
                     bg="red", 
                     fg="yellow", 
                     font=("Times New Roman", 12, "bold"), 
                     relief=RAISED,
                     bd=20,
                     pady=15,
                     padx=10,
                    )
        estado = 1
    else:
        boton.config(text="Ahora soy azul", 
                     bg="blue", 
                     fg="black", 
                     font=("Arial", 12, "bold"), 
                     relief=RAISED,
                     bd=15,
                     pady=10,
                     padx=15)
        estado = 0


window.title("UGLY BUTTON")

boton = Button(window, 
               command= click,
               text="Ahora soy azul", bg="blue", fg="black", font=("Time New Roman", 12, "bold"), relief=RAISED, bd=15, pady=10, padx=15
               )

boton.pack()
boton.place(x=225, y=225, anchor=CENTER)
window.mainloop()