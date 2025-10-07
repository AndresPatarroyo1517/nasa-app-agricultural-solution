# NASA Agricultural Climate Prediction App 🌾

Este proyecto fue desarrollado durante el **NASA Space Apps Challenge 2024** como parte de un reto de soluciones agrícolas.  
Se trata de una aplicación web creada con **Django** que permite visualizar gráficos de predicción climática utilizando datos de la NASA, con el objetivo de ayudar a los agricultores a tomar decisiones informadas.

## 🚀 Objetivo del Proyecto

- Visualizar predicciones climáticas a partir de datos satelitales de la NASA.
- Ayudar a los agricultores a planificar cultivos y tomar decisiones basadas en el clima.
- Practicar el uso de Django para aplicaciones web con gráficos interactivos.

## 🧱 Estructura del Proyecto

```
nasa-app-agricultural-solution/
├── agri_app/ # Aplicación principal de Django
├── nasa_app/ # Configuración del proyecto Django
├── templates/ # Archivos HTML
├── static/ # CSS, JS y recursos estáticos
├── media/ # Imágenes y gráficos generados
├── manage.py
└── README.md
```

## ⚡ Tecnologías Utilizadas

- **Python 3.11**: Lógica del backend.
- **Django**: Framework web.
- **Matplotlib / Plotly / Seaborn**: Para generar gráficos de predicción.
- **HTML, CSS y JavaScript**: Interfaz web.

## 📌 Cómo Ejecutar el Proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/AndresPatarroyo1517/nasa-app-agricultural-solution.git
```
2. Crear un entorno virtual:
```bash
python -m venv env
source env/bin/activate  # Linux / Mac
env\Scripts\activate     # Windows
```
3. Instalar dependencias:
```bash
pip install -r requirements.txt
```
4. Ejecutar migraciones de Django:
```bash
python manage.py migrate
```
5. Ejecutar migraciones de Django:
```bash
python manage.py runserver
```
6. Abrir http://127.0.0.1:8000 en tu navegador.

