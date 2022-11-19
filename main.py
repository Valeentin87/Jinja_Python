from jinja2 import Template, select_autoescape

#age = 28
#name = 'Фёдор'
#tm = Template('Мне {{a}} Привет {{n}}') # создали экземпляр класса Template
#print(tm.render(a=age, n=name))  # применили метод render к переменной tm, позволяющий в шаблон вставить имя

# ---продемонстрируем, что внутри {{  }} можно использовать любые конструкции Python------

#per = { 'name': 'Фёдор', 'age': 28}
#tm = Template('Мне {{a}} Привет {{n}}')
#print(tm.render(a=per['age'], n=per['name']))

# ----------применение экранирования {% raw %}....{% endraw %} --------------------

#per = { 'name': 'Фёдор', 'age': 28}
#tm = Template('''{% raw %} Мне {{a}}
#                            Привет {{n}} {% endraw %}''')
#print(tm.render(a=per['age'], n=per['name']))     # как видим значения к ключам словаря не вставились

# --------экранирование отдельных символов в шаблонах {{ name | e }} ------

#link = '''Отображение ссылок в HTML реализуется
# путём следующего синтаксиса <a href = http//..... /a>'''

#tm = Template('{{link | e}}')
#print(tm.render(link=link))

# чтобы не использовать конструкцию {{link | e}} можно воспользоваться классом escape встроенным в jinja, например:


#link = '''Отображение ссылок в HTML реализуется
# путём следующего синтаксиса <a href = http//..... /a>'''

#tm = Template('{{link}}')
#link_1 = select_autoescape(link)
#print(tm.render(link=link_1))

# -----использование цикла for в шаблонах ----------

fruits = ['apple', 'orange', 'strawberry']

data = '''Сегодня на рынке предлагают следующие фрукты:
        {% for i in fruits %}
            {{i}}
        {% endfor %}'''
tm1 = Template(data)
msg = tm1.render(fruits = fruits)
print(msg)

# ------Использование условия if в шаблонах -----------

numbers = []
data1 = '''Среди чисел {{nums}} на 2 без остатка делятся:
            {% if nums == None %}
                print('список пуст')
            {% endif %}'''
tm3 = Template(data1)
msg1 = tm3.render(nums = numbers)
print(msg1)


tm3 = Template('{{data1}}')
