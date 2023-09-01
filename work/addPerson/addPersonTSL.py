from ldap3 import Server, Connection, ALL, NTLM, Tls
import ssl

AD_SERVER = 'ldap://192.168.88.239:389'
AD_USER = 'TEST\Администратор'
AD_PASSWORD = 'admin20!'
# PORT = 389
PORT = 636

# tls = Tls(local_private_key_file='client_private_key.pem', local_certificate_file='client_cert.pem', validate=ssl.CERT_REQUIRED, version=ssl.PROTOCOL_TLSv1, ca_certs_file='ca_certs.b64')
# Создать рпавило на серваке для коннекта по защищённому соединению 
# для тсл ии ссл, подключения, сертифицированного

server = Server(AD_SERVER)   # use_ssl=True          tls=Tls(validate=ssl.CERT_NONE)    
conn = Connection(server, user=AD_USER, password=AD_PASSWORD)  



# tls = Tls(local_private_key_file = 'key.pem', local_certificate_file = 'cert.pem', validate = ssl.CERT_REQUIRED, version = ssl.PROTOCOL_TLSv1,
#           ca_certs_file = 'cacert.b64')
# server = Server(host = test_server, port = test_port_ssl, use_ssl = True, tls = tls)
# connection = Connection(server, auto_bind = True, version = 3, client_strategy = test_strategy, authentication = SASL,
#                         sasl_mechanism = 'EXTERNAL', sasl_credentials = 'username')


# провести проверку на наличие пользователя с этими данными if else потом старт по даннымм пользователя 
# работа будет с несколькими сервисами - предусматреть различные вопросы 
# проверка во всех сервисах и в дальнейшем создаём

conn.bind()
# conn.start_tls() 
def create_user(username, password, givenName, sn, displayName, 
                description, room, Officephone, mailWork, streetAddress,
                personalMailbox, city, RegionOfRussia, country, UserLogin,
                EnterUserLogin, phone, info, position,department,
                Company):
    dn = f'CN={displayName},OU=LOL,DC=test,DC=ru' 
    # CN - Отображаемое имя 
    # OU - папка где будет создан пользователь
    attributes = {
        'objectClass': ['top', 'person', 'organizationalPerson', 'user'],
        'cn': displayName, # не понятно
        
        # Общие
        'givenName': givenName,  # Имя
        'sn': sn,  # Фамилия
        'displayName': displayName,  # Отображаемое имя
        'description': description, # описание         
        'physicalDeliveryOfficeName': room, # комната
        'telephoneNumber':  Officephone,
        'mail': mailWork, # Эл почта
        
        # Адрес
        'streetAddress': streetAddress,
        'postOfficeBox': personalMailbox, # личный почтовый ящик
        'l': city,
        'St': RegionOfRussia,
        'co': country,

        # Учётная запись
        'userPrincipalName': UserLogin, # Имя входа пользователя
        'sAMAccountName': EnterUserLogin, # Имя входа пользователя (пред-Windows 2000)

        # Телефоны
        'Mobile': phone, # Телефон
        'info': info, # Заметки

        # Организация
        'title': position, # Должность
        'department': department,
        'Company': Company,

        'userPassword': password,  # не работает
        # 'unicodePwd':'IgA3ACQANQBNAHMAIwA0AEQAaQBHACIA',


        # 'altSecurityIdentities': public_key,
        # "userAccountControl": 512
        # 'userAccountControl': 512,
        # 'altSecurityIdentities': public_key
        
        # "userPassword": [password.encode('utf-8')] ,
        
        # 'unicodePwd': codecs.encode(f'"{password}"'.encode('utf-16-le'), 'hex').decode('utf-8')
        # 'unicodePwd': password.encode('utf-16-le')

    }
    # conn.extend.microsoft.modify_password(displayName, password)
    # conn.modify(dn, {'userAccountControl': [('MODIFY_REPLACE', 512)]})

    conn.add(dn, attributes=attributes)

create_user(
            'Игорь', 
            'admin20!', 
            'Игорь',  
            'Литуненко',
            'Литуненко Игорь Ильич',
            'Директор Инженерного центра', 
            '708',
            '700', 
            'lili@confident.ru',
            'проспект Обуховской обор.,д.51,литера K',
            'lili@mail.ru',
            'Sankt Petersburg', 
            'Ленинградская область', 
            'Россия',
            'lili@test.ru',
            'lili',
            '+7-900-000-00-00',
            'работает с 10.10.2023','Директор СОБИС',
            'СОБИС',
            'Конфидент'
            )

if conn.result['result'] == 0:
    print('Пользователь успешно добавлен')
else:
    print('Ошибка при добавлении пользователя:', conn.result['description'])


conn.unbind()