class Asignatura:

    def __init__(self, nombre, salon="remoto"):##Necesario para que se imprima ese valor por defecto
        self._nombre = nombre
        self._salon = salon

    def __str__(self):##Hace de toString
        return f"{self._nombre} {self._salon}"
