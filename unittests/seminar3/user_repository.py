class UserRepository:

    # Тут можно хранить аутентифицированных пользователей
    data = []

    def add_user(self, user):
        self.data.append(user)

    def all_users_logout(self):
        dataNew = []
        for elem in self.data:
            if elem.admin:
                dataNew.append(elem)
        self.data = dataNew
