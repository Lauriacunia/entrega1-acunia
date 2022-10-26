# CandyCode Blog Project

##### Proyecto fullstack realizado con Django 4.1.2.

##### Blog con posteos sobre tecnología y desarrollo de software.

#### Tecnologías:

- [x] Django 4.1.2
- [x] SQLite

#### Instalación

- Si lo desea puede crear un entorno virtual y activarlo

```
python3 -m venv venv
source venv/bin/activate
```

- Instalar módulos necesarios

```
pip install -r requirements.txt
```

- Realizar las migraciones. Éste proyecto utiliza SQLite

```
python manage.py migrate
```

- Levantar el proyecto

```
python3 manage.py runserver
```

#### Generar mock data inicial

```
>python manage.py shell < seed_data.py
```
