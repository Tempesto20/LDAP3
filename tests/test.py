
# работает, иногда

from ldap3 import Server, Connection, ALL
AD_SERVER = 'ldap://192.168.88.239:389'
# # AD_USER = 'TEST\admin1'
AD_USER = 'TEST\Администратор'
AD_PASSWORD = 'admin20!'
AD_SEARCH_TREE = 'dc=test,dc=ru'
PORT = 389
# # Подключение к серверу Active Directory
server = Server(AD_SERVER, get_info=ALL)

# define the connection
connect = Connection(server, user=AD_USER, password=AD_PASSWORD)
if not connect.bind():
    exit(connect.result)
# perform the Add operation
# connect.add('cn=LDAP1','ou=tests', ['person', 'top', 'user'], {'userPrincipalName': 'LDAP1@test.ru','sAMAccountName': 'sAMAccountName'})
# # equivalent to
# connect.add('cn=LDAP1','ou=tests', attributes={'objectClass':  ['person', 'top', 'user'],'userPrincipalName': 'LDAP1@test.ru','sAMAccountName': 'sAMAccountName'})
    

# connect.add('cn=LDAP2,ou=tests','dc=test', ['person'], {  'userPrincipalName': 'LDAP2@test.ru','sAMAccountName': 'sAMAccountName'})
# equivalent to
connect.add('cn=LDAP2','ou=SEARCH', 'dc=test','dc=ru', attributes={'objectClass':  ['inetOrgPerson'], 'userPrincipalName': 'LDAP2@test.ru','sAMAccountName': 'sAMAccountName'})


print(connect.result)

# close the connection

connect.unbind()










# from ldap3 import Server, Connection, ALL
# AD_SERVER = 'ldap://192.168.88.254'
# # # AD_USER = 'TEST\admin1'
# AD_USER = 'TEST\Администратор'
# AD_PASSWORD = 'admin20!'
# AD_SEARCH_TREE = 'dc=test,dc=ru'
# PORT = 389
# # Подключение к серверу LDAP
# server = Server(AD_SERVER, get_info=ALL)
# connect = Connection(server, AD_USER, AD_PASSWORD)
# if not connect.bind():
#     exit(connect.result)
# # Учетные данные для нового пользователя
# username = 'LDAP2'
# password = 'admin20!admin.'
# given_name = 'John'
# surname = 'Doe'
# email = 'johndoe@example.com'

# # Создание DN для нового пользователя
# base_dn = 'ou=tests,dc=test,dc=ru'
# new_user_dn = f'cn={username},{base_dn}'

# # Проверка наличия записи перед добавлением
# connect.search(new_user_dn, '(objectClass=*)')
# if connect.entries:
#     print('Пользователь уже существует')
# else:
#     # Установка атрибутов для нового пользователя
#     attributes = {
#         'objectClass': ['top', 'person', 'organizationalPerson', 'user'],
#         'cn': username,
#         'userPrincipalName': f'{username}@test.ru',
#         'sAMAccountName': username,
#         'givenName': given_name,
#         'sn': surname,
#         'displayName': f'{given_name} {surname}',
#         'mail': email,
#         'userAccountControl': 512,  # Установка флага "Учетная запись активна"
#         'unicodePwd': f'"{password}"'.encode('utf-16-le')  # Кодирование пароля в формат UTF-16LE
#     }

#     # Выполнение операции добавления записи
#     connect.add(new_user_dn, attributes)

# # Закрытие соединения
# connect.unbind()
