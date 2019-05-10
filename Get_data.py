import pymysql

def get_data(host, user, password, db):

    conn = pymysql.connect(host=host, #localhost
                            user=user, #user
                            password=password,
                            db = db, #youtube
                            charset='utf8mb4')
    cursor = conn.cursor()

    # ==== select example ====
    sql = "select caption from caption"
    cursor.execute(sql)

    # 데이타 Fetch
    captions = cursor.fetchall()
    captions = list(captions)
    captions = [i[0] for i in captions]
    cursor.close()
    return captions
