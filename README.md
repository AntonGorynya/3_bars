# Ближайшие бары

Данный скрипт предназначен для анализа информации по барам и выводу следующей информации по ним:

-самый большой бар: ключ -b;
-самый маленький бар: ключ -s;
-самый близкий бар (текущие gps-координаты пользователь введет с клавиатуры: ключ -с).

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```#!bash

$ python bars.py # possibly requires call of python3 executive instead of just python

$ ./bars.py bars.json -s -b -c 1 1
biggests bar are 
-  Юнион Джек
-  Спорт бар «Красная машина»
biggest seats counts is  450

smallest bar are 
-  БАР. СОКИ
-  Соки
-  Фреш-бар
-  Бар в Деловом центре Яуза
smallest seats counts is  0

Closset bar is Staropramen

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
