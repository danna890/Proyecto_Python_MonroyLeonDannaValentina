# 📚🎬🎵 Administrador de Colección de Libros, Películas y Música

El **Administrador de Colección de Libros/Películas/Música** es una aplicación de consola que permite gestionar de forma sencilla una colección personal de elementos culturales, como libros, películas o música.  
Su objetivo principal es ofrecer una herramienta para **organizar títulos, consultar información rápidamente y realizar búsquedas eficientes**.

---

## 🔍 Problemática

Organizar una colección de libros, películas o música puede convertirse en un desafío cuando el número de elementos aumenta.  
Sin un sistema adecuado resulta complicado:

- 📑 Mantener un registro ordenado de cada elemento con sus características.  
- 🔎 Consultar detalles de cada título (autor, género o valoración) sin revisar manualmente toda la colección.  
- ⏱ Realizar búsquedas rápidas por título, autor o género.

Este **Administrador de Colección** resuelve dichas problemáticas ofreciendo:
- Una **interfaz de consola** clara y sencilla.
- **Persistencia de datos** usando archivos JSON.
- Herramientas para añadir, editar, buscar, listar y eliminar elementos de manera intuitiva.

---

## 🛠️ Tecnologías y Herramientas

- **Lenguaje principal**: [Python](https://www.python.org/) 🐍  
- **Librerías utilizadas**:
  - [tabulate](https://pypi.org/project/tabulate/) → mostrar la información en formato de tablas.
- **Diseño de menús**:  
  Basado en [este recurso](https://gist.github.com/programmersland/0d76751149e083e073e7aac03e6fbae0)
- **Control de versiones**: [Git](https://git-scm.com/) y [GitHub](https://github.com/)  
  - Uso de **conventional commits** para la gestión del historial.

---

## ✨ Funcionalidades Principales

### ➕ Añadir Elemento a la Colección
Registrar un nuevo elemento indicando:
- **Título**
- **Autor/Director/Artista** (según el tipo)
- **Género**
- **Valoración** (opcional)  
Datos guardados en archivos JSON para mantener la persistencia.

### 📋 Listar Elementos
- Listado completo de la colección.
- Opciones de filtrado por categoría:
  - 📚 **Libros**
  - 🎬 **Películas**
  - 🎵 **Música**

### 🔍 Buscar Elementos
- Por **Título**
- Por **Autor/Director/Artista**
- Por **Género**

### ✏️ Editar Elementos
Modificar información existente:
- Título
- Autor/Director/Artista
- Género
- Valoración  
Cambios guardados automáticamente.

### 🗑️ Eliminar Elementos
Eliminar por:
- Título
- Índice único  
Manteniendo la colección organizada y sin duplicados.

### 💾 Guardar y Cargar Colección
- **Cargar:** al iniciar el programa, lee automáticamente los datos existentes desde archivos JSON.
- **Guardar:** cambios persistentes para no perder información.

---

## 📂 Estructura del Proyecto

```bash
Proyecto_Python_ApellidoNombre/
│
├─ main.py                   # Archivo principal de ejecución
│
├─ controladores/            # Lógica de cada acción
│    ├─ agregar.py
│    ├─ listar.py
│    ├─ buscar.py
│    ├─ editar.py
│    ├─ eliminar.py
│   
│
├─ modelos/                  # Capa de datos (manejo JSON)
│    ├─ coleccion.py
│  
│
├─ vistas/                   # Menús e interacción con el usuario
│    ├─ menu_consola.py
│    
│
├─ libros.json               # Datos de libros 📚
├─ peliculas.json            # Datos de películas 🎬
└─ musica.json               # Datos de música 🎵
