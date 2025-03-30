Nome= str (input("Digite o seu nome?"))
idade=int(input("Digite a sua idade?"))
linguagem= str(input("Qual a sua linguagem de programação favorita?")) 
print("Olá, meu nome é ",Nome," tenho", idade ," anos e estou aprendendo",linguagem ,"!")
if idade < 18: 
    print("Você ainda é menor de idade, continue estudando e praticando! Que tal aprender Python? É uma ótima linguagem para iniciantes!")
else :  
    print("Parabéns! Você já pode ingressar no mercado de tecnologia!")
