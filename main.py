from tkinter import *
import conf 
import requests


class App:
	def __init__(self,toplevel):
		self.fr1 = Frame(toplevel)
		self.fr1.pack()
		self.fr2 = Frame(toplevel)
		self.fr2.pack()
		self.fr3 = Frame(toplevel)
		self.fr3.pack()
		self.fr4 = Frame(toplevel)
		self.fr4.pack()
		self.fr5 = Frame(toplevel).pack()
		self.fr6 = Frame(toplevel).pack() 
		self.fr7 = Frame(toplevel).pack()
		
		fonte1 = 'Verdana 14 bold'
		Label(self.fr1,text='BUSCADOR DE CEP',fg='green',font = fonte1,pady=7).pack()
		Label(self.fr2,text='Número do CEP',fg='darkblue',font=fonte1,pady=7).pack()
		self.n_cep = Entry(self.fr2,font=fonte1)
		self.n_cep.focus_force()
		self.n_cep.pack()
		
		CEP_texto = Label(self.fr3,text='CEP informado',font=fonte1,fg='blue',pady=7)
		CEP_texto.pack()
		self.CEP = Label(self.fr3,text='Nenhum Cep informado',font=fonte1,pady=7)
		self.CEP.pack()
		cidade_texto=Label(self.fr3,text='Localidade',font=fonte1,fg='blue')
		cidade_texto.pack()
		self.cidade = Label(self.fr3,text='---',font=fonte1,pady=7)
		self.cidade.pack()
		ddd_texto = Label(self.fr4,text='DDD',font=fonte1,fg='blue').pack()
		self.ddd = Label(self.fr4,text='---',font=fonte1,pady=7)
		self.ddd.pack()
		estado_texto = Label(self.fr5,text='Unidade Federativa',font=fonte1,fg='blue')
		estado_texto.pack()
		self.estado = Label(self.fr5,text='---',font=fonte1,pady=7)
		self.estado.pack()
		logradouro_texto = Label(self.fr5,text='Logradouro',font=fonte1,fg='blue')
		logradouro_texto.pack()
		self.logradouro = Label(self.fr5,text='---',font=fonte1,pady=7)
		self.logradouro.pack()
		self.buscar = Button(self.fr6,text='BUSCAR CEP',width=20,font=fonte1,fg='white',bg='#121212',pady=7,command=self.BuscarCep)
		self.buscar.pack()
		self.error_msg = Label(self.fr7,text="",font=fonte1,fg='red',pady=7)
		self.error_msg.pack()
		
	def BuscarCep(self):
		try:
			
			cep = self.n_cep.get() 
			CepFormatado = cep.replace('-','').replace('.','').replace('','')
			link = f'https://viacep.com.br/ws/{CepFormatado}/json/'
		
			if len(CepFormatado) == 8:
				requisicao = requests.get(link)
				CepFormatado = requisicao.json()
				cidade = CepFormatado['localidade']
				CEP = cep
				ddd = CepFormatado['ddd']
				self.CEP['text'] = f'{CEP}'
				self.cidade['text'] = f'{cidade}'
				self.ddd['text'] = f'{ddd}'
				estado = CepFormatado['uf']
				self.estado['text'] = f'{estado}'
				logradouro = CepFormatado['logradouro']
				self.logradouro['text'] = f'{logradouro}'
				self.error_msg['text'] = ''
			elif CepFormatado == '':
				self.error_msg['text'] = 'INSIRA UM CEP'

			elif len(CepFormatado) <8 or len(CepFormatado) >8:
				self.error_msg['text'] = f'ERROR! CEP COM {len(CepFormatado)} Nº'
				
			
			else:
				self.error_msg['text'] = 'INSIRA UM CEP VÁLIDO'
			
		except KeyError:
			self.error_msg['text'] = 'CEP INVÁLIDO'
	

if __name__=='__main__':

	raizApp = Tk()
	raizApp.title(conf.titulo_app)
	raizApp.resizable(conf.r_altura,conf.r_largura)
	App(raizApp)

	raizApp.mainloop()
