# task1
class Student:
    __id = 0

    def __init__(self, firstName: str, secondName: str, name: str, birthday: str, adress: str, phone: str, facult: str,
                 course: int, group: int):
        self.__student = {
            "firstName": firstName,
            "secondName": secondName,
            "name": name,
            "birthday": birthday,
            "adress": adress,
            "phone": phone,
            "facult": facult,
            "course": course,
            "group": group,
        }
        print("Студент создан")
        self.__student["id"] = self.__class__.__id
        self.__class__.__id += 1

    def __del__(self):
        print("Студент отчислен")
    def setName(self,name:str):
        if type(name) == str and len(name)>1:
            self.__student["name"] = name

    def getName(self):
        return self.__student["name"]

    def getGroup(self):
        return self.__student["group"]

    def getFacult(self):
        return self.__student["facult"]

    def getAge(self):
        lst = self.__student["birthday"].split(".")
        lst = [int(x) for x in lst]
        dt = datetime.datetime(lst[2], lst[1], lst[0])
        now = datetime.datetime.now()
        return ((now - dt).days // 365)

    def showInfo(self):
        for i, item in self.__student.items():
            print(str(i) + ': ' + str(item))

collection = [
    Student("Ермакович", "Сергеевич", "Виталий", "15.10.2000", "ул.Белорусская", "+375296728310", "FIT", 2, 5),
    Student("Новик", "Александрович", "Леша", "12.12.1909", "ул.Белорусская", "+3752973453345", "FIT", 2, 6),
    Student("Грудько", "Антонович", "Юра", "12.12.1999", "ул.Белорусская", "+375297667974", "FIT", 2, 10),
    Student("Гурский", "Владимирович", "Артем", "12.12.1999", "ул.Белорусская", "+375297425905", "LESHOZ", 3, 1),
    Student("Сураго", "Николаевич", "Гриша", "12.12.1999", "ул.Белорусская", "+375296432184", "LESHOZ", 4, 3),
]

n = int(input("Введите n:\n"))
query1 = [x for x in collection if x.getGroup() == n]
for i in query1:
    print(i.getName())
f = input("Введите факультет(FIT или LESHOZ):\n")
query2 = [x for x in collection if x.getFacult() == f]
for i in query2:
    print(i.getName())

# task2
class Stem:  # стебель
    def __init__(self, height: int):
        self.height = height

class Flower:  # цветок
    name = ""

    def __init__(self, height: int):
        self.stem = Stem(height)

class Rose(Flower):
    name = "Роза"

class Chrysanthemum(Flower):
    name = "Хризантема"

class Bouquet:  # букет

    def __init__(self):
        self.__bouquet = []

    def add(self, flower: Flower):
        self.__bouquet.append(flower)

    def __iter__(self):
        for i in self.__bouquet:
            yield i

    def __len__(self):
        return len(self.__bouquet)


f1 = Rose(7)
f2 = Chrysanthemum(8)
f3 = Rose(15)
f4 = Chrysanthemum(2)
bouquet = Bouquet()
bouquet.add(f1)
bouquet.add(f2)
bouquet.add(f3)
bouquet.add(f4)
for i in bouquet:
    print(i.name, i.stem.height)