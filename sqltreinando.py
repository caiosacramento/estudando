import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "mercadoacoes"
)

my_cursor = mydb.cursor()


my_cursor.execute("CREATE TABLE acao (name VARCHAR(255), precoatual FLOAT(10), precoatualopen FLOAT(10), precoatualmax FLOAT(10), precoatualmin FLOAT(10), volume INTEGER(15), precosete FLOAT(10), precosetehigh FLOAT(10), precosetemin FLOAT(10), precoquinze FLOAT(10) , precoquinzehigh FLOAT(10), precoquinzemin FLOAT(10), precotrinta FLOAT(10), precotrintahigh FLOAT(10), precotrintamin FLOAT(10), precosessenta FLOAT(10), precosessentahigh FLOAT(10), precosessentamin FLOAT(10), preconoventa FLOAT(10), preconoventahigh FLOAT(10), preconoventamin FLOAT(10), precocentoitenta FLOAT(10), precocentoitentahigh FLOAT(10), precocentoitentamin FLOAT(10), precotrezentosssenta FLOAT(10), precotrezentosssentahigh FLOAT(10), precotrezentosssentamin FLOAT(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")

