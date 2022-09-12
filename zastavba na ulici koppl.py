import tkinter #naimportuje kniznicu tkinter
canvas = tkinter.Canvas(width=1000,height=300) #vytvoru premennu canvas platno 
canvas.pack()
subor = open('zastavba na ulici.txt', 'r',encoding='utf-8') #otvory subor autobusy




def zastavba():
    riadok = subor.readline()
    canvas.create_rectangle(0,150,30,0,fill='gray')


    






zastavba()
entry1 = tkinter.Entry()
entry1.pack()

button1 = tkinter.Button(text='vykresli')
button1.pack()

subor.close()
