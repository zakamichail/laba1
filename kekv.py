groupmates = [
    {
        "name": "Дмитрий",
        "surname": "Комаров",
        "exams": ["Анжуманя", "Бегит", "Прес качат"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Вольдемар",
        "surname": "Австрийцев",
        "exams": ["Пивоварение", "ЛГБТ", "Сборка стульев"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Арсений",
        "surname": "Дрейман",
        "exams": ["АиАЯ", "ИС", "КТП"],
        "marks": [3, 5, 2]
    },
    {
        "name": "Кирилл",
        "surname": "Михайлов",
        "exams": ["Философия", "История", "Социология"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Юрий",
        "surname": "Дружинин",
        "exams": ["Аиг", "Высшая математика", "ВвИТ"],
        "marks": [5, 4, 5]
    }
]


def print_students(students,average):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(40), u"Оценки".ljust(20))
    for student in students:
        if sum(student["marks"]) > average:
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(40), str(student["marks"]).ljust(20))



def find_average(students):
    summ = 0
    count = 0
    for student in students:
        summ += sum(student["marks"])
        count +=1
    return summ/count


average = find_average(groupmates)
print("Средний балл группы: " + str(average/3))
print("Студенты, имеющие ср. балл выше среднего:")
print_students(groupmates,average)
