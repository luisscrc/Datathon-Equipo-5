# To Do
Aquí tienes las tareas agrupadas y divididas entre Guillermo, Luis y Víctor, según las instrucciones proporcionadas:

### Tareas de Guillermo
- [ ] **Posición**: Pasarla como una variable categórica y usar OneHotEncoder.
- [ ] **Motivo de la Renuncia**: Continuar con la limpieza y clasificación de las razones, diferenciando entre renuncias voluntarias e impuestas. Dividir en columna con 1 como renuncia voluntaria y 2 como no voluntaria, aplicar variable categórica y emplear encoder.
- [X] **Clave de sexo**: Convertir a datos categóricos en pandas (M para masculino, F para femenino).

### Tareas de Luis
- [ ] **Área**: Esperar el mensaje de Luis en WhatsApp para explicar el significado de las iniciales y pasarla como una variable categórica usando OneHotEncoder.
- [ ] **Grupo de personal**: Esperar detalles de Luis en WhatsApp, y luego pasarla como una variable categórica usando OneHotEncoder.
- [ ] **Lugar de Nacimiento**: Convertir a mayúsculas una vez que Luis pase el archivo limpio.
- [X] **Estado Civil**: Convertir a categoría una vez que esté limpio.

### Tareas de Víctor
- [X] **A líquida**: Decidir si se elimina (Drop) por no estar disponible.
- [ ] **Código Postal**: Usar API para determinar el lugar actual de vivienda, integrar los códigos que no corresponden y consumir API para agregar columna de distancia a Bosch.
- [X] **Tiempo Viviendo en Ciudad Juárez**: Convertir a categoría.
- [X] **Hijos**: Contabilizar el número de hijos y crear una nueva columna para indicar si tienen hijos o no.

### Tareas Pendientes (No Asignadas)
- [ ] **Baja**: Fecha en que los empleados salen de la empresa.
- [ ] **Alta**: Fecha en que los empleados entran a la empresa.
- [ ] **Regla PHT**: Dejar para después como variable categórica.

### Tareas Completadas
- [X] **Años**: Duración en años que el empleado estuvo en la empresa.
- [X] **Meses**: Duración en meses que el empleado estuvo en la empresa.
- [X] **Antigüedad**: Total de días que el empleado estuvo en la empresa.
- [X] **Nacionalidad**: Información disponible.
- [X] **Edad del Empleado**: Información disponible.

Este formato te permite visualizar claramente las responsabilidades asignadas a cada persona, así como las tareas pendientes y completadas.

# Datathon-Equipo-5
Desarrollo del problema propuesto por Bosch 

Esta es una rama de pruebas. 


# Análisis de Datos - Checklist

## Descripción de las Columnas

- [ ] **Posición**: No tenemos información. - 
- [ ] **Área**: Luis pasará un mensaje en WhatsApp explicando el significado de las iniciales.
- [ ] **A líquida**: No disponible.
- [ ] **Grupo de personal**: Luis proporcionará detalles en WhatsApp.
- [ ] **Código Postal**: Usar API para determinar el lugar actual de vivienda. Dos códigos no corresponden.
- [ ] **Motivo de la Renuncia**: Continuar con la limpieza y clasificación de las razones, diferenciando entre renuncias voluntarias e impuestas.
- [ ] **Baja**: Fecha en que los empleados salen de la empresa.
- [ ] **Alta**: Fecha en que los empleados entran a la empresa.
- [ ] **Regla PHT**: Se desconoce su significado.
- [ ] **Años**: Duración en años que el empleado estuvo en la empresa.
- [ ] **Meses**: Duración en meses que el empleado estuvo en la empresa.
- [ ] **Antigüedad**: Total de días que el empleado estuvo en la empresa.
- [ ] **Clave de sexo**: M (Masculino) y F (Femenino).
- [ ] **Lugar de Nacimiento**: Ya está limpio. Falta convertir a mayúsculas.
- [ ] **Nacionalidad**: Información disponible.
- [ ] **Edad del Empleado**: Información disponible.
- [X] **Tiempo Viviendo en Ciudad Juárez**: Convertir a categoría.
- [ ] **Estado Civil**: Incluye soltero, casado, separado.
- [X] **Hijos**: Número de hijos. Crear nueva columna para indicar si tienen hijos o no.


# Proyectos de Análisis de Datos en Recursos Humanos

## 1. Modelo Predictivo de Retención de Empleados
- **Objetivo**: Identificar factores clave que influyen en la retención y desarrollar un modelo para predecir la probabilidad de renuncia de un empleado.
- Hay que hacer un scatterplot para identificar la correlacion de las caracteristicas con la probabilidad de una renuncia
- Se crea un modelo de machine learning que pueda evaluar la probabilidad de renuncia o despido del 1 al 10
- Tenemos los DNO

## 2. Análisis de Diversidad en el Lugar de Trabajo
- **Objetivo**: Evaluar el estado actual de la diversidad en la organización y proponer estrategias para mejorarla.
- Hacer graficas sobre las diversidad laboral en distintas categorias en las que son necesarias como por ejemplo, su sexo, estado civil, edad expresada en rangos y en graficas lineales, estado civil, si tienen hijos o no y cuantos tienen.

## 3. Estrategias de Desarrollo de Carrera
- **Objetivo**: Analizar datos para identificar patrones en el ascenso y desarrollo de carrera, y recomendar vías para el progreso de los empleados.
- Hacer investigacion de que tan probable es que el personal se quede en una organizacion basados en informacion

## 4. Impacto de la Ubicación en la Satisfacción Laboral
- **Objetivo**: Estudiar cómo la ubicación geográfica afecta la satisfacción y retención de los empleados.
- Es mas probable que alguien nacido en otro estado se vaya de la empresa? 
- Que tan probable es que alguien se vaya por motivos de transporte o reubicacion
- Distancia al lugar de

## 5. Tendencias Salariales y Equidad
- **Objetivo**: Examinar las tendencias salariales y proponer medidas para asegurar la equidad salarial en la organización.
- Ver la manera de incluir tendencias salariales aunque no se tengan

## 6. Optimización del Equilibrio Vida Laboral-Personal
- **Objetivo**: Proponer soluciones basadas en datos para mejorar el equilibrio vida laboral-personal de los empleados.

## 7. Visualización Innovadora de Datos de RH
- **Objetivo**: Crear visualizaciones interactivas que destaquen insights clave de los datos de RH.

## Notas Adicionales
- Considerar otros aspectos relevantes que puedan surgir durante el análisis de datos.
