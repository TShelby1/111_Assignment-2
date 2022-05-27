import requests

USER_TEMPLATE = {
    "first_name":"John",
    "last_name":"Doe",
    "hobbies":"Chillen like a villain"
}


# trying to get the user first, then update the user

user_data = USER_TEMPLATE

URL = "http://127.0.0.1:5000/users/"

def get_user(pk):
    url = "%S/%S" % (URL, pk)
    response = requests.get(url)
    print(response.json())

def update_user(pk, user_data):
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




if __name__ == "__main__":
    print("UPDATE A USER")
    print("----------")
    fname = input("First Name: ")
    lname = input("Last Name: ")
    hobbies = input ("Hobbies: ")
    update_user(fname, lname, hobbies)
