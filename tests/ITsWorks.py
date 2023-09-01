from ldap3 import Server, Connection, ALL

AD_SERVER = 'ldap://192.168.88.239:389'
AD_USER = 'TEST\Администратор'
AD_PASSWORD = 'admin20!'
PORT = 389

# define the server
s = Server(AD_SERVER, get_info=ALL)  # define an unsecure LDAP server, requesting info on DSE and schema

# define the connection
c = Connection(s, user=AD_USER, password=AD_PASSWORD)
c.bind()


# perform the Add operation
# c.add('cn=LDAP,ou=LOL,DC=test,DC=ru', ['inetOrgPerson', 'posixGroup', 'top'], {'sn': 'user_sn', 'gidNumber': 0})
# equivalent to
c.add('cn=LDAP3,ou=LOL,DC=test,DC=ru', attributes={'objectClass':  ['inetOrgPerson', 'posixGroup', 'top'], 'sn': 'user_sn', 'gidNumber': 0})

print(c.result)

# close the connection

c.unbind()