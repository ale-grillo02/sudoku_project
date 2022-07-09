# # # #
# Author: Carlos A. Grillo
# Group: M112
# Created at: July 8 2022 4:00 PM
# Finished at:
# # # #

"""
Module Docstring.
"""

# Funciones Adicionales:

def make_reg(array : list, order : int) -> list:
    """
    Dado un sudoku y un orden entre [0, 8],devuelve en una lista plana la
    region correspondiente a dicho orden.
    [0,1,2],
    [3,4,5],
    [6,7,8]
    """
    # print("Creando region de orden " + str(order)) # DEBUG:
    output = []
    row = order // 3
    # print("Fila de orden " + str(row)) # DEBUG:
    col = 0 if order in (0,3,6) else 1 if order in (1,4,7) else 2
    # print("Columna de orden " + str(col)) # DEBUG:
    for i in range(3):
        for k in range(3):
            output.append(array[row * 3 +i][col * 3 + k])
    return output

def printsudoku(array : list) -> None: # DEBUG:
    """Imprime un sudoku, esta funcion solo tiene propositos de Debugging."""
    for i in array:
        print(i)

# Funciones Principales del Proyecto

def check_sudoku_sol(array : list) -> bool:
    """Dada una matriz sudoku resuelta, devuelve si esta es solucion de la misma."""

    def is_repeated(ls : list) -> bool:
        """Devuelve si existen elementos repetidos en una lista plana."""
        ls_prime = ls.copy()
        for i in ls_prime:
            # print("Eliminando " + str(i) + " de la lista, Comprobando repeticiones") # DEBUG:
            ls_prime.remove(i)
            # print(ls_prime)
            if i in ls_prime:
                # print("Existe una repeticion en el orden " + str(ls_prime.index(i))) # DEBUG:
                return True
        # print("No existen repeticiones") # DEBUG:
        return False

    # print("Comprobando si el sudoku es solucion correcta: \n") # DEBUG:
    # printsudoku(array) # DEBUG:
    for i in range(9):
        # print("Comprobando repeticiones en la fila " + str(i) \
        # + str(array[i]) + str(is_repeated(array[i]))) # DEBUG:
        # print("Comprobando repeticiones en la Columna " + str(i) \
        # + str(list(k[i] for k in array)) + str(is_repeated(list(k[i] for k in array)))) # DEBUG:
        # print("Comprobando repeticiones en la region de orden " \
        # + str(i) + ": " + str(make_reg(array, i)) + str(is_repeated(make_reg(array, i)))) # DEBUG:
        if is_repeated(array[i]) or is_repeated(list(k[i] for k in array)) or is_repeated(make_reg(array, i)):
            # print("Existen Repeticiones, No es Solucion: False") # DEBUG:
            return False
    # print("Es Solucion: True") # DEBUG:
    return True

def create_sudoku_candidates(array : list) -> list:
    """Dada una matriz sudoku sin resolver, devuelve en cada casilla vacia,
    los posibles valores que pueden colocarse en dicha casilla."""
    output = array.copy()

    def missing(list : list, row, col) -> list:
        """Dada una lista, devuelve los elementos no existentes en esta"""
        for i in list:
            if
            for k in range(1,10)
        return output

    def intersect(many_lists : list) -> list:
        """Dada una lista de listas, devuelve la interseccion de dichas listas"""
        pass

def find_unico_oculto():
    """Docstring."""

def main():
    """Main function Docstring."""
    pass

if __name__ == '__main__':
    main()
