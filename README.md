
# Optimizador de Ingresos - Revenew

Implementación de modelo optimizador de ingresos diarios de empresa manufacturera, produciendo productos A y B. Uso de herramientas: Django y Python. 



## Quick Start

### Installation


```
# From GitHub
git clone https://github.com/Rodrigo-Mella/Revenew_optimizador.git
```

Utilizando un environment con Python=3.10.18, pararse dentro de la carpeta Revenew_test e instalar dependencias en la terminal de comandos ejecutando: 
```
# Installation
cd ./Revenew_optimizador
pip install -r requirements.txt
```
    
## Overview
Este repositorio contiene código para la implementación de un optimizador que define cantidades de un producto A y un producto B para maximizar los ingresos según ciertas condiciones definidas que restringen los tiempos de producción de ambos productos y los tiempos de uso de dos máquinas. 

Utilizando Django se genera una aplicación que accede al servidor, la cual permite cargar un archivo csv con los parámetros de restricción y precios de los productos, y como resultado entrega las cantidades e ingresos óptimos. 

La carpeta de trabajo contiene varios scripts de python asociados al optimizador y los códigos de funcionamiento de Django. En general se tiene la siguiente estructura de datos: 

```
| Revenew_optimizador/
    |- databases/
    |--- data/optimization_problem_data.csv
    |
    |- models/
    |
    |- optimizador/
    |--- migrations/
    |--- templates/
    |------failed_results.html
    |------load_csv.html
    |------success_results.html
    |--- urls.py
    |--- views.py
    |
    |- revenew/
    |--- settings.py
    |--- urls.py
    |
    |- main.py
    |- manage.py

```



## Execution

Hay dos modos de ejecutar el código, uno es en el navegador utilizando Django y el otro es ejecutando el archivo main.py en la terminal de comando. 

### Django
En la terminal de comando parado dentro de la carpeta Revenew_test se debe ejecutar el siguiente comando: 

```
# Correr servidor
python .\manage.py runserver
```
Una vez ejecutado, empezará a correr el servidor y se debe copiar y pegar el siguiente url http://127.0.0.1:8000/optimizador en el navegador a utilizar y dar ENTER.

Posteriormente se solicitará cargar el archivo csv con los parámetros de restricción para el modelo de optimización. Presionar el botón "seleccionar archivo", buscar el csv correspondiente y aceptar. Una vez cargado, presionar el botón "Enviar".

A continuación se ejecutará el programa y se entregarán los resultados de la optimización. 


### Terminal
En la terminal de comando parado dentro de la carpeta Revenew_test se debe ejecutar el siguiente comando: 

```
# Correr main
python .\main.py [ubicacion/archivo/csv]
```

Se debe definir correctamente la ubicación del csv con los parámetros de restricción para el modelo de optimización y posteriormente ejecutar el comando. 

A continuación se ejecutará el programa y se entregarán los resultados de la optimización. 