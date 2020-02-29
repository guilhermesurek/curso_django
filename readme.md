#Setar 
DEBUG = True -> para ver os erros.

#ALLOWERDHOST
Endpoint para as outras api bater. deve ser liberado o acesso passando o ip de quem vai acessar
o servidor dentro dele.

#ULRS
Lugar onde seta novas URL'S

#LANGUAGE,TIME
Setar os padroẽs para br. Outros metodos juntos todos são utilizado para setar o padrao de
timezone e etc...

#Criar o diretorio virtual
virtualenv --python=python3.6 myvenv

#Iniciar o diretorio virtual
source myvenv/bin/activate

#Instalando o django
pip install django

#Helper para os camandos do django-admin
django-admin help startproject

#Iniciando o projeto com o nome abaixo.
django-admin startproject cursodjango 

#Criando a migração e o banco
python manage.py migrate

#Rodar o servidor
python manage.py runserver

-----------------------------------------------------

#Criando app
python manage.py startapp aula3

python manage.py startapp aula3
