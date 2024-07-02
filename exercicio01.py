def soma_tres_numeros(n1,n2,n3):
    print(f'n1={n1}\tn={n2}\tn3={n3}')
    return n1 + n2+ n3

def main():
    num1 = int(input('1º numero:'))
    num2 = int(input('2º numero:'))
    num3 = int(input('3º numero:'))

    result = soma_tres_numeros(num1,num2,num3)
    print(result)

    result2 = soma_tres_numeros(num1,num2,num3)
    print(result2)

    print('resultado = ', result)
    print('')
main()