
# Установка бэкенда
Основные версии библиотек - django 4.1 и vue 3.2.13
<ul>
  <li> Сначала необходимо установить виртуальное окружение, библиотеки в requirements.txt </li>
  <li> База данных используется postgresql и psycopg2 для django </li>
  <li> После установки базы данных необходимо накатить миграции коммандами </li>
    <span>python manage.py makemigrations и python manage.py migrate</span> 
</ul>
<br/>

# Установка фронтенда
Для установки фронтенда потребуется сначала установить:
<ul>
  <li> nodejs - лучше всего устанавливать 16 версию </li>
  <li> Вместе с nodejs также нужно установить менеджер пакетов yarn </li>
  <li> yarn install - установка зависимостей и создание папки node_modules </li>
  <li> yarn run serve - запуск сервера </li>
  <li> yarn run build - создание билда для nginx </li>
</ul>
