Nome = str (input("Qual o seu nome?"))
idade = int(input("Qual a Sua idade?"))
linguagem = str(input("Qual a sua linguagem de programação favorita?")) 
print("Olá, meu nome é ",Nome," tenho", idade ," anos e estou aprendendo",linguagem ,"!")
if idade < 18: 
    print("Você ainda é menor de idade, continue estudando e praticando!")
    # fiz o desafio extra separando as mensagens mas poderia ter feito tudo num print só.
    print("Que tal aprender Python? É uma ótima linguagem para iniciantes! ")
else :  
    print("Parabéns! Você já pode ingressar no mercado de tecnologia!")
    
