while True:
    letra = input("Digite a letra (S, C, V): ")
    match letra.upper():
        case 'S':
            print("Solteiro(a)")
            break
        case 'C':
            print("Casado(a)")
            break
        case 'V':
            print("Viúvo(a)")
            break
        case _:
            print("Estado civil não encontrado")