#trabalho calculadora

print("")
print("Selecione a operação:")
print("1. Soma")
print("2. Subtração")
print("3. Divisão")
print("4. Multiplicação")
print("0. Sair")





while True:

    operacao = int(input('Digite a operação: '))

    if operacao != 0:
        if operacao >=0 and operacao <= 4:
            
            numero1 = int(input('Digite o numero 1:'))
            numero2 = int(input('Digite o numero 2:'))

            match operacao:
                case 1:
                    resultado = numero1 + numero2
                    print ('A soma dos numeros', resultado)

                case 2:
                    resultado = numero1 - numero2
                    print ('A subtração dos números é', resultado)

                case 3: 
                    if numero2 == 0:
                        print("Divisão por zero não aceita!!")
                    else:
                        resultado = numero1 / numero2
                        print ('A divisão dos números é:', resultado)

                case 4:
                    resultado = numero1 * numero2
                    print('A Multiplicação dos números é:', resultado)
                    break

        else:
            print("Informe uma operação valida!!")
    else:
        print("Ate logo!!")
        break