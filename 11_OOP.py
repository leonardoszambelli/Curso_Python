class Carro: 
    #metodo dunder: Double Underscore Method
    #metodos especiais e restrito
    def __init__ (self, modelo, cor): 
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0
    
    def acelerar(self, incremento):
        self.velocidade+=incremento
        print(f'O carro {self.modelo} acelerou para {self.velocidade} Km/h')    
    
    def parar(self):
        self.velocidade =self.velocidade
        print(f'O carro {self.modelo} parou. ') 
        
    def desacelerar(self):
        while self.velocidade >0:
            self.velocidade = max(0,self.velocidade-5)
        
#Criando um objeto: O carro!
carroInstrutor = Carro("Jetta GLI", "Preto")
carroLucas = Carro("T-Cross","Preto")
carroRafael = Carro ("Saveiro","Branco")

carroInstrutor.acelerar(60)
carroInstrutor.acelerar(10)
carroInstrutor.parar()

carroLucas.acelerar(60)