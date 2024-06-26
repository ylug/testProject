
## Технологии:

- **Backend:**
    - **Python:** Язык программирования
    - **Django:** Web-фреймворк
    - **Django REST Framework:** Фреймворк для создания API
    - **django-filter:** Библиотека для фильтрации данных
    - **psycopg2-binary:** Библиотека для взаимодействия с PostgreSQL
    - **JWT:**  Система аутентификации 
    - **DRF-YASG:**  Библиотека для документации API 
    - **Djoser:** Библиотека для аутентификации и регистрации пользователей
- **Инструменты:**
    - **Docker:**  Система контейнеризации 
    - **Docker Compose:**  Инструмент для управления многоконтейнерными приложениями 

## Запуск проекта:

```bash
docker-compose up -d --build
```

## Краткое техническое задание:

### Цель:

Создать веб-приложение с API интерфейсом и админ-панелью для управления сетью по продаже электроники.

### Модель сети:

- **Иерархическая структура:** Завод -> Розничная сеть -> Индивидуальный предприниматель.
- **Связь:** Каждое звено сети ссылается на одного поставщика, который может быть не обязательно предыдущим по иерархии.
- **Уровень:** Определяется отношением к остальным элементам сети (завод - уровень 0, розничная сеть, связанная напрямую с заводом - уровень 1).

### Элементы каждого звена сети:

- **Название**
- **Контакты:** 
    - **Email**
    - **Страна**
    - **Город**
    - **Улица**
    - **Номер дома**
- **Продукты:**
    - **Название**
    - **Модель**
    - **Дата выхода продукта на рынок**
    - **Поставщик** (предыдущий по иерархии объект сети)
    - **Задолженность перед поставщиком** (в денежном выражении)
    - **Время создания** (автоматически при создании)

### Реализация:

1. **Модель сети:** Создать модель сети в Django, отражающую иерархическую структуру и связи между элементами.
2. **Админ-панель:** Сделать вывод созданных объектов в админ-панели Django.
    - **Ссылка на "Поставщика":**  Добавить ссылку на страницу поставщика для каждого объекта сети.
    - **Фильтр по городу:**  Реализовать фильтр по названию города.
    - **Admin action:**  Создать действие в админ-панели для очистки задолженности перед поставщиком у выбранных объектов.
3. **API:**
    - **CRUD для модели поставщика:**  Создать API для CRUD-операций над моделью поставщика (создание, чтение, обновление, удаление).
    - **Запрет обновления "Задолженности":**  Запретить обновление поля "Задолженность перед поставщиком" через API.
    - **Фильтрация по стране:**  Добавить возможность фильтрации объектов по определенной стране.
    - **Аутентификация:**  Настроить права доступа к API, чтобы только активные сотрудники имели доступ. 

## Дополнительные замечания:

- **Автоматизация:**  Используйте автоматические тесты для проверки правильной работы API и моделей. 
- **Документация:**  Создайте документацию для API с помощью DRF-YASG.
- **Безопасность:**  Используйте JWT для аутентификации и используйте надежные методы шифрования данных. 
- **Разработка и развертывание:**  Используйте Docker Compose для простого развертывания приложения и всех зависимостей в среде разработки и на сервере.

## Реализация:

**1. Модель сети:**

```python
from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class NetworkElement(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

**2. Админ-панель:**

- Создать модели `Supplier` и `NetworkElement` в Django Admin
- Добавить ссылки на поставщика, фильтр по городу и "admin action" для очистки задолженности.

**3. API:**

- Создать API-представления для `Supplier` с помощью Django REST Framework.
- Настроить фильтры, сериализаторы и права доступа. 
- Запретить обновление поля `debt` через API. 

**4. Аутентификация:**

- Использовать JWT для аутентификации.
- Настроить правила, чтобы только активные сотрудники имели доступ к API.

**5. Docker Compose:**

- Создать `docker-compose.yml` файл для определения сервисов (Django, PostgreSQL, Nginx и др.) и настройки связи между ними. 
- Настроить запуск и развертывание приложения с помощью `docker-compose up -d --build`. 

## Дополнительно:

- **Документация API:**  Использовать DRF-YASG для автоматической генерации документации API. 
- **Тестирование:**  Создать автоматические тесты для проверки работы API и моделей. 
- **Разработка:**  Использовать инструменты для облегчения разработки, например, IDE с поддержкой Django и Docker. 

**Важно:** 

- **Помните о безопасности:**  Используйте надежные пароли и методы шифрования данных. 
- **Следуйте best practices:**  Используйте лучшие практики разработки Django и Python. 
- **Документируйте свой код:**  Создавайте четкие комментарии и документацию.