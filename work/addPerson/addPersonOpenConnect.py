from ldap3 import Server, Connection, ALL, NTLM, Tls
# import ssl

AD_SERVER = 'ldap://192.168.88.239:389'
AD_USER = 'TEST\Администратор'
AD_PASSWORD = 'admin20!'
# PORT = 389
PORT = 636

server = Server(AD_SERVER)   # use_ssl=True          tls=Tls(validate=ssl.CERT_NONE)    
conn = Connection(server, user=AD_USER, password=AD_PASSWORD)  


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

        # 'userPassword': password,  # не работает
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
            'lil@confident.ru',
            'проспект Обуховской обор.,д.51,литера K',
            'lil@mail.ru',
            'Sankt Petersburg', 
            'Ленинградская область', 
            'Россия',
            'lil@test.ru',
            'lil',
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