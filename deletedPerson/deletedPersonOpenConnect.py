from ldap3 import Server, Connection, ALL, NTLM, Tls
# import ssl

AD_SERVER = 'ldap://192.168.88.239:389'
AD_USER = 'TEST\Администратор'
AD_PASSWORD = 'admin20!'
# PORT = 389
PORT = 636

server = Server(AD_SERVER)   # use_ssl=True          tls=Tls(validate=ssl.CERT_NONE)    
conn = Connection(server, user=AD_USER, password=AD_PASSWORD)  

# Подключение к серверу LDAP
if not conn.bind():
    print('Ошибка подключения к серверу LDAP:', conn.result)

# Удаление пользователя из папки в домене
dn = 'cn=Литуненко Игорь Ильич,ou=LOL,DC=test,DC=ru'  # DN (distinguished name) пользователя
if conn.delete(dn):
    print('Пользователь успешно удален')
else:
    print('Ошибка удаления пользователя:', conn.result)

# Закрытие соединения с сервером LDAP
conn.unbind()
