import configparser
from threading import Lock


class ToolsBaseClass(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwds):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwds)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Tools(metaclass=ToolsBaseClass):
    def __init__(self):
        """Конструктор класса"""
        self.config = configparser.ConfigParser()
        self.config.read(r"C:\Users\Саня\Desktop\selenium_test\test_OOP\test\LK\Tools\settings.ini", encoding='utf-8')
        self.__url = self.config.get("URL", "current_url")
        self.__user_login = self.config.get("USER", "user_login")
        self.__user_password = self.config.get("USER", "user_pasword")

    @property
    def url(self):
        """ Валидная ссылка на ресурс """
        return self.__url

    @property
    def login(self):
        """ Валидный логин """
        return self.__user_login

    @property
    def password(self):
        """ Валидный пароль """
        return self.__user_password
