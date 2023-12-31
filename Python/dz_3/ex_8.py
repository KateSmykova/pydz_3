# ✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга,
# а значение — кортеж вещей.
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться на любое большее количество друзей.

data = {'Ivan':('спички','нож','палатка'),
        'Petr':('палатка','ложка','угли'),
        'Semen':('удочка','палатка','спальник')}

all = list(data.values())
everybody_have = set(all[0])
for items in all:
    everybody_have = everybody_have.intersection(set(items))
print(f'Все три друга в поход взяли {everybody_have}')

exclusive = {}
for i, items in data.items():
    exclusive[i] = set(items).difference(everybody_have)
print(f'Эти вещи уникальны и есть в одном экземпляре {exclusive}')


