from tkinter import *
from calendario import *

global usuarios, emails, senhas
usuarios = []
emails = []
senhas = []

def Inicio():
  principal = Tk()
  principal.title('Planner')
  principal.configure(background = '#1E90FF')
  principal.geometry('700x700+500+500') 
  
  label1 = Label(text = 'Seja bem vindo(a) ao Planner', background = '#1E90FF', foreground = 'black', font = ('Arial', 15))
  label1.place(x = '230', y = '20')
  label1_1 = Label(text = 'Entrar em uma conta existente', background = '#1E90FF', foreground = 'black')  
  label1_1.place(x = '221', y = '70')
  label1_2 = Label(text = 'Criar uma conta', background = '#1E90FF', foreground = 'black')
  label1_2.place(x = '268', y = '141')
  
  def bt_click():
    Login()
  
  def bt_click2():
    principal.destroy()
    CriarConta()
  
  botao1 = Button(principal, command = bt_click, text = 'LOGIN')
  botao1.place(x = '286', y = '90')
  
  label1
  botao2 = Button(principal, command = bt_click2, text = 'CRIAR CONTA')
  botao2.place(x = '266', y = '160')

  principal.mainloop()

def Login():
  label1.destroy(), label1_1.destroy(), label1_2.destroy(), botao1.destroy(), botao2.destroy()
  
  label2 = Label(text = 'LOGIN', background = '#1E90FF')
  label2.place(x = '296', y = '20')
  
  label3 = Label(text = 'Email', background = '#1E90FF')
  label3.place(x = '300', y = '65')
  entrada1 = Entry(email)
  entrada1.place(x = '240', y = '85')

  label4 = Label(text = 'Senha', background = '#1E90FF')
  label4.place(x = '300', y = '125')
  entrada2 = Entry(senha)
  entrada2.place(x = '240', y = '145')
  
  botao3 = Button(principal, command = bt_click3, text = 'ENTRAR')
  botao3.place(x = '285', y = '185')

def CriarConta():
  criarConta = Tk()
  criarConta.title('Planner')
  criarConta.configure(background = '#1E90FF')
  criarConta.geometry('700x700+500+500')

  label2 = Label(criarConta,text = 'CRIAR CONTA', background = '#1E90FF')
  label2.place(x = '275', y = '20')

  label3 = Label( criarConta,text = 'Nome de usuário', background = '#1E90FF')
  label3.place(x = '267', y = '70')
  entrada1 = Entry(criarConta)
  entrada1.place(x = '240', y = '90')

  nome = entrada1.get()
  usuarios.append(nome)
  
  label4 = Label( criarConta,text = 'Email', background = '#1E90FF')
  label4.place(x = '300', y = '120')
  entrada2 = Entry(criarConta)
  entrada2.place(x = '240', y = '140')

  email = entrada2.get()
  emails.append(email)

  label5 = Label( criarConta, text = 'Senha', background = '#1E90FF')
  label5.place(x = '300', y = '170')
  entrada3 = Entry(criarConta)
  entrada3.place(x = '240', y = '190')

  senha = entrada3.get()
  senhas.append(senha)
  
  def bt_click3():
    criarConta.destroy()
  
  botao3 = Button(criarConta, command = bt_click3, text = 'CRIAR')
  botao3.place(x = '292', y = '230')

  criarConta.mainloop()

  Menu()
