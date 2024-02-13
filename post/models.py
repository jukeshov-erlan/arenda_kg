from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

LOCATION_CHOICES = {
    'BISHKEK': 'Бишкек',
    'TOKMOK': 'Токмок',
    'BOSTERY': 'Бостери',
    'BALYKCHY': 'Балыкчы'
}

CURRENCY_CHOICES = {
        'DOLLAR': 'Доллар USA',
        'SOM': 'Сом'
    }



class Auto(models.Model):
    
    TYPE_OF_BODY_CHOICES = {
        'SEDAN': 'Седан',
        'HATCHBACK': 'Хетчбек',
        'UNIVERSAL': 'Универсал',
        'CROSSOVER': 'Кроссовер',
        'SUV': 'Внедорожник',
        'CABRIOLET': 'Кабриолет'
    }

    TRANSMISSION_CHOICES = {
        'MECHANICS': 'Механика',
        'AUTOMAT': 'Автомат'
    }

    WHEEL_CHOICES = {
        'LEFT': 'Левый',
        'RIGTH': 'Правый',
    }

    COLOR_CHOICES = {
        'BLACK': 'Черный',
        'WHITE': 'Белый',
        'BROWN': 'Коричневый',
        'SILVER': 'Серебристый',
        'GREEN': 'Зеленый',
        'RED': 'Красный',
        'YELLOW': 'Желтый'
    }

    GASOLINE_CHOICES = {
        'ELECTRO': 'Электро',
        'BENZIN': 'Бензин',
        'DIESEL': 'Дизель',
        'GAS': 'Газ'
    }

    RANTING_CHOICE = {
        'FROM 6 TO 24 HOURS': 'От 6 до 24 часов',
        'FROM 1 TO 7 DAYS': 'От 1 до 7 дней',
        'FROM 1 WEEK TO MONTH': 'От 1 недели до месяца'
    }
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    mark = models.CharField(verbose_name='Марка', max_length=100)
    model = models.CharField(verbose_name='Модель', max_length=100)
    year = models.IntegerField(verbose_name='Год',validators=[MinValueValidator(1940)],help_text='Введите год выпуска автомобиля') 
    type_of_body = models.CharField(verbose_name='Тип кузова', max_length=15, choices=TYPE_OF_BODY_CHOICES)
    transmission = models.CharField(verbose_name='Коробка передач', max_length=15, choices=TRANSMISSION_CHOICES)
    gasoline = models.CharField(verbose_name='Тип топлива', max_length=30, choices=GASOLINE_CHOICES)
    wheel = models.CharField(verbose_name = 'Руль', max_length=10, choices=WHEEL_CHOICES)
    color = models.CharField(verbose_name='Цвет', max_length=50, choices=COLOR_CHOICES)
    photo = models.ImageField(upload_to='auto_photos/', null=True, blank=True)
    price_currency = models.CharField(verbose_name='Цена в', max_length=20, choices=CURRENCY_CHOICES)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    location = models.CharField(verbose_name='локация', max_length=100, choices=LOCATION_CHOICES)
    ranting = models.CharField(verbose_name='аренда', max_length=60, choices=RANTING_CHOICE)

    def __str__(self):
        return f'{self.mark}, {self.model}, {self.year}, {self.price}'
    

class House(models.Model):

    NUMBER_OF_ROOMS = {
        '1 ROOM': '1 КОМНАТА',
        '2 ROOMS': '2 КОМНАТЫ',
        '3 ROOMS': '3 КОМНАТЫ',
        '4 ROOMS': '4 КОМНАТЫ',
        '5 ROOMS': '5 КОМНАТЫ',
        '6 ROOMS': '6 КОМНАТЫ',
        '7 ROOMS': '7 КОМНАТЫ',
    }

    YEAR_OF_BUILDINGS = {
        'UNTILL 19650': 'До 1950',
        '1950-1959': '1950-1959',
        '1960-1969': '1960-1969',
        '1970-1979': '1970-1979',
        '1980-1989': '1980-1989',
        '1990-1999': '1990-1999',
        '2000-2009': '2000:2009',
        '2010-2019': '2010-2019',
        '2020-current': '2020-наст.время'

    }

    TYPE_OF_HOUSE_CHOICES = {
        'APPARTMENT': 'КВАРТИРА',
        'COMMERCIAL_ESTATE': 'КОММЕРЧЕСКАЯ НЕДВИЖИМОСТЬ',
        'PRIVATE HOUSE': 'ЧАСТНЫЙ ДОМ'
    }

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Недвижимость', max_length=100, choices=TYPE_OF_HOUSE_CHOICES)
    location = models.CharField(verbose_name='локация', max_length=100, choices=LOCATION_CHOICES)
    price_currency = models.CharField(verbose_name='Цена в', max_length=20, choices=CURRENCY_CHOICES)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    number_of_rooms = models.CharField(verbose_name='Количество комнат',max_length=100, choices=NUMBER_OF_ROOMS)
    square = models.IntegerField(verbose_name='Площадь(м2)')
    floor = models.IntegerField(verbose_name='Этаж', validators=[MinValueValidator(1), MaxValueValidator(15)])
    year_of_buildings = models.CharField(verbose_name='Год постройки', max_length=100, choices=YEAR_OF_BUILDINGS)

    def __str__(self):
        return self.name