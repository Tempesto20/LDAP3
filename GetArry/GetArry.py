from ldap3 import Server, Connection, SUBTREE, NTLM

# AD_SERVER = 'confi.ru'
AD_SERVER = 'ldap://192.168.88.239'
# AD_SERVER = 'ldap://10.10.10.254'
# AD_SERVER = ('ldap://192.168.0.50:389')
# AD_SERVER = ('ldap://192.168.0.51:389')
AD_USER = 'TEST\Администратор'
# AD_USER = 'TEST\AL'
AD_PASSWORD = 'admin20!'
AD_SEARCH_TREE = 'dc=test,dc=ru'
PORT = 389

# Подключение к серваку
server = Server(AD_SERVER)
# conn = Connection(server)
conn = Connection(server, user=AD_USER, password=AD_PASSWORD)
conn.bind()
print(conn.bind())

attr = ['operatingSystem']
#читаю список пользоватей со "всеми" атрибутами
conn.search(AD_SEARCH_TREE, 
            # '(objectCategory=person)', 
            # '(&(objectCategory=*) (objectClass=user))',  ## Полный список всего в AD
            '(&(objectCategory=person)(objectClass=user))',
            # '(cn=anon)',
            SUBTREE, attributes=attr) 
print(len(conn.entries))
lenght = len(conn.entries)
print(lenght)
i = 0
while i < lenght:
    print(conn.entries[i])
    i = i + 1




