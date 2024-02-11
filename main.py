class SocialNetwork:
    """
    Базовый класс, представляющий социальную сеть.
    """

    def __init__(self, name: str, users: int):
        """
        Инициализирует объект социальной сети.

        Args:
        name (str): Название социальной сети.
        users (int): Количество пользователей в социальной сети.
        """
        if not isinstance(name, str):
            raise TypeError("Название социальной сети должно быть строкой")
        if not isinstance(users, int):
            raise TypeError("Количество пользователей должно быть целым числом")
        if users < 0:
            raise ValueError("Количество пользователей не может быть отрицательным")

        self._name = name
        self._users = users

    @property
    def name(self) -> str:
        """
        Возвращает название социальной сети.
        """
        return self._name

    @property
    def users(self) -> int:
        """
        Возвращает количество пользователей в социальной сети.
        """
        return self._users

    @users.setter
    def users(self, value: int) -> None:
        """
        Устанавливает количество пользователей в социальной сети.

        Args:
        value (int): Новое количество пользователей.
        """
        self._users = value

    def login(self) -> None:
        """
        Симулирует авторизацию пользователей в социальной сети.
        """
        pass

    def connect(self) -> None:
        """
        Симулирует подключение пользователей к социальной сети.
        """
        pass

    def __str__(self) -> str:
        """
        Возвращает строковое представление социальной сети.
        """
        return f"SocialNetwork: {self.name}, Users: {self.users}"

    def __repr__(self) -> str:
        """
        Возвращает представление социальной сети для отладки.
        """
        return f"SocialNetwork(name='{self.name}', users={self.users})"


class Facebook(SocialNetwork):
    """
    Подкласс, представляющий Facebook.
    """

    def __init__(self, name: str, users: int, active_users: int, posts: int):
        """
        Инициализирует объект Facebook.

        Args:
        name (str): Название социальной сети.
        users (int): Количество пользователей в социальной сети.
        active_users (int): Количество активных пользователей на Facebook.
        posts (int): Количество постов, опубликованных на Facebook.
        """
        if not isinstance(active_users, int) or not isinstance(posts, int):
            raise TypeError("Активные пользователи и посты должны быть целыми числами")
        if active_users < 0 or posts < 0:
            raise ValueError("Активные пользователи и посты не могут быть отрицательными")

        super().__init__(name, users)
        self._active_users = active_users
        self._posts = posts

    @property
    def active_users(self) -> int:
        """
        Возвращает количество активных пользователей на Facebook.
        """
        return self._active_users

    @property
    def posts(self) -> int:
        """
        Возвращает количество постов на Facebook.
        """
        return self._posts

    @posts.setter
    def posts(self, value: int) -> None:
        """
        Устанавливает количество постов на Facebook.

        """
        self._posts = value

    def advertise(self) -> None:
        """
        Симулирует рекламу на Facebook.
        """
        pass

    def __str__(self) -> str:
        """
        Возвращает строковое представление Facebook.
        """
        return f"Facebook: {self.name}, Users: {self.users}, Active Users: {self.active_users}, Posts: {self.posts}"

    def __repr__(self) -> str:
        """
        Возвращает представление Facebook для отладки.
        """
        return f"Facebook(name='{self.name}', users={self.users}, active_users={self.active_users}, posts={self.posts})"

    def login(self) -> None:
        """
        Симулирует авторизацию пользователей в социальной сети.
        """
        pass

    def connect(self) -> None:
        """
        Переопределяет метод connect для добавления специфической логики подключения на Facebook.

        Обоснование:
        Facebook должен иметь уникальные процессы подключения по сравнению с
        другими социальными сетями.
        """
        pass


if __name__ == "__main__":
    """
    Точка входа в программу для проверки работоспособности кода.
    """
    social_network = SocialNetwork("VK", 3000000)
    print(social_network)  # Проверка метода str
    print(social_network.name)  # Выводит название VK
    print(social_network.users)  # Выводит количество пользователей VK
    social_network.connect()  # Вызывает метод connect для VK
    social_network.login()     # Вызывает метод login для VK

    facebook = Facebook("Facebook", 30000000, 100000, 5000)
    print(facebook)  # Проверка метода str
    print(facebook.name)  # Выводит название Facebook
    print(facebook.users)  # Выводит количество пользователей Facebook
    print(facebook.active_users)  # Выводит количество активных пользователей Facebook
    print(facebook.posts)  # Выводит количество постов на Facebook
    facebook.connect()  # Вызывает метод connect для Facebook
    facebook.login()     # Вызывает метод login для Facebook
