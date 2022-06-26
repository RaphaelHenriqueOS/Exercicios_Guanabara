frase = str(input('Digite algo: ')).upper().strip()
palavra = frase.split() #pegou a frase e separou por caracteres dentro de uma lista
junto = ''.join(palavra) #juntou todos os caracteres
inverso = '' #variável para receber a frase ao contrário
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra] #a variável INVERSO vai receber ela mesma mais o caracteri correspondente em JUNTO que o FOR estiver chamndo
print(junto, inverso)
if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um Palíndromo')