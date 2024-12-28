from database.database import db
from werkzeug.security import generate_password_hash
import random, string


class Alumnus:
    @staticmethod
    def get_alumnus(username):
        alumni = Alumnus.get_alumni(username)
        return dict(alumni[0]) if len(alumni) else None

    @staticmethod
    def get_alumnus_by_id(id):
        alumni = db.execute("SELECT * FROM alumni WHERE id = ?;", id)
        return alumni[0] if len(alumni) else None

    @staticmethod
    def get_marital_status_by_id(id):
        return db.execute("SELECT name FROM marital_status WHERE id = ?;", id)[0][
            "name"
        ]

    @staticmethod
    def get_major_by_id(id):
        return db.execute("SELECT name FROM majors WHERE id = ?;", id)[0]["name"]

    @staticmethod
    def get_degree_by_id(id):
        return db.execute("SELECT name FROM degrees WHERE id = ?;", id)[0]["name"]

    @staticmethod
    def get_news():
        return db.execute(
            "SELECT * FROM posts WHERE id IN (SELECT id FROM news) ORDER BY publish_date DESC;"
        )

    @staticmethod
    def get_alumni(username):
        return db.execute("SELECT * FROM alumni WHERE username = ?;", username)

    @staticmethod
    def is_alumni(username):
        return Alumnus.get_alumni(username)

    @staticmethod
    def get_all_alumni():
        return db.execute("SELECT * FROM alumni")

    @staticmethod
    def update_password(user_id, password):
        db.execute(
            "UPDATE alumni SET password_hash = ? WHERE id = ?;",
            generate_password_hash(password),
            user_id,
        )

    @staticmethod
    def check_email(email):
        return db.execute("SELECT * FROM alumni WHERE email = ?;", email)

    @staticmethod
    def recover_account(email):
        new_password = "".join(
            random.choices(string.ascii_letters + string.digits, k=8)
        )
        db.execute(
            "UPDATE alumni SET password_hash = ? WHERE email = ?;",
            generate_password_hash(new_password),
            email,
        )
        return new_password
        


    @staticmethod
    def edit_alumni_profile(data, id):
        db.execute(
            "UPDATE users SET display_name = ? WHERE id = ?;",
            data["display_name"],
            id,
        )
        db.execute(
            "UPDATE alumni SET personal_privacy = ?, academic_privacy = ?, employment_privacy = ? WHERE id = ?;",
            data["personal_privacy"],
            data["academic_privacy"],
            data["employment_privacy"],
            id,
        )
