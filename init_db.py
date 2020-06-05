"""
Небольшой скрипт для инициализации базы данных.
Добавляет стандартного суперюзера, чтобы руками постоянно не создавать заново.
+ Создаёт для него токен (нужен для бота)

Сюда можно добавлять свои инициализации, если нужно.
"""

import os, django


DEFAULT_USER = {
    'username': "vasya",
    'email': "1@abc.net",
    'password': "promprog",
}


def init_django():
    """ Init Django and setup settings variable """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "marketplace.settings")
    django.setup()


def create_superuser(username, email, password):
    """ Creating default superuser """
    from django.contrib.auth.models import User
    if not hasattr(User, 'objects'):
        print('No User objects!\n'
              'Probably, you need make `manage.py migrate`.'
              )
        return

    if User.objects.filter(username=username):
        print(f'User "{username}" already exists!')
        return User.objects.get(username=username)
    u = User.objects.create_user(username=username, email=email, password=password)
    u.is_staff = True
    u.is_admin = True
    u.is_superuser = True
    u.save()
    print(f'User "{username}:{password}" created.')
    return u


def create_superuser_token(user):
    """ Creating token for user """
    from rest_framework.authtoken.models import Token
    if not user:
        return
    if not hasattr(Token, 'objects'):
        print('No Token objects!\n'
              'Probably, you need add "rest_framework.authtoken" in settings.INSTALLED_APPS '
              'or make `manage.py migrate`.'
              )
        return
    if Token.objects.filter(user=user):
        print(f'Token for user "{user}" already exists: {Token.objects.get(user=user).key}')
        return

    token = Token.objects.create(user=user)
    print(f'Token created: {token.key}')


def main():
    """Main func"""
    init_django()
    u = create_superuser(**DEFAULT_USER)
    create_superuser_token(u)


if __name__ == '__main__':
    main()
