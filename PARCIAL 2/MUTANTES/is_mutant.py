def is_mutant(dna):
    def is_valid_dna_matrix(dna):
        # Verificar si la matriz de ADN tiene las dimensiones correctas (6x6)
        return len(dna) == 6 and all(len(row) == 6 for row in dna)

    def has_valid_dna_sequence(sequence):
        # Verificar si la longitud de la secuencia es mayor o igual a 4 y si alguna de las secuencias objetivo se encuentra en la secuencia.
        return len(sequence) >= 4 and any(seq in sequence for seq in ["AAAA", "CCCC", "TTTT", "GGGG"])

    def check_sequences(dna, length):
        # Definimos un contador que indica la cantidad de secuencias de ADN válidas
        sequence_counter = 0
        # Verificar filas
        # Comprobamos si hay una secuencia de cuatro caracteres iguales en cada fila
        for row in dna:
            if has_valid_dna_sequence(row):
                sequence_counter += 1
        # Verificar columnas
        # Comprobamos si hay una secuencia de cuatro caracteres iguales en cada columna
        for col in range(length):
            if has_valid_dna_sequence(''.join(dna[row][col] for row in range(length))):
                sequence_counter += 1
        # Verificar diagonales
        # Comenzamos las iteraciones a partir de 3 para evitar secuencias de ADN con longitudes menores a 4
        for number in range(3, length):
            # Verifica las secuencias de las diagonales superiores izquierdas
            if has_valid_dna_sequence(''.join(dna[number - i][i] for i in range(number + 1))):
                sequence_counter += 1
            # Verifica las secuencias de las diagonales superiores derechas
            if has_valid_dna_sequence(''.join(dna[i + 1][(length + i) - number] for i in range(-1, number))):
                sequence_counter += 1
            # Condición para evitar iterar elementos repetidos 
            if number < 5:
                # Verifica las secuencias de las diagonales inferiores izquierdas
                if has_valid_dna_sequence(''.join(dna[(length + i) - (number + 1)][i] for i in range(number + 1))):
                    sequence_counter += 1
                # Verifica las secuencias de las diagonales inferiores derechas
                if has_valid_dna_sequence(''.join(dna[i][(length - 1) - ((i + number) - (length - 1))] for i in range((length - 1) - number, length))):
                    sequence_counter += 1
        # Devolvemos la contidad de secuencias validas        
        return sequence_counter

    # Verificamos si la matriz de ADN tiene las dimensiones correctas
    if is_valid_dna_matrix(dna):
        # Definimos la longitud de la lista de ADN
        length = len(dna)

        # Definimos una variable que alamacena el total de secuencias repetidas
        repeated_sequences = check_sequences(dna, length)
        
        # Devolvemos True si se encuentran más de una secuencia de cuatro letras iguales
        return repeated_sequences > 1

    return False