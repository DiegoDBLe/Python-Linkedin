
# Declarando e inicializando uma variável
f = 0 
print(f)

# declarando a mesma variável novamente
f = "abc"
print(f)

# Gerando um erro, tentando unir variáveis de tipos diferentes
#print('isso é uma string' + 123) #ERRO
print('isso é uma string' + str(123))
# Variável Global X Variável local
# Para tornar a variavel f global utilizo o metodo global

def algumaFuncao():
    #global f
    f = 'def'
    print(f)


algumaFuncao()
print(f)