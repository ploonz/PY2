class Ship:
    def __init__(self, name: str, dwt: int, currentload=0, ):
        """

        :param name: Название судна
        :param dwt:  Максимально разрешенная нагрузка, в тоннах
        :param currentload: Текущая загрузка
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть типа STR")
        self.name = name
        if not isinstance(dwt, int):
            raise TypeError("DWT должен иметь тип int")
        if dwt < 0:
            raise ValueError("DWT не может иметь отрицательное значение")
        self.dwt = dwt
        if not isinstance(currentload, int):
            raise TypeError("Текущая загрузка должна иметь тип int")
        if currentload < 0:
            raise ValueError("загрузка не может быть отрицальной")
        self.currentload = currentload
        if not isinstance(name, str):
            raise TypeError("\"name\"должен иметь тип STR")
        self.name = name

    def chname(self, newname: str) -> str:
        """

        :param newname: Новое название судна
        :return:
        """
        oldname=self.name
        if not isinstance(newname, str):
            raise TypeError("новое название должно иметь тип str")
        self.name = newname
        print(f"Название судна изменено ({oldname} -> {self.name})")

    def loadup(self, load: int)-> None:
        """

        :param load: Объем загружаемого груза в тоннах
        :return:
        """
        if self.currentload > 0:
            raise ValueError("Судно уже загружено")
        if not isinstance(load, int):
            raise TypeError("Загрузка должна иметь тип int")
        if not load > 0:
            raise ValueError("Загрузка должна быть положительным числом")
        self.currentload = load

    def __str__(self) -> str:
        """
        Строковое представление экземпляра класса
        :return:
        """
        return f"Судно \"{self.name}\", загружено {self.currentload} тонн из {self.dwt} разрешенных"

    def __repr__(self) -> str:
        """
        Возвращает строку, показывающую как может быть инициализирован экземпляр
        :return:
        """
        return f"{self.__class__.__name__}({self.name!r}, {self.dwt},{self.currentload})"


class Tanker(Ship):
    def __init__(self, name: str, dwt: int, crudecond=False, currentload=0):
        """
        :param name: Название судна
        :param dwt:  Максимально разрешенная нагрузка, в тоннах
        :param currentload: Текущая загрузка
        :param crudecond: Готовность хранилища к загрузке нефтепродуктов
        """
        self.crude = crudecond
        super().__init__(name, dwt, currentload)

    def prep(self) -> None:
        self.crude = True

    def loadup(self, load: int):
        """

        :param load: Объем загружаемого груза в тоннах
        :return:
        """
        if not self.crude:
            raise ValueError("Хранилище не подготовлено к загрузке нефтепродуктов")
        if self.currentload > 0:
            raise ValueError("Судно уже загружено")
        if not isinstance(load, int):
            raise TypeError("Загрузка должна иметь тип int")
        if not load > 0:
            raise ValueError("Загрузка должна быть положительным числом")
        self.currentload = load


if __name__ == "__main__":
    df = Tanker("Big one", 35000)
    df.chname("Ol one")
