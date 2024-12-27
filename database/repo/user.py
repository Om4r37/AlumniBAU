import sqlite3
from database.database import db
from database.repo.alumnus import Alumnus


class User:
    @staticmethod
    def get_last_user_id():
        return db.execute("SELECT id FROM users ORDER BY id DESC LIMIT 1;")[0]["id"]

    @staticmethod
    def get_all_users():
        return db.execute("SELECT * FROM users")

    @staticmethod
    def get_user(id):
        return db.execute("SELECT * FROM users WHERE id = ?;", id)[0]

    @staticmethod
    def get_alumnus_public_profile(id):
        alumnus = dict(Alumnus.get_alumnus_by_id(id))
        user = dict(User.get_user(id))
        data = {
            "Display Name": user.get("display_name"),
        }
        if alumnus.get("personal_privacy"):
            if alumnus.get("email"):
                data["Email"] = alumnus.get("email")
            if alumnus.get("phone_number"):
                data["Phone Number"] = alumnus.get("phone_number")
            if alumnus.get("home_address"):
                data["Home Address"] = alumnus.get("home_address")
            if alumnus.get("marital_status_id") != 1:
                data["Marital Status"] = Alumnus.get_marital_status_by_id(
                    alumnus.get("marital_status_id")
                )
        if alumnus.get("academic_privacy"):
            data["Major"] = Alumnus.get_major_by_id(alumnus.get("major_id"))
            data["Degree"] = Alumnus.get_degree_by_id(alumnus.get("degree_id"))
            data["GPA"] = alumnus.get("GPA") / 100
            data["Graduation Year"] = alumnus.get("graduation_year")
        if alumnus.get("employment_privacy"):
            if alumnus.get("work_place"):
                data["Work Place"] = alumnus.get("work_place")
            if alumnus.get("work_start_date"):
                data["Work Start Date"] = alumnus.get("work_start_date")
            if alumnus.get("work_address"):
                data["Work Address"] = alumnus.get("work_address")
            if alumnus.get("public_sector"):
                data["Sector"] = "Public" if alumnus.get("public_sector") else "Private"
            if alumnus.get("work_phone"):
                data["Work Phone"] = alumnus.get("work_phone")
        return data

    @staticmethod
    def get_user_public_profile(id):
        if Alumnus.get_alumnus_by_id(id):
            return User.get_alumnus_public_profile(id)
        user = dict(User.get_user(id))
        return (
            {"Display Name": user.get("display_name")}
            if user.get("display_name")
            else {}
        )

    @staticmethod
    def get_user_full_profile(id):
        user = dict(User.get_user(id))
        user.pop("profile_picture")
        if Alumnus.get_alumnus_by_id(id):
            user.update(dict(Alumnus.get_alumnus_by_id(id)))
            user.pop("password_hash")
            user.pop("nno_hash")
        return user

    @staticmethod
    def get_pfp(id):
        pfp = db.execute("SELECT profile_picture FROM users WHERE id = ?;", id)[0]
        return pfp["profile_picture"] or open("static/pics/pfp.png", "rb").read()

    @staticmethod
    def update_pfp(id, pfp):
        db.execute(
            "UPDATE users SET profile_picture = ? WHERE id = ?;",
            sqlite3.Binary(pfp.read()),
            id,
        )
