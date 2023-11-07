# Importa la función is_mutant del módulo is_mutant
from is_mutant import is_mutant 

# Define una función para validar secuencias de ADN
def validate_dna_sequence(message):
    while True:
        dna_sequence = input(message)
        dna_sequence = dna_sequence.upper()

        # Verifica si la secuencia tiene una longitud de 6 caracteres y contiene solo las bases A, C, G o T
        if len(dna_sequence) == 6 and all(base in "ACGT" for base in dna_sequence):
            return dna_sequence
        else:
            print("La secuencia de ADN ingresada no es válida.")

# Crea una lista para almacenar las filas de ADN
dna = []

# Solicita al usuario ingresar las filas de ADN
for i in range(6):
    dna_sequence = validate_dna_sequence(f'Ingresa la fila {i + 1} de ADN (debe contener 6 letras de A, C, G o T): ')
    dna.append(dna_sequence)

print("\nMatriz de ADN:\n")

# Muestra la matriz de ADN en la consola
for row in dna:
    for base in row:
        print(base, end="  ")  # Muestra cada base con dos espacios de separación
    print("")  # Salto de línea al final de cada fila

# Llama a la función is_mutant para verificar si la secuencia de ADN es mutante
result_dna = is_mutant(dna)

print(f"\nEs Mutante: {result_dna}\n")  # Muestra si la secuencia es mutante o no en la consola
