#   Sistema de escalas de guitarra


# 1. Notas musicais em ordem cromatica
notas = [
    'C', 'C#', 'D', 'D#', 'E', 'F',
    'F#', 'G', 'G#', 'A', 'A#', 'B'
]

# 2. Intervalos da escala maior
padrao_maior = [2, 2, 1, 2, 2, 2, 1]


# 3. Afinacao padrao: da 6 ate a 1 corda
cordas = ['E', 'A', 'D', 'G', 'B', 'E']

# 4. Funcao para gerar a escala
def gerar_escala(tonica):
    escala = []
    index = notas.index(tonica)

    for intervalo in padrao_maior:
        escala.append(notas[index % 12])
        index += intervalo

    return escala


# 5. Mostrar as notas no braco da guitarra
def mostrar_braco(escala):
    casas = 13

    print("\nBraço da guitarra:")
    print("Casa:", end=" ")

    for casa in range(casas):
        print(f"{casa:^4}", end="")

    print()

    for corda in cordas:
        linha = f"{corda} | "
        index = notas.index(corda)

        for casa in range(casas):
            nota = notas[(index + casa) % 12]

            if nota in escala:
                linha += f"{nota:^4}"
            else:
                linha += f"{'-':^4}"

        print(linha)


# 6. Executar o programa
tonica = input("Digite a tonalidade (C, D, E, F, G, A ou B): ")

escala = gerar_escala(tonica)

print("\nEscala:", escala)

mostrar_braco(escala)
