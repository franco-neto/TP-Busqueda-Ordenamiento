# ORDENAMIENTO - BURBUJA
def bubble_sort(arr):
    """
    Ordenamiento por burbuja: compara elementos adyacentes e intercambia si están desordenados.
    """
    n = len(arr)
    for i in range(n):
        # Últimos i elementos ya están ordenados
        for j in range(0, n - i - 1):
            # Si el elemento actual es mayor que el siguiente, los intercambia
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# ORDENAMIENTO - SELECCIÓN
def selection_sort(arr):
    """
    Ordenamiento por selección: busca el elemento más pequeño y lo coloca al principio.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i  # Se asume que el índice mínimo es el actual
        for j in range(i + 1, n):
            # Si encuentra un elemento menor, actualiza el índice mínimo
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambia el elemento actual con el mínimo encontrado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# BÚSQUEDA - LINEAL
def busqueda_lineal(arr, objetivo):
    """
    Búsqueda lineal: recorre todos los elementos hasta encontrar el objetivo.
    """
    for i in range(len(arr)):
        # Si encuentra el objetivo, devuelve su posición
        if arr[i] == objetivo:
            return i
    # Si no lo encuentra, devuelve -1
    return -1


# BÚSQUEDA - BINARIA
def busqueda_binaria(arr, objetivo):
    """
    Búsqueda binaria: requiere que la lista esté ordenada.
    Divide y conquista hasta encontrar el valor.
    """
    inicio = 0
    fin = len(arr) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2  # Calcula el punto medio
        if arr[medio] == objetivo:
            return medio  # Elemento encontrado
        elif arr[medio] < objetivo:
            inicio = medio + 1  # Busca en la mitad derecha
        else:
            fin = medio - 1  # Busca en la mitad izquierda
    return -1  # Elemento no encontrado


# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    # Lista de datos de ejemplo
    datos = [34, 7, 23, 32, 5, 62]
    print(f"Lista original: {datos}")

    # Ordenamiento por burbuja (usando una copia para no modificar el original)
    ordenada_burbuja = datos.copy()
    bubble_sort(ordenada_burbuja)
    print(f"Lista ordenada con burbuja: {ordenada_burbuja}")

    # Ordenamiento por selección (otra copia de la lista original)
    ordenada_seleccion = datos.copy()
    selection_sort(ordenada_seleccion)
    print(f"Lista ordenada con selección: {ordenada_seleccion}")

    # Valor a buscar
    objetivo = 23

    # Búsqueda lineal sobre la lista original
    pos_lineal = busqueda_lineal(datos, objetivo)
    if pos_lineal != -1:
        print(f"Búsqueda lineal: {objetivo} encontrado en la posición {pos_lineal}")
    else:
        print("No encontrado (con búsqueda lineal)")

    # Búsqueda binaria sobre la lista ordenada con burbuja
    pos_binaria = busqueda_binaria(ordenada_burbuja, objetivo)
    if pos_binaria != -1:
        print(f"Búsqueda binaria: {objetivo} encontrado en la posición {pos_binaria}")
    else:
        print("No encontrado (con búsqueda binaria)")
