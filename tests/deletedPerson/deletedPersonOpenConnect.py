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

conn.delete('cn=Литуненко Игорь Ильич,ou=LOL')
print(conn.result)

conn.unbind()