
database = {
    1: "Ali Khan",
    2: "kamran",
    3: "Jawad"
}

def get_user_from_db(user_id):
    return database.get(user_id)




