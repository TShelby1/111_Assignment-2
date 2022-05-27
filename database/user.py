from app.database import get_db

def output_formatter(results):                
    out = []
    for result in results:
        result_dict = {
            "id": results[0],
            "first_name": results [1],
            "last_name": results [2],
            "hobbies": results[3],
            "active": results[4]
        }
        out.append(result_dict)
    return out

def insert(user_dict):

    value_tuple = (
        user_dict.get("first_name"),
        user_dict.get("last_name"),
        user_dict.get("hobbies")
    )
    statement = """
        INSERT INTO user (
            first_name,
            last_name,
            hobbies
        ) VALUES (?, ?, ?)
    """
    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()

def scan():
    cursor = get_db().execute(
        "SELECT * FROM user",
        ()
    )
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def select_by_id(pk):
    cursor = get_db().execute("SELECT * FROM user WHERE id=?", (pk, ))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def update(pk, user_data):
    value_tuple = (
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies"),
        pk
    )
    statement = """ 
        UPDATE user
        SET first_name=?,
        last_name=?,
        hobbies=?
        WHERE id=?
    """
    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()
