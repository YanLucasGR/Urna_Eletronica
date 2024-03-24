'''ELEIÇÕES 2037'''

from tkinter import *
from tkinter import messagebox

import pymysql.cursors

conexao = pymysql.connect(
     host="localhost",
     user="root",
     password="",
     database="urna",
     cursorclass=pymysql.cursors.DictCursor
)

def corrigir():
    visorNumero.delete(0, END)

def confirmar():

     voto = visorNumero.get()

     if voto != '13' and voto != '22':
         sql = "INSERT INTO nulo (voto) VALUES (%s)"
         valor = ('.')
         cursor = conexao.cursor()
         cursor.execute(sql, (valor))
         conexao.commit()
         visorNumero.delete(0, END)

     if voto == '13':
         sql = "INSERT INTO Lula (voto) VALUES (%s)"
         valor = ('.')
         cursor = conexao.cursor()
         cursor.execute(sql, (valor))
         conexao.commit()
         visorNumero.delete(0, END)


     if voto == '22':
        sql = "INSERT INTO Bolsonaro (voto) VALUES (%s)"
        valor = ('.')
        cursor = conexao.cursor()
        cursor.execute(sql, (valor))
        conexao.commit()
        visorNumero.delete(0, END)
def branco():
    sql = "INSERT INTO branco (voto) VALUES (%s)"
    valor = ('.')
    cursor = conexao.cursor()
    cursor.execute(sql, (valor))
    conexao.commit()
    visorNumero.delete(0, END)

janela = Tk()

janela.title('ELEIÇÕES 2037')
janela.geometry('1100x800')
janela.config(bg='#C0C0C0')

def getNumero(numero):
    pegarNumero = visorNumero.get()
    visorNumero.delete(0, END)
    visorNumero.insert(0, str(pegarNumero) + str(numero))
    return

#criação do frame dos números para a votação
area_votação = Frame(janela,borderwidth=1,relief="solid",bg='#4e4e4e')
area_votação.place(x=690,y=50,height=700,width=400)

#criação dos botões (numeros e funcionalidades do sistema)
botao_1 = Button(area_votação,text='1',font='calibri 30',relief="raised",bg='black',fg='white', command= lambda : getNumero(1))
botao_1.place(x=30,y=30,height=100,width=100)

botao_2 = Button(area_votação, text='2',font='calibri 30',relief="raised",bg='black',fg='white',command= lambda : getNumero(2))
botao_2.place(x=150,y=30,height=100,width=100)

botao_3 = Button(area_votação,text='3',font='calibri 30',relief="raised",bg='black',fg='white',command= lambda : getNumero(3))
botao_3.place(x=270,y=30,height=100,width=100)

botao_4 = Button(area_votação,text='4',font='calibri 30',relief="raised",bg='black',fg='white', command= lambda : getNumero(4))
botao_4.place(x=30,y=170,height=100,width=100)

botao_5 = Button(area_votação,text='5',font='calibri 30',relief="raised",bg='black',fg='white',command= lambda : getNumero(5))
botao_5.place(x=150,y=170,height=100,width=100)

botao_6 = Button(area_votação,text='6',font='calibri 30',relief="raised",bg='black',fg='white', command= lambda : getNumero(6))
botao_6.place(x=270,y=170,height=100,width=100)

botao_7 = Button(area_votação,text='7',font='calibri 30',relief="raised",bg='black',fg='white',command= lambda : getNumero(7))
botao_7.place(x=30,y=310,height=100,width=100)

botao_8 = Button(area_votação,text='8',font='calibri 30',relief="raised",bg='black',fg='white',command= lambda : getNumero(8))
botao_8.place(x=150,y=310,height=100,width=100)

botao_9 = Button(area_votação,text='9',font='calibri 30',relief="raised",bg='black',fg='white',command= lambda : getNumero(9))
botao_9.place(x=270,y=310,height=100,width=100)

botao_0 = Button(area_votação,text='0',font='calibri 30',relief="raised",bg='black',fg='white',command= lambda : getNumero(0))
botao_0.place(x=150,y=450,height=100,width=100)

botao_votoBranco = Button(area_votação,text='BRANCO',font='calibri 15 bold',relief="raised",bg='white',fg='black', command= branco)
botao_votoBranco.place(x=30,y=610,height=60,width=100)

botao_votoCorrigir = Button(area_votação,text='CORRIGIR',font='calibri 15 bold',relief="raised", bg='orange',fg='black', command=corrigir)
botao_votoCorrigir.place(x=150,y=610,height= 60,width=100)

botao_votoConfirmar = Button(area_votação,text='CONFIRMA',font='calibri 15 bold',relief="raised",bg='green',fg='black', command=confirmar)
botao_votoConfirmar.place(x=270,y=610,height=60,width=100)
#fim dos botões

#criação do frame do visor da votação
Visor_votação = Frame(janela,bg='black',borderwidth=1,relief='solid',)
Visor_votação.place(x=10,y=50,height=700,width=670)

visor_votoNumero = Frame(Visor_votação,bg='black',borderwidth=1,relief='solid')
visor_votoNumero.place(x=180,y=250,height=150,width=300)

visorNumero = Entry(visor_votoNumero,fg='white',bg="black",font="calibri 150 bold",borderwidth=0)
visorNumero.place(x=14,y=6,height=140,width=270)

janela.mainloop()

sql = "SELECT id_lula FROM lula"
cursor = conexao.cursor()
cursor.execute(sql)
Lula = cursor.fetchall()

sql = "SELECT id_bolsonaro FROM bolsonaro"
cursor = conexao.cursor()
cursor.execute(sql)
Bolsonaro = cursor.fetchall()

sql = "SELECT id_branco FROM branco"
cursor = conexao.cursor()
cursor.execute(sql)
Branco = cursor.fetchall()

sql = "SELECT id_nulo FROM nulo"
cursor = conexao.cursor()
cursor.execute(sql)
Nulo = cursor.fetchall()

messagebox.showinfo('Apuração dos votos', message=f'''Votos no candidato Lula: {Lula[-1]['id_lula']}
Votos no candidato Bolsonaro: {Bolsonaro[-1]['id_bolsonaro']}
Votos em branco: {Branco[-1]['id_branco']}
Votos nulos: {Nulo[-1]['id_nulo']}
''')
