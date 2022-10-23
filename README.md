# entrega1-acunia


## Instalación

- Si lo desea puede crear un entorno virtual y activarlo
```
python3 -m venv venv
source venv/bin/activate
```
- Instalar módulos necesarios

```
pip install -r requirements.txt
```

-  Realizar las migraciónes. Éste proyecto utloza SQLite
```
python manage.py migrate
```

- Levantar el proyecto
```
python3 manage.py runserver
```

