conda create -n elison0 python=3.7
conda activate elison0
mkdir ./elison_beta/
cd elison_beta
sudo yum install python-pip
pip3 install -U pip
pip3 install rasa
pip3 install rasa[full]
pip3 install rasa[spacy]
python3 -m spacy download es_core_news_lg
pip install rasa --upgrade
rasa init #sin entrenar
#Luego reemplazar los archivos correspondientes
#

