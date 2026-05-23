def auto_mapear(origen, destino, excluir=None):
    excluir = excluir or []

    for campo, valor in vars(destino).items():
        if campo.startswith("_") or campo in excluir:
            continue
        
        if valor is None:
            continue

        if hasattr(origen, campo):
            setattr(origen, campo, valor)

    return origen