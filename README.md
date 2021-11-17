# SISTEMA DE PROPOSTA EM DJANGO 3

## 1 - clone o repositório
* > git clone https://github.com/GregMasterBr/sistema-de-proposta-wings-design.git

##  2 - Criar ambiente Virtual
* > python -m venv venv

##  3- Ativando o ambiente virtual no Windows
* > venv\Scripts\activate (PROMPT)
* > venv\Scripts\Activate.ps1 (PowerShell)

## 4 - Instale o requirements.txt
* > python -m pip install -r requirements.txt

##  5 - ERRO - Comentado a linha #18 da proposta/URLS.py
* > #urlpatterns = format_suffix_patterns(urlpatterns)

##  6 - Criando as migratons
* > python manage.py makemigrations core

## 7- Aplicando as migrations
* > python manage.py migrate

## 8 - Criar um superusuário para acessar o ADMIN
* > python manage.py createsuperuser
** > gregmasterbr

## 9 - Rodar o projeto
* > python manage.py runserver

## 10 - INDEX do ADMIN
* > http://127.0.0.1:8000/admin

## 11 - DESATIVAR AMBIENTE VIRTUAL
* > deactivate


### REFERÊNCIA: 
AUTOR ORGINAL: WINGS DESIGN
https://github.com/wingsdesign/proposta

https://www.youtube.com/watch?v=kLKl9IuLDV8


### EXECUTOR
Gregorio (GregMaster)

