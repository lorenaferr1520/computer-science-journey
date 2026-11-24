def main():
    plate = input("plate:  ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Regra 1: tamanho entre 2 e 6
    if not (2 <= len(s) <= 6):
        return False

    # Regra 2: somente alfanumérico
    if not s.isalnum():
        return False

    # Regra 3: primeiras duas letras
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Regra 4 e 5: números só no final e primeiro número não pode ser 0
    found_number = False

    for c in s:
        if c.isdigit():
            if not found_number:  # primeiro número
                if c == "0":      # não pode ser zero
                    return False
                found_number = True
        else:  # letra
            if found_number:      # letra depois de número → inválido
                return False

    # Se passou por todas as regras, é válido
    return True


main()
