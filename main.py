class Language:
    def __init__(self, lang_id, name):
        self.lang_id = lang_id
        self.name = name


# Языки
languages = [Language(1, 'C++'),
             Language(2, 'Python'),
             Language(3, 'Java'),
             Language(4, 'C#')]


class Operator:
    def __init__(self, op_id, name, uses, lang_id):
        self.op_id = op_id
        self.name = name
        self.uses = uses
        self.lang_id = lang_id


# Названия
operators = [Operator(1, 'сложение', 95, 1),
             Operator(2, 'вычитание', 95, 1),
             Operator(3, 'противоположное число', 42, 4),
             Operator(4, 'возведение в степень', 20, 2),
             Operator(5, 'присваивание', 100, 3)]


class OpLang:
    def __init__(self, lang_id, op_id):
        self.lang_id = lang_id
        self.op_id = op_id


op_lang = [OpLang(1, 1),
           OpLang(1, 2),
           OpLang(4, 3),
           OpLang(2, 4),
           OpLang(3, 5)]


def find(element, arr):
    for i in arr:
        if i.name == element:
            return i.lang_id


def main():
    one_to_many = [(op.name, op.uses, lan.name)
                   for op in operators
                   for lan in languages
                   if op.lang_id == lan.lang_id]

    many_to_many_tmp = [(lan.name, ol.lang_id, ol.op_id)
                        for lan in languages
                        for ol in op_lang
                        if lan.lang_id == ol.lang_id]

    many_to_many = [(lan_name, op.name)
                    for lan_name, lang_id, op_id in many_to_many_tmp
                    for op in operators
                    if op.op_id == op_id]


    # Д1
    print('Задание 1')
    ans1 = []
    for el in one_to_many:
        if el[0][len(el[0]) - 2:] == 'ие':
            ans1.append((el[0], el[2]))

    print(ans1)

    # Д2
    print('Задание 2')
    sum = [0 for i in range(0, len(languages))]
    count = [0 for i in range(0, len(languages))]
    for i in operators:
        sum[i.lang_id - 1] += i.uses
        count[i.lang_id - 1] += 1

    ans2 = []
    for i in range(len(sum)):
        ans2.append((languages[i].name, sum[i] / count[i]))

    print(sorted(ans2, key = lambda s: s[1]))

    # Д3
    print('Задание 3')
    ans3 = {}
    _languages = list(filter(lambda x: x.name[0] == 'C', languages))

    for i in _languages:
        anstmp = []
        tmp = list(filter(lambda x: x[0] == i.name, many_to_many))
        for j in tmp:
            anstmp.append(j[1])
        ans3[i.name] = anstmp
    print(ans3)


if __name__ == '__main__':
    main()
