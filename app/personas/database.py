import pymysql

def query_r(sql):
    conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="50c13d4d11", db="personas")
    cursor = conn.cursor()
    cursor.execute(sql)

    list = []
    columns = [column[0] for column in cursor.description]
    for row in cursor.fetchall():
        list.append(dict(zip(columns, row)))

    cursor.close()
    respuesta = True

    # except:
    #    list = ""
    #    respuesta = False

    return respuesta, list
