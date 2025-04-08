def main():
    print("Ingrese los votos (use 0 para terminar):")

    votos = []
    while True:
        voto = int(input())
        if voto == 0:
            break
        if voto in [1, 2, 3, 4]:
            votos.append(voto)
        else:
            print("Voto inválido. Solo se permiten los números 1, 2, 3 o 4.")

    total_votos = len(votos)

    if total_votos == 0:
        print("No se ingresaron votos válidos.")
        return

    conteo = {1: 0, 2: 0, 3: 0, 4: 0}

    for voto in votos:
        conteo[voto] += 1

    print("\nResultados de la elección:")
    for candidato in range(1, 5):
        cantidad = conteo[candidato]
        porcentaje = (cantidad / total_votos) * 100
        print(f"Candidato {candidato}: {cantidad} votos - {porcentaje:.2f}%")

if __name__ == "__main__":
    main()