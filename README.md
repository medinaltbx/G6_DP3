# G6_DP3

## Project structure

```
├───data                      # Contiene todos los datos usados en el proyecto
│   ├───hp                    # Mejores hiperparametros por modelo
│   ├───input                 
│   │   ├───merged_data       # Datos preprocesados
│   │   └───raw_data          # Datos en crudo
│   │
│   └───models                # Modelos serializados
│
├───notebooks                 # Notebooks utilizados en clustering, feature selection y PCA
│
└───src                       # Código generado
│   ├───model
│   │       baseline.py       # Modelo baseline
│   │       grid_search.py    # Obtención de mejores hiperparámetros
│   │
│   ├───preprocess            
│   │   │   merge_files.py    # Generación de datos input etiquetados
│   │   │   preprocess.py     # utils
│   │
│   └───testing               # Scripts de prueba
│
└───info                      # Información general 
```

## Introducción:

## 0. Requisitos previos

Los únicos requisitos necesarios a la hora de reproducir la solución es tener instalado Docker y Git. En primer lugar, clonamos este mismo repositorio:
```
git clone https://github.com/medinaltbx/G6_DP3.git
```

Una vez clonado el repositorio, accedemos al mismo y creamos el contenedor el cual contará con el entorno Jupyter:
```
docker-compose up -d --build 
```

Esperamos unos segundos a que carguen todos los componentes y nos dirigimos a la siguiente dirección usando cualquier navegador:
``
http://localhost:8888/
``

![](info/readme_imgs/jupyter_login.png)

Completamos el campo "Password or token" con el token "**dp**", indicado en el archivo docker-compose.yml. Si todo ha ido bien, contaremos con acceso al proyecto cargado en el entorno Jupyter. Navegando dentro de la carpeta "work", observaremos la misma distribución de archivos y directorios que en el repositorio local previamente clonado:

![](info/readme_imgs/jupyter_structure.png)

## Arquitectura de la solución:

![](info/readme_imgs/arch.png)

En primer lugar realizaremos una transformación y limpieza de los datos, de los cuales obtendremos dos sets:

* **merged_train.csv**: Conjunto de datos con el cual entrenaremos y testearemos los modelos. Será subdividido en entrenamiento (75%) y validación (25%).
* **merged_test.csv**: Conjunto de datos sobre el que se realizará la clasificación con el modelo que obtenda un mejor desempeño.

Transformamos los datos de ambos sets con los notebooks de transformación. En ellos, se realizará un análisis y se generarán tres datasets nuevos, los cuales también se subdividirán en entrenamiento y test (ambos representados por *):

* **cluster_*** : Contiene los mismos datos que merged_*, añadiendo el resultado obtenido en la clusterización.
* **top_10_***: Contiene las diez variables más significativas haciendo uso del atributo "feature_importances" del módulo XGBoostClassifier.
* **pca_***: Dataset con nuevas variables obtenidas haciendo uso del método PCA.

Una vez obtenidos los nuevos datasets, pasaremos a entrenar cinco modelos haciendo uso de la librería XGBoost y, en concreto, XGBoostClassifier. Todos los modelos son sometidos previamente a una búsqueda de los mejores hiperparámetros realizando el método GridSearch Cross Validation, a excepción del modelo baseline:

* **baseline_model**: Entrenado con merged_train.csv.
* **complete_model**: Entrenado con merged_train.csv .
* **cluster_model**: Entrenado con cluster_train.csv.
* **top_10_model**: Entrenado con top_10_train.csv.
* **pca_model**: Entrenado con pca_train.csv.

Posteriormente, comparamos todos los modelos haciendo uso de la métrica _accuracy_ y obtenemos aquel que cuente con la puntuación más alta. Con este modelo final realizaremos las predicciones sobre el conjunto de test correspondiente.

## 1. Ingesta y transformación

En primer lugar, para poder realizar cualquier tipo de análisis o clasificación debemos de preprocesar nuestros datos input. Contamos con tres datasets principales, los cuales a su vez se subdividen en entrenamiento y test:

* *_datos_demograficos.csv : Información sobre el cliente (edad, empleo, estudios, etc.).
* *_performance.csv : Conjunto de datos con préstamos a clasificar. 
* *_previous_loan.csv : Préstamos históricos. Puede contener información de clientes presentes en *_performance.csv o no.

