# Sistema de Nómina - Programación Orientada a Objetos (POO) || Actualizado 27/12/2025.

Este repositorio contiene una implementación avanzada de un sistema de gestión de nómina utilizando Python. El objetivo principal es demostrar el uso de **clases abstractas**, **herencia**, **encapsulamiento** y **polimorfismo**. Desarrollar sistemas aplicables, eficientes, escalables y robustos. Aprender y entender el desarrollo de todas las fases del mismo.

## 🚀 Características Técnicas

- **Abstracción:** Se implementó la clase base `Empleado` utilizando el módulo `abc` (Abstract Base Classes), lo que impide la instanciación directa de la clase padre y define un contrato estricto mediante el método `@abstractmethod calcular_pago`.
- **Encapsulamiento:** Uso de atributos protegidos (ej. `_nombre`, `_salario_base`) y decoradores `@property` para la gestión de datos.
- **Polimorfismo:** El sistema procesa diferentes tipos de empleados (Desarrolladores, Gerentes, Freelancers e incluso Practicantes vía *Duck Typing*) de forma uniforme.
- **Gestión de Equipos:** La clase `Gerente` permite la composición de equipos recibiendo objetos completos, facilitando la escalabilidad del sistema.

## 🛠 Estructura de Clases



- `Empleado (ABC)`: Clase base que define la estructura común.
- `Desarrollador`, `Gerente`, `Freelancer`: Clases que heredan y especializan el comportamiento.
- `Practicante`: Ejemplo de implementación de Duck Typing.

## 💻 Ejecución

Para probar el sistema, simplemente clona el repositorio y ejecuta:

```bash
python reto_herencia.py
