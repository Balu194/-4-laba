class Car:
    """Базовый класс для всех автомобилей."""

    def __init__(self, make: str, model: str, year: int) -> None:
        """Конструктор класса Автомобиль."""
        self.make = make
        self.model = model
        self.year = year

    def __str__(self) -> str:
        """Возвращает строковое представление автомобиля."""
        return f"{self.make} {self.model}, год выпуска: {self.year}"

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта для отладки."""
        return f"Car('{self.make}', '{self.model}', {self.year})"

    def start_engine(self) -> str:
        """Общий метод для запуска двигателя."""
        return "Двигатель запущен."

    def get_info(self) -> str:
        """Возвращает информацию об автомобиле."""
        return f"Это автомобиль марки {self.make}."


class SportsCar(Car):
    """Дочерний класс для спортивных автомобилей."""

    def __init__(self, make: str, model: str, year: int, top_speed: int) -> None:
        """Конструктор класса Спортивный автомобиль, расширяет конструктор базового класса."""
        super().__init__(make, model, year)
        self.top_speed = top_speed

    def __str__(self) -> str:
        """Перегружает строковое представление спортивного автомобиля."""
        return f"{self.make} {self.model}, год выпуска: {self.year}, максимальная скорость: {self.top_speed} км/ч"

    def start_engine(self) -> str:
        """Перегружает метод запуска двигателя для спортивного автомобиля."""
        return "Двигатель спортивного автомобиля запущен. Время разгона до 100 км/ч: 3.5 секунды."

    def get_info(self) -> str:
        """Перегружает информацию о спортивном автомобиле."""
        return f"Это спортивный автомобиль {self.make} {self.model} с максимальной скоростью {self.top_speed} км/ч."
