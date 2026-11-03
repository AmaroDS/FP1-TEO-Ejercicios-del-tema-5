def elimina_duplicados(lista: list) -> list:
    """
    Devuelve la lista resultante de eliminar los elementos duplicados, 
    conservando para el resto de elementos el orden de la lista original.

    Parámetros:
    lista (list): Lista de elementos que puede contener duplicados.
    
    Devuelve:
    list: La lista sin elementos duplicados, manteniendo el orden original.
    """
    res = []
    vistos = set() #NO SE PUEDE USAR {}!!!
    for elemen in lista:
        if elemen not in vistos:
            res.append(elemen)
            vistos.add(elemen)
    return res

def une_conjuntos(lista_de_conjuntos: list[set]) -> set:
    """
    Devuelve el conjunto resultante de la unión de todos los conjuntos de la lista.

    Parámetros:
    lista_de_conjuntos (list[set]): Lista de conjuntos a unir.
    
    Devuelve:
    set: El conjunto resultante de la unión de todos los conjuntos.
    """
    res = set()
    for conjunto in lista_de_conjuntos:
        res = res | conjunto #también se puede res = res.union(conjuntos)
        #Seria más eficiente usar el metodo update
        res.update(conjunto)
    return res

def intersecta_conjuntos(lista_de_conjuntos: list[set]) -> set:
    """
    Devuelve el conjunto resultante de la intersección de todos los conjuntos de la lista.

    Parámetros:
    lista_de_conjuntos (list[set]): Lista de conjuntos a intersectar.
    
    Devuelve:
    set: El conjunto resultante de la intersección de todos los conjuntos.
    """
    if len(lista_de_conjuntos) == 0:
        return set()

    #if not lista_de_conjuntos:
    #   return set()

    res = lista_de_conjuntos[0] #Esto es seguro porque antes he comprobado que no está vacío
    for conjunto in lista_de_conjuntos: #Si se quiere saltar el primero, lista de conjuntos[1:]
        res = res & conjunto # res = res.intersection(conjunto)
    return res