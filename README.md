# ELISON: EL CHATBOT PARA LA PREDICCIÓN DE RIESGO CARDIOVASCULAR

_Elison es un chatbot clasificador de riesgo cardiovascular (RCV), construído construido sobre el framework RASA en python, con el fin de aprovechar la funcionalidad DIET (Dual Intent and Entity Transformer), la cual está basada en transformers y permite utilizar modelos previamente entrenados como BERT, para mejorar la comunicación con el paciente. Así mismo, incorpora un modelo de clasificación multiclase basado en el algoritmo Xgboost para predecir el RCV en tres niveles: bajo, latente y alto. El entrenamiento del modelo predictivo de RCV se hizo usando el conjunto de datos de Pacientes Crónicos de Pasto año 2017 ( [datos abiertos](https://www.datos.gov.co/)). La validación del modelo en términos de las métricas de desempeño accuracy y recall, resultó en un 78% con un costo computacional mínimo._

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

_ELISON está construído sobre RASA open source para linux. Los pre-requisitos mínimos recomendados son los siguientes:_

```
Sistemas operativo Linux Ubuntu 18 o superior; aunque se podría probar con otras distros
Python 3.7 

```

### Instalación 🔧

_La versión actual de ELISON beta, se ejecuta localmente haciendo uso de RASA open source. Se recomienda crear un ambiente virtual con python versión 3.7 o superior. A continuación se explica cómo crear el ambiente virtual e instalar RASA open source, así mismo se detalla como descargar el repositorio de ELISON beta. Adicionalmente, se requiere descargar y descompromir ngrok._

_Crear ambiente virtual (desde Conda seguir estas instrucciones)_

```
conda create -n elison python=3.7
conda activate elison
```

_Instalar RASA Open Source_

```
sudo yum install python-pip
pip3 install -U pip
pip3 install rasa
pip3 install rasa[full]
pip3 install rasa[spacy]
python3 -m spacy download es_core_news_lg
pip install rasa --upgrade
```
_Descargar el repositorio de ELISON beta_

```
wget https://github.com/ebuitrago/Asistente_Riesgo_Cardio/archive/refs/heads/main.zip
unzip Asistente_Riesgo_cardio.zip
```

_Descargar ngrok_

Descargar ngrok y descomprimirlo en el directorio raiz; el mismo donde se alojará el directorio con los archivos fuente de ELISON

```
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip
```

## Exponer puertos con ``` ngrok ``` ⚙️

La versión beta actual de ELISON se ejecuta de manera local sobre RASA open source. Sin embargo, se requiere exponer el puerto local 5005 para que el despliegue en Telegram sea posible. Esto se hace mediante ngrok.

_Ejecutar ngrok_

```
./ngrok http 5005 
```

_Otra manera para ejecutar ngrok_

```
./ngrok http 5005 --log=stdout > ngrok.log & 
``` 

## Modificar archivo credentials.yml ⚙️

Una vez ejecutado ngrok, se genera una dirección que expone el puerto local 5005. La nueva dirección generada por ngrok debe ser cambiada en el campo respectivo del archivo credentials.yml. Esto debe hacerse cada vez que se desea ejecutar ELISON beta. Una vez realizado este ajuste, se podrán ejecutar tanto el servidor de acciones como el servidor de la versión en producción de RASA; como se muestra en los próximos pasos.

### Ejecutar RASA action server 🔩

```
rasa run actions &
```

### Ejecutar RASA ⌨️

_Explica que verifican estas pruebas y por qué_

```
rasa run &
```

## Despliegue 📦

_El despliege final de ELISON beta se hace mediante Telegram, aprovechando la flexibilidad de RASA para agregar distintos canales para lograr la interacción con el usuario final. En Telegram se accede a ELISON beta contactándo al usuario Elison. Entonecs, para que un usuario pueda iniciar sesión con ELISON beta, se requiere haber realizado los siguientes pasos:_

* Exponer puerto local 5005 con ngrok
* Cambiar la dirección generada por ngrok en el campo respectivo en el archivo credentials.yml
* Ejecutar el servidor de acciones de RASA open source
* Ejecutar el servidor de RASA open source

Los pasos anteriores fueron explicados anteriormente, por lo tanto, en este punto se podrá acceder a ELISON beta en telegram 😊

http://t.me/TuAsistenteCardiaco_Elisonbot

## Construido con 🛠️

_Las siguientes herramientas fueron utilizadas en el desarrollo de ELISON beta:_

* [RASA open source](https://rasa.com/docs/rasa/) - El framework de python sobre el cual se desarrolló ELISON beta
* [Ngrok](https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip/) - Usado para exponer puerto local 5005
* [Xgboost](https://xgboost.readthedocs.io/en/latest/python/python_intro.html) - Usado como modelos clasificador de RCV

## Autores ✒️

ELISON beta surge como producto de un trabajo de grado de Maestría en Analítica de Datos en la Universidad Central. A continuación se especifican tanto los nombres de los autores como sus respectivos aportes relacionados específicamente con ELISON beta:_

* **Elias Buitrago Bolivar** - *Desarrollo de software, calibración modelo predictivo riesgo cardiovascular, documentación* - [ebuitrago](https://github.com/ebuitrago)
* **Sonia Tereza Ardila** - *Trabajo Inicial, documentación* - [sap0408](https://github.com/sap0408)
  
Los autores agradecen al profesor Carlos Isaac Zainea por su apoyo como director del proyecto de grado. 

## Licencia 📄

Este proyecto está bajo la Licencia GPL v3.0 - mira el archivo [LICENSE.md](LICENSE.md) para detalles


* Un agradecimiento enorme a [Villanuevand](https://github.com/Villanuevand) por la plantilla para este readme.md 😊
