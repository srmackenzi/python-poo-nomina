# 🏦 Sistema de Gestión de Nómina (POO) |21/12/2025. || Actualizacion 22/12/2025.

Este proyecto es una implementación avanzada de **Programación Orientada a Objetos** en Python, diseñada para gestionar diferentes tipos de empleados dentro de una organización. Planeo continuar mejorandolo y añadiendole funciones a medida que avance en mi aprendizaje

## 🧠 Conceptos Aplicados
* **Herencia:** Clase base `Empleado` con especializaciones para `Desarrollador`, `Gerente` y `Freelancer`. Se agrego una clase * **utilizando el concepto de Duck Typing, la clase "PRACTICANTE" No hereda de Empleado por lo tanto, es duck typing. 
* **Polimorfismo:** Implementación dinámica del método `calcular_pago()` y `mostrar_detalles()` según el tipo de objeto.
* **Encapsulamiento:** Uso de atributos protegidos (`_`) y decoradores `@property` para asegurar la integridad de los datos.
* **Composición:** La clase `Gerente` gestiona una colección de objetos de tipo `Empleado`.

## 🛠️ Estructura del Código
El sistema permite:
1. Crear empleados con salarios base o tarifas por hora.
2. Asignar bonos específicos a roles de liderazgo.
3. Gestionar equipos de trabajo de forma dinámica.
4. Generar reportes de pago automáticos.

---
*Proyecto educativo para el dominio de arquitecturas limpias en Python.*
