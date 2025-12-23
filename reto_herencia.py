# 19/12/2025 mackenziedev.
# RETO HERENCIA
# Crear una jerarquia donde existe una clase padre y varias clases hijas que heredan
# Pero añaden su propia funcionalidad o toque
# La clase padre sera Empleado, debe tener los atributos:
# nombre,id,salario base, un metodo mostrar detalles que imprima la informacion del empleado
# un metodo llamado calculador pago que simplemente retorne el salario base
# clase hija 1: desarrollador, hereda de empleado, añade lenguaje principal, sobreescribe el 
# metodo mostrar detalles para que tambien mencione el lenguaje principal
# clase hija 2: gerente, hereda de empleado, añade departamento, añade el atributo bono
# sobreescribe el metodo calculador pago para que retorne el salario base mas el bono
# clase hija 3: freelancer, sin salario base, su metodo calcular pago recibe horas y tarifa por hora
# clase hija 4: practicante, sin salario base, su metodo calcular pago recibe horas y tarifa por hora
# PARA LA SOBREESCRITURA DEBO UTIIZAR EL MISMO NOMBRE DEL METODO DE LA CLASE PADRE PERO MODIFICAR SU FUNCIONALIDAD SEGUN LO NECESITE EN LA CLASE HIJA
# AÑADI CLASE PRATICANTE QUE NO HEREDA DE EMPLEADO, PERO AUNQUE NO HEREDA, SE COMPORTA IGUAL QUE UN EMPLEADO
# --------------------------------------------------------
class Empleado:
    def __init__(self, nombre, id, salario_base):
        self._nombre = nombre
        self._id = id
        self._salario_base = salario_base

    @property # GETTER
    def nombre(self): return self._nombre
    @property # GETTER
    def id(self): return self._id
    @property # GETTER
    def salario_base(self): return self._salario_base
    
    @nombre.setter # SETTER
    def nombre(self, nombre): self._nombre = nombre
    @id.setter # SETTER
    def id(self, id): self._id = id
    @salario_base.setter # SETTER
    def salario_base(self, salario_base): self._salario_base = salario_base
    
    def mostrar_detalles(self):
        print(f"\n--- INFORMACION DE {self._nombre} ---")
        print(f"ID: {self._id} | Salario Base: {self._salario_base}")

    def calcular_pago(self):
        return self._salario_base
    # --------------------------------------------------------

# --- DESARROLLADOR ---
class Desarrollador(Empleado):
    def __init__(self, nombre, id, salario_base, lenguaje_principal):
        super().__init__(nombre, id, salario_base) # Solo lo que pide Empleado
        self._lenguaje_principal = lenguaje_principal

    def mostrar_detalles(self):
        super().mostrar_detalles()
        print(f"Especialidad: Desarrollador {self._lenguaje_principal}")
    # --------------------------------------------------------

# --- GERENTE ---
class Gerente(Empleado):
    def __init__(self, nombre, id, salario_base, departamento, bono):
        super().__init__(nombre, id, salario_base)
        self._departamento = departamento
        self._bono = bono
        self._equipo = []

    # Recibimos el objeto completo (no sus datos sueltos)
    def agregar_empleado(self, empleado_objeto):
        self._equipo.append(empleado_objeto)
        print(f"✅ {empleado_objeto.nombre} añadido al equipo de {self._nombre}")

    def mostrar_equipo(self):
        print(f"\n🚀 MIEMBROS DEL EQUIPO DE {self._nombre.upper()}:")
        if not self._equipo:
            print("No hay subordinados asignados.")
        else:
            for emp in self._equipo:
                # Usamos polimorfismo: cada objeto se muestra como sabe
                emp.mostrar_detalles()
                print(f"Pago Final: {emp.calcular_pago()}")
                print("-" * 20)

    def calcular_pago(self):
        return self._salario_base + self._bono

    def mostrar_detalles(self):
        super().mostrar_detalles()
        print(f"Puesto: Gerente de {self._departamento} | Bono: {self._bono}")
    # --------------------------------------------------------
# --- FREELANCER ---
class Freelancer(Empleado):
    def __init__(self, nombre, id, horas, tarifa_por_hora):
        # Un Freelancer no tiene salario_base, pasamos 0 al padre
        super().__init__(nombre, id, 0)
        self._horas = horas
        self._tarifa_por_hora = tarifa_por_hora

    def calcular_pago(self):
        return self._horas * self._tarifa_por_hora

    def mostrar_detalles(self):
        super().mostrar_detalles()
        print(f"Tipo: Freelance | Pago final({self._horas}horas * {self._tarifa_por_hora}): {self.calcular_pago()}")
    # --------------------------------------------------------
# --- PRACTICANTE ---
class Practicante: # No hereda de Empleado por lo tanto, es duck typing. 
    # No se centra en la jerarquia, sino en el comportamiento, no me importa que sea
    # Mientras se comporte de una manera
    def __init__(self, nombre, id, horas, tarifa_por_hora):
        # Un practicante en este caso tiene salario base 0
        self.nombre = nombre
        self._horas = horas
        self._tarifa_por_hora = tarifa_por_hora
        
    def calcular_pago(self):
        return self._horas * self._tarifa_por_hora    

    def mostrar_detalles(self):
        print(f"\n--- INFORMACION DE {self.nombre} ---")
        print(f"Tipo: Practicante")
        print(f"Pago final({self._horas}horas * {self._tarifa_por_hora}): {self.calcular_pago()}")
# --------------------------------------------------------
# --- PRUEBA DEL SISTEMA ---
if __name__ == "__main__":

    # CREO EL PERSONAL
    dev1 = Desarrollador("Gabriel", "D001", 1200, "Python")
    dev2 = Desarrollador("Hamssy", "D002", 1000, "Python")
    free1 = Freelancer("Phillips", "F001", 15, 100)
    prac1 = Practicante("Juan", "P001", 10, 50)
    
    # CREO AL JEFE(GERENTE)
    boss = Gerente("Ibrahim", "G001", 5000, "Sistemas", 1500)

    # EL JEFE RECIBE LOS OBJETOS(NO LOS DATOS SUELTOS)
    boss.agregar_empleado(dev1)
    boss.agregar_empleado(dev2)
    boss.agregar_empleado(free1)
    boss.agregar_empleado(prac1)
    # MUESTRO EL EQUIPO PARA TESTEAR
    boss.mostrar_equipo()