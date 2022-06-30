IPI = int(input('Informe % IPI a ser acrescido: '))
codigo1 = int(input('Informe código peça 1: '))
valor1 = int(input('Informe valor peça 1: '))
quant1 = int(input('Informe quantidade peças 1: '))

codigo2 = int(input('Informe código peça 2: '))
valor2 = int(input('Informe valor peça 2: '))
quant2 = int(input('Informe quantidade peças 2: '))

formula = (valor1 * quant1 + valor2 * quant2)*(IPI/100 + 1)
print('Total a pagar', formula)
