import sqlite3
from datetime import datetime
from database.database import db
from werkzeug.utils import secure_filename



class Survey:
    @staticmethod
    def get_personal(alumnus):
        if alumnus.get("marital_status_id"):
            alumnus["marital_status"] = int(alumnus["marital_status_id"])

        alumnus["is_completed"] = (
            all(
                [
                    alumnus.get(x)
                    for x in [
                        "email",
                        "phone_number",
                        "home_address",
                        "marital_status_id",
                    ]
                ]
            )
            and int(alumnus.get("marital_status_id")) != 1
        )

        return alumnus

    @staticmethod
    def update_personal(data, id):
        db.execute(
            """UPDATE alumni SET marital_status_id = ?, email = ?, phone_number = ?, home_address = ?, submitted = ? WHERE id = ?;""",
            data["marital_status"],
            data["email"],
            data["phone_number"],
            data["home_address"],
            1,
            id,
        )

    @staticmethod
    def get_academic(alumnus):
        if alumnus.get("major_id"):
            alumnus["major"] = db.execute(
                "SELECT name FROM majors WHERE id = ?;", alumnus["major_id"]
            )[0]["name"]

        if alumnus.get("degree_id"):
            alumnus["degree"] = db.execute(
                "SELECT name FROM degrees WHERE id = ?;", alumnus["degree_id"]
            )[0]["name"]

        if alumnus.get("GPA"):
            alumnus["gpa"] = alumnus["GPA"] / 100

        if alumnus.get("postgrad") is not None:
            alumnus["postgraduate"] = (
                1 if alumnus["postgrad"] == 1 else 2 if alumnus["postgrad"] == 0 else 0
            )
        alumnus["is_completed"] = alumnus.get("postgraduate") and alumnus.get(
            "postgrad_reason"
        )

        return alumnus

    @staticmethod
    def update_academic(data, id):
        db.execute(
            """UPDATE alumni SET postgrad = ?, postgrad_reason = ?, submitted = ? WHERE id = ?;""",
            (
                1
                if data["postgraduate"] == 1
                else 0 if data["postgraduate"] == 2 else None
            ),
            data["postgrad_reason"],
            1,
            id,
        )

    @staticmethod
    def get_cv(alumnus):
        alumnus["is_completed"] = alumnus.get("cv") and alumnus.get("cv_file_name")
        return alumnus

    @staticmethod
    def get_cv_file(id):
        return db.execute("SELECT cv, cv_file_name FROM alumni WHERE id = ?;", id)[0]

    @staticmethod
    def update_cv(data, id):
        db.execute(
            "UPDATE alumni SET cv = ?, cv_file_name = ? WHERE id = ?;",
            sqlite3.Binary(data["cv"].read()),
            secure_filename(data["cv"].filename),
            id,
        )

    @staticmethod
    def get_employment(alumnus):
        if alumnus.get("work") is not None:
            alumnus["does_work"] = 1 if alumnus["work"] else 2

        if alumnus.get("work_reason"):
            alumnus["reason"] = alumnus["work_reason"]

        if alumnus.get("public_sector"):
            alumnus["sector"] = 1 if alumnus["public_sector"] else 2

        if alumnus.get("work_start_date"):
            alumnus["date"] = datetime.strptime(alumnus["work_start_date"], "%Y-%m-%d")

        if alumnus.get("work_place"):
            alumnus["place"] = alumnus["work_place"]

        if alumnus.get("work_address"):
            alumnus["address"] = alumnus["work_address"]

        if alumnus.get("work_phone"):
            alumnus["phone"] = alumnus["work_phone"]

        if alumnus.get("work_position"):
            alumnus["title"] = alumnus["work_position"]

        alumnus["is_completed"] = alumnus.get("does_work") and (
            alumnus.get("work_reason")
            or all(
                [
                    alumnus.get(x)
                    for x in [
                        "public_sector",
                        "work_place",
                        "work_start_date",
                        "work_address",
                        "work_phone",
                        "work_position",
                    ]
                ]
            )
        )
        return alumnus

    @staticmethod
    def update_employment(data, id):
        db.execute(
            """UPDATE alumni SET work = ?, public_sector = ?, work_place = ?, work_start_date = ?, work_address = ?, work_phone = ?, work_reason = ?, work_position = ?, submitted = ? WHERE id = ?;""",
            1 if data["does_work"] == 1 else 0 if data["does_work"] == 2 else None,
            1 if data["sector"] == 1 else 0 if data["sector"] == 2 else None,
            data["place"],
            data["date"],
            data["address"],
            data["phone"],
            data["reason"],
            data["title"],
            1,
            id,
        )

    @staticmethod
    def get_feedback(alumnus):
        for column, data in zip(
            ["follow", "communicate", "club"],
            ["does_follow", "does_communicate", "supports_club"],
        ):
            if alumnus.get(column) is not None:
                alumnus[data] = 1 if alumnus[column] else 2

        alumnus["is_completed"] = all(
            [
                alumnus.get(x)
                for x in ["does_follow", "does_communicate", "supports_club"]
            ]
        )
        return alumnus

    @staticmethod
    def update_feedback(data, id):
        db.execute(
            """UPDATE alumni SET suggestion = ?, follow = ?, communicate = ?, club = ?, submitted = ? WHERE id = ?;""",
            data["suggestion"],
            1 if data["does_follow"] == 1 else 0 if data["does_follow"] == 2 else None,
            (
                1
                if data["does_communicate"] == 1
                else 0 if data["does_communicate"] == 2 else None
            ),
            (
                1
                if data["supports_club"] == 1
                else 0 if data["supports_club"] == 2 else None
            ),
            1,
            id,
        )
