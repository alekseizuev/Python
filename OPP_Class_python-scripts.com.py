# Создаем класс Car
class Car:
    # создаем атрибуты класса
    name = "c200"
    make = "mercedez"
    model = 2008

    # создаем методы класса
    def start(self):
        print("Заводим двигатель")

    def stop(self):
        print("Отключаем двигатель")


##В примере выше мы создали класс под названием Car с тремя атрибутами:
# имя name, марка make и модель model. Наш класс также содержит два метода: start() и stop()

c = Car()
