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
├───notebooks                 # Notebooks utilizados en clustering y feature selection
│
└───src                       # Código generado
    ├───model
    │       baseline.py       # Modelo baseline
    │       grid_search.py    # Obtención de mejores hiperparámetros
    │
    ├───preprocess            
    │   │   merge_files.py    # Generación de datos input etiquetados
    │   │   preprocess.py     # utils
    │
    └───testing               # Carpeta con scripts de prueba
```

## To do:

* Buscar nuevas variables, estudio de riesgos --> Luis
* Limpieza de datos --> Cristian
* Exploración de variables / Feature engineering --> Masa
* Clustering --> Chema, Ricardo
* Modelo clasificador --> Cristian 
* Arquitectura final --> Masa, Cristian
    - Contenerizacion
    - Escalabilidad
* Presentación
* Hacer el ReadMe