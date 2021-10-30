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

_La versión beta actual de ELISON se ejecuta de manera local sobre RASA open source. Sin embargo, se requiere exponer el puerto local 5005 para que el despliegue en Telegram sea posible. Esto se hace mediante ngrok, como se explica a continuación._

```
./ngrok http 5005 
```

## Modificar archivo credentials.yml ⚙️

_Una vez ejecutado ngrol, se genera una dirección que expone el puerto local 5005. LA nuevq dirección de ngrok debe ser cambiada en el campo respectivo del archivo credentials.yml. Esto debe hacerse cada vez que se desea ejecutar ELISON beta. Una vez realizada este ajuste, se podrán ejecutar tanto el servidor de acciones como el servidor de la versión en producción de RASA; como se muestra en los próximos pasos.

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

_El despliege final de ELISON beta se hace mediante Telegram, aprovechando la flexibilidad de RASA para agregar distintos canales para lograr la interacción con el usuario final_

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Maven](https://maven.apache.org/) - Manejador de dependencias
* [ROME](https://rometools.github.io/rome/) - Usado para generar RSS

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki)

## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Elias Buitrago Bolivar** - *Desarrollo de software, documentación* - [ebuitrago](https://github.com/ebuitrago)
* **Sonia Tereza Ardila** - *Trabajo Inicial, documentación* - [sap0408](https://github.com/sap0408)
* **Carlos Isaac Zainea** - *Director Trabajo de Grado* - [Izainea](https://github.com/Izainea)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) quíenes han participado en este proyecto. 

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles


* Un agradecimiento enorme a [Villanuevand](https://github.com/Villanuevand) por la plantilla para este readme.md 😊
