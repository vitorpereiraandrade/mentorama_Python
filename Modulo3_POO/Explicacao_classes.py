Olá! Tudo bem? Vou te ajudar com o conteúdo sobre programação orientada a objetos e vou te ajudando a montar o código. Acho que montar pra
vc não é uma boa alternativa porque pode atrapalhar no seu processo de aprendizado, ok? Mas todas as dúvidas que surgirem você me envia aqui,
pois vou te ajudar a montar esta questão. Bom, vamos lá...
A classe é uma entidade, que pode ser: carro, pessoa, empresa, televisão, etc...
Os atributos são as características que definem cada classe.
Por exemplo:
Temos a classe pessoa, então os atributos que definem cada pessoa pode ser: altura, peso, cor dos olhos, etc...
Os métodos são as ações que as classes podem realizar.
Por exemplo: A pessoa pode crescer, engordar, emagrecer,  acordar, dormir, viajar, etc....

Tá, mas como definir cada uma destas coisas no código?
Vamos lá... Suponha uma classe Carro que tem como atributo cor, marca e modelo. Além disso, seus métodos são: ligar, desligar e imprimir os dados do carro.

#define a classe
class Carro:

#o método init é executado todas as vezes que você criar um novo Carro. Então, dentro dele é interessante definir os atributos iniciais
    def init (self, cor, marca, modelo):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo

 #método/função para ligar o carro
    def ligar (self):
        print('O carro ligou!!')

  #método/função para desligar o carro
    def desligar (self):
        print('O carro desligou!!')

 #método/função para mostrar para o usuário as informações sobre o carro
    def imprimir (self):
        print('O carro possui a cor: ', self.cor)
        print('O carro é da marca: ', self.marca)
        print('O carro é do modelo: ', self.modelo)



#Aqui, estamos fora da classe Carro. Agora, quero criar 2 Objetos carros diferentes. Para isso, vou chamar a classe duas vezes e enviar como parâmetro os atributos deles.
car1 = Carro('Azul','Honda','Civic')
car2 = Carro('Prata','Chevrolet','Onix')

#agora quero realizar algumas ações com meu carro 1
car1.ligar()
car1.desligar()
car1.imprimir()

#agora quero realizar algumas ações com meu carro 2
car2.ligar()
car2.desligar()
car2.imprimir()