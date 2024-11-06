import oracledb

uname = "ADMIN"

pwd = "P3tH@ppYD@t@B@s3"

cdir = "C:\Projetos\PetHappyBack\pethappy-projeto-integrador-01-backend\infra\oracledb"

wltloc = "C:\Projetos\PetHappyBack\pethappy-projeto-integrador-01-backend\infra\oracledb"

wltpwd = "dsf29788"

dsn = "pethappydb_tpurgent"

with oracledb.connect(user=uname, password=pwd, dsn=dsn, config_dir=cdir, wallet_location=wltloc, wallet_password=wltpwd) as connection:
    with connection.cursor() as cursor:

# SQL statements should not contain a trailing semicolon (“;”) or forward slash (“/”).

        sql = """select * from PET_HAPPY_PETS"""
        for r in cursor.execute(sql):
            print(r)