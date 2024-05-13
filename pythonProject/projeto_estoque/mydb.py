import mysql.connector

baseDados= mysql.connector.connect(
    host='localhost',
    user= 'root',
    passwd = '01020304',
    database='autopecasbd',
)

cursorObject=baseDados.cursor()

cursorObject.execute('SELECT * FROM autopecasbdplud.loja;')
print('ok')