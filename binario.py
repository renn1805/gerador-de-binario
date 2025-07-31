tipoOperacao = int(input(
    "digite 1 para passar de binario para número, digite 0 para passar de numero para binario: "))

if tipoOperacao == 0:
    numeroEscolhido = int(
        input("digite seu número para passar para binario: "))
    casasBinario = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    casasBinario.reverse()
    numeroBinario = []

    for i in range(10):
        if numeroEscolhido >= casasBinario[i]:
            numeroBinario.append(1)
            numeroEscolhido = numeroEscolhido - casasBinario[i]
        else:
            numeroBinario.append(0)
        i = i + 1
    numeroBinario.reverse()
    print("Seu binario é: ", numeroBinario)

elif tipoOperacao == 1:
    numeroEscolhido = int(
        input("digite seu binario para passar para numero: "))
    baseOperacao = len(str(numeroEscolhido))

    for i in range(int(len(str(numeroEscolhido)))):
        if (str(numeroEscolhido)[i] == "1") | (str(numeroEscolhido)[i] == "0"):
            if str(numeroEscolhido)[i] == "1":
                somaBases = 0
                somaBases += pow(2, len(str(numeroEscolhido)[i]))
                print(somaBases)
        else:
            print("acho que seu numero não é um binario")
            break
