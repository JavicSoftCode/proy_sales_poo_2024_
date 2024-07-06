<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Gestión de Ventas Basado en Programación Orientada a Objetos</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #333;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin: 10px 0;
        }
        .tech-icon {
            width: 20px;
            height: 20px;
            vertical-align: middle;
            margin-right: 10px;
        }
    </style>
</head>
<body>
    <h1>Sistema de Gestión de Ventas Basado en Programación Orientada a Objetos</h1>

    <h2>Descripción General</h2>
    <p>El objetivo principal de este proyecto es desarrollar un sistema integral de gestión de ventas utilizando el paradigma de programación orientada a objetos (POO) en Python. El sistema está diseñado para permitir a las empresas registrar, administrar y analizar de manera eficiente toda la información relacionada con sus procesos de ventas, incluyendo productos, clientes, facturas y reportes. Este sistema no solo optimiza la gestión interna, sino que también proporciona herramientas analíticas para mejorar la toma de decisiones.</p>

    <h2>Propósito del Sistema</h2>
    <p>El sistema de gestión de ventas se crea con el propósito de centralizar y simplificar las operaciones comerciales de las empresas. Al proporcionar una solución integrada, se busca:</p>
    <ul>
        <li>Reducir la carga administrativa mediante la automatización de tareas repetitivas.</li>
        <li>Mejorar la precisión en el seguimiento y gestión de inventarios.</li>
        <li>Facilitar la gestión de relaciones con clientes mediante el mantenimiento de registros detallados.</li>
        <li>Generar informes precisos y oportunos para ayudar en la toma de decisiones estratégicas.</li>
    </ul>

    <h2>Objetivos Clave</h2>
    <ul>
        <li><strong>Gestión de Productos</strong>: Proporcionar un módulo robusto para el registro, actualización y eliminación de productos, así como la consulta del catálogo completo.</li>
        <li><strong>Gestión de Clientes</strong>: Permitir el registro, actualización y eliminación de información de clientes, además de mantener un historial detallado de sus compras.</li>
        <li><strong>Gestión de Facturas</strong>: Facilitar la creación de nuevas facturas de venta, la adición de productos, el cálculo automático de totales y la emisión de facturas en formato PDF.</li>
        <li><strong>Reportes y Análisis</strong>: Generar informes y análisis de ventas por diversos criterios (período, producto, cliente, etc.) para obtener insights valiosos.</li>
        <li><strong>Interfaz Gráfica de Usuario (GUI)</strong>: Desarrollar una interfaz de usuario intuitiva y amigable utilizando las bibliotecas PyQt/PySide, que permita a los usuarios finales interactuar fácilmente con el sistema.</li>
    </ul>

    <h2>Arquitectura y Diseño</h2>
    <p>El sistema se ha diseñado siguiendo los principios de la programación orientada a objetos, con una estructura modular y escalable. Las principales clases y módulos incluyen:</p>
    <ul>
        <li><strong>Producto</strong>: Encapsula la información y el comportamiento de los productos, como nombre, descripción, precio, stock, etc.</li>
        <li><strong>Cliente</strong>: Representa los datos y las acciones relacionadas con los clientes, como nombre, dirección, historial de compras, etc.</li>
        <li><strong>Factura</strong>: Maneja la creación, cálculo y emisión de facturas de venta, incluyendo la adición de productos y el cálculo de totales.</li>
        <li><strong>Reportes</strong>: Genera informes y análisis de ventas a partir de los datos almacenados en el sistema.</li>
        <li><strong>GUI</strong>: Implementa la interfaz gráfica de usuario utilizando PyQt/PySide, integrando todas las funcionalidades del sistema.</li>
    </ul>

    <h2>Tecnologías Utilizadas</h2>
    <ul>
        <li><img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/python.svg" alt="Python" class="tech-icon">Python 3.9: Lenguaje de programación principal utilizado para el desarrollo del sistema.</li>
        <li><img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/programming.svg" alt="POO" class="tech-icon">Programación Orientada a Objetos (POO): Paradigma de programación utilizado para estructurar y organizar el código del sistema.</li>
        <li><img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/qt.svg" alt="PyQt" class="tech-icon">PyQt 5.15 / <img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/qt.svg" alt="PySide" class="tech-icon">PySide 6: Bibliotecas de widgets y herramientas GUI para crear la interfaz de usuario gráfica.</li>
        <li><img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/sqlite.svg" alt="SQLite" class="tech-icon">SQLite 3.35 / <img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/postgresql.svg" alt="PostgreSQL" class="tech-icon">PostgreSQL 13: Sistemas de gestión de bases de datos relacionales utilizados para almacenar y administrar los datos del sistema.</li>
        <li><img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/git.svg" alt="Git" class="tech-icon">Git 2.31 / <img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/github.svg" alt="GitHub" class="tech-icon">GitHub: Sistema de control de versiones y plataforma de alojamiento del código fuente del proyecto.</li>
        <li><img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/html5.svg" alt="HTML" class="tech-icon">HTML 5 / <img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/css3.svg" alt="CSS" class="tech-icon">CSS 3 / <img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/javascript.svg" alt="JavaScript" class="tech-icon">JavaScript ES6: Tecnologías web utilizadas para el diseño y la interactividad de la interfaz de usuario.</li>
        <li><img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/pandas.svg" alt="Pandas" class="tech-icon">Pandas 1.2 / <img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/matplotlib.svg" alt="Matplotlib" class="tech-icon">Matplotlib 3.4: Bibliotecas de análisis de datos y visualización utilizadas en los módulos de reportes.</li>
    </ul>

    <h2>Estado Actual del Proyecto</h2>
    <p>El proyecto se encuentra en una etapa inicial de desarrollo, con solo un commit realizado hasta el momento. Se espera que en las próximas semanas se avance en la implementación de las funcionalidades clave y se establezca una estructura sólida para el sistema.</p>

    <h2>Contribución</h2>
    <p>Si deseas contribuir a este proyecto, te invitamos a que revises las <a href="CONTRIBUTING.md">pautas de contribución</a> y te pongas en contacto con el equipo de desarrollo. Todas las contribuciones son bienvenidas, ya sea en forma de informes de problemas, solicitudes de funciones, correcciones de errores o mejoras en el código.</p>

    <h2>Licencia</h2>
    <p>Este proyecto aún no ha especificado una licencia. Se determinará una licencia apropiada, como MIT o Apache 2.0, en una etapa posterior del desarrollo, una vez que se haya consolidado la estructura y las funcionalidades principales del sistema.</p>

    <h2>Repositorio</h2>
    <p>Puedes encontrar el repositorio del proyecto en <a href="https://github.com/JavicSoftCode/proy_sales_poo_2024_.git">GitHub</a>.</p>
</body>
</html>
