import doctest


class fuel:
    "Класс представляет собой топливо, с определенными характеристиками"
    def __init__(self,brand:str,price:float,type:str):
        """
        Инициализация класса
        :param brand: Производитель
        :param price: Цена за литр
        :param type: вид топлива
        Example:
        >>> fuel1=fuel("GPN",65.12,"LPG")
        >>> fuel1.brand
        'GPN'
        >>> fuel1.price
        65.12
        >>> fuel1.type
        'LPG'
        >>> fuel2=fuel(brand=11,price=65,type="Petrol")
        Traceback (most recent call last):
        ...
        TypeError: Имя производителя должно быть типа String
        """
        if not isinstance(brand,str):
            raise TypeError("Имя производителя должно быть типа String")
        self.brand = brand
        if not isinstance(price,(int,float)):
            raise TypeError("Цена должна быть типа int или float")
        if price <= 0 :
            raise ValueError("Цена не может быть отрицательной или нулевой")
        self.price = price
        if not isinstance(type,str):
            raise TypeError("Вид топлива должен быть типа String")
        self.type = type

    def newprice(self,np:float)->str:
        """
        Метод меняет цену за 1 литр топлива, возвращает строку вида:"Новая цена: <pricenew>"
        :param np:новая цена
        :return:

        >>> fuel1=fuel("GPN",65.12,"LPG")
        >>> fuel1.newprice(65)
        'новая цена - 65'

        """
        if not isinstance(np,(float,int)):
            raise TypeError("Цена должна быть типа int или float")
        if np <=0:
            raise ValueError("Цена должна быть положительным числом")
        self.price=np
        return f"новая цена - {np}"
    def info(self) -> str:
        """
        "Возвращает информацию об экземпляре класса"
        :return:
        """
        return f"Информация о топливе: Вид топлива - {self.type}, Производитель - {self.brand}, Цена за 1 литр топлива - {self.price}"

fuel1=fuel("shell",60,"petrol")
print(fuel1.info())
class metal:
    "Класс представляет собой металл, с определенными х-ми"
    def __init__(self,name:str,wpc:float,price:float):
        """
        инициализация класса

        :param type:название металла
        :param wpc: вес/куб.метр
        :param price: цена за кг
        """
        if not isinstance(name,str):
            raise TypeError("Вид должен металла должен быть типа string")
        self.name=type
        if not isinstance(wpc,(float,int)):
            raise TypeError("Вес на м^3 должен быть типа int или float")
        if wpc<=0:
            raise ValueError("Вес на метр кубический должен быть больше нуля")
        self.weightpercube=wpc
        if not isinstance(price,(int,float)):
            raise TypeError("Цена должна быть типа int или float")
        if price<=0:
            raise ValueError("Цена должна быть положительной")
        self.price=price
    def info(self) -> str:
        """
        Возвращает информаци. об экзеспляре класа
        :return:
        """
        return f"Тип металла - {self.name},вес на кубический метр - {self.weightpercube},цена за кг - {self.price   }"
    def changename(self,nn:str) -> str:
        """
        Изменяет существующее название на новое
        :param nn: новое название
        :return:
        """
        if not isinstance(nn,str):
            raise TypeError("новое название должно быть типа str")
        old=self.name
        self.name=nn
        return f"название {old} изменено на {self.name}"
alu=metal("aluminium",900,650)
print(alu.info())
class tyre:
    "Класс представляет отдельную покрышку с некими характеристиками"
    def __init__(self,width:int,profile:int,radius:int):
        """

        :param width: Ширина покрышки
        :param profile: Профиль
        :param radius: Радиус
        """
        if not isinstance(width,int):
            raise TypeError("Ширина покрышки должна быть типа int")
        if width<=0:
            raise ValueError("Ширина должна быть положительным числом")
        self.width=width
        if not isinstance(profile,int):
            raise TypeError("Профиль должен быть типа INT")
        if profile <=0:
            raise ValueError("Профиль дрлжен быть положительным")
        self.profile=profile
        if not isinstance(radius,int):
            raise TypeError("Радиус должен быть типа INT")
        if profile <= 0:
            raise ValueError("Радиус должен быть положительным")
        self.radius=radius
    def chwidth(self,nw:int) :
        """
        Изменяет исходное значение шириныв на новое
        :param nw: новое значение ширины
        :return:
        """
        if not isinstance(nw,int):
            raise TypeError("Ширина должна быть типа int")
        if nw<=0:
            raise ValueError("Ширина должна быть неотрицательным числом")
        self.width=nw
    def specs(self) -> str:
        """
        Возвращает характеристики в упрощенной форме
        :return:
        """
        return f"{self.width}/{self.profile} R{self.radius} "


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()

