import numpy as np

# Configurar o gerador
rng = np.random.Generator(np.random.PCG64())


def rolar_dados():
    # rolar 2d10
    dados = rng.integers(low=1, high=11, size=2)
    print(f'\nOs dados rolados foram: {dados}')
    resultado_dados = dados[0] + dados[1]  # somar os dados
    print(f'O total dos dados foi: {resultado_dados}')
    # verificar se dados são iguais, e caso sejam, rolar novamente, somar e testar de novo em loop
    while dados[0] == dados[1]:
        print('Números iguais! Rolando novamente:')
        dados = rng.integers(low=1, high=11, size=2)
        print(f'Os dados rolados foram: {dados}')
        resultado_dados = resultado_dados + dados[0] + dados[1]
        print(f'O total dos dados foi: {resultado_dados}')
    return resultado_dados
