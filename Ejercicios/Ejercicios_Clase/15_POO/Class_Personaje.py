
#Atributos publicos
'''class Personaje:
    def __init__(self, id, nombre, nano, vuela) -> None:
        self.new_id = id
        self.new_nombre = nombre
        self.new_nano = nano
        self.new_vuela = vuela

    def retornar_descripcion(self):
        per_descripcion = f"{self.new_id} - {self.new_nombre} - {self.new_nano} - {self.new_vuela}"
        return per_descripcion'''

#Atributo Privado ("__")
class Personaje:
    def __init__(self, id, nombre, nano, vuela):
        self._new_id = id
        self._new_nombre = nombre
        self._new_nano = nano
        self._new_vuela = vuela

    def set_nombre(self, nombre:str):
        self._new_nombre = nombre.strip().capitalize()
    #solo lectura
    def get_nombre(self):
        return self._
    def retornar_descripcion(self):
        per_descripcion = f"{self._new_id} - {self._new_nombre} - {self._new_nano} - {self._new_vuela}"
        return per_descripcion
