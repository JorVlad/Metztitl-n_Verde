# Metztitl-n Verde 🌿

Sitio web informativo para concientizar sobre el cambio climático en nuestra ciudad.

---

## 📂 Estructura del proyecto

Metztitl-n_Verde/
│
├── app.py
├── requirements.txt
├── templates/
│ └── index.html
└── static/
└── style.css

yaml
Copiar código

- `app.py` — servidor Flask que sirve la página.
- `templates/index.html` — plantilla HTML principal.
- `static/style.css` — estilos CSS de la aplicación.
- `requirements.txt` — dependencias del proyecto.

---

## 🛠 Instalación y ejecución local

1. Clona el repositorio:

   ```bash
   git clone https://github.com/JorVlad/Metztitl-n_Verde.git
   cd Metztitl-n_Verde
(Opcional) crea y activa un entorno virtual:

bash
Copiar código
python -m venv venv
source venv/bin/activate    # en Linux/macOS
venv\Scripts\activate       # en Windows
Instala dependencias:

bash
Copiar código
pip install -r requirements.txt
Ejecuta la aplicación:

bash
Copiar código
python app.py
Abre en tu navegador:

cpp
Copiar código
http://127.0.0.1:5000
📐 Funcionalidades
Navbar con enlaces que hacen scroll a secciones: Inicio, Consecuencias, Historia.

Espacios para:

Videos (embebidos).

Imágenes.

Sección de Consecuencias del cambio climático.

Sección de Historia del fenómeno.

Footer con enlaces a noticias externas relevantes.

Diseño con paleta de colores: verde oscuro, azul oscuro y beige.

Derechos de autor: Jordan.

📦 Dependencias
text
Copiar código
Flask
(Opcionalmente puedes incluir otras librerías si creces el proyecto, como requests, Flask-Cors, etc.)

🎨 Colores del diseño
Verde oscuro: #14532d

Azul oscuro: #0f172a

Beige: #f5f5dc

🧩 Mejoras futuras sugeridas
Scroll suave al hacer clic en los enlaces del menú.

Modo oscuro / claro.

Cargar noticias dinámicamente mediante APIs (por ejemplo, usar requests para obtener RSS o JSON).

Un sistema de comentarios o foro para que usuarios compartan sus experiencias.

Optimización para dispositivos móviles/responsive.

Uso de animaciones moderadas (fade-in, transiciones suaves).

📝 Licencia & Créditos
Autor: Jordán Bautista Hernández

© 2025 Metztitlán Verde — Todos los derechos reservados.