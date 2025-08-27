def calcular_valores(total, pessoas, sugeridor):
    if pessoas < 2:
        print("O número de pessoas deve ser pelo menos 2.")
        return

    # Número de pessoas que pagam a parcela normal
    pessoas_normais = pessoas - 1

    # Seja x o valor da parcela normal. O sugeridor paga 2x.
    # Então: pessoas_normais * x + 2x = total
    # => (pessoas_normais + 2) * x = total
    # => x = total / (pessoas_normais + 2)

    parcela_normal = total / (pessoas_normais + 2)
    parcela_sugeridor = 2 * parcela_normal

    print(f"\nTotal do churrasco: R$ {total:.2f}")
    print(f"Total de pessoas: {pessoas} (incluindo quem sugeriu)")
    print(f"{sugeridor} (quem sugeriu) pagará: R$ {parcela_sugeridor:.2f}")

    for i in range(1, pessoas + 1):
        nome = f"Pessoa {i}"
        if nome != sugeridor:
            print(f"{nome} pagará: R$ {parcela_normal:.2f}")
calcular_valores(total_churrasco, num_pessoas, nome_sugeridor)


