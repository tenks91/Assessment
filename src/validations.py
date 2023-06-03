# Valida el código (si es numérico y de longitud 6).
def validate_code(codigo: str) -> bool:
    return (codigo.isnumeric())