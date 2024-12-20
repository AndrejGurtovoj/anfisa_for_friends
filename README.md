# Anfisa_for_friends

## Учебный проект

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AndrejGurtovoj/anfisa_for_friends.git
```

```
cd anfisa_for_friends
```

Cоздать и активировать виртуальное окружение:

Windows
```
python -m venv venv
source venv/Scripts/activate
```
Linux/macOS
```
python3 -m venv venv
source venv/bin/activate
```

Обновить PIP

Windows
```
python -m pip install --upgrade pip
```
Linux/macOS
```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

Windows
```
python manage.py makemigrations
python manage.py migrate
```

Linux/macOS
```
python3 manage.py makemigrations
python3 manage.py migrate
```

Запустить проект:

Windows
```
python manage.py runserver
```

Linux/macOS
```
python3 manage.py runserver
```
### Автор

- __Андрей Гуртовой__
