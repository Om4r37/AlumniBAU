import sqlite3, csv
from database.database import db
from werkzeug.security import generate_password_hash
from io import StringIO
from datetime import datetime
from werkzeug.utils import secure_filename


class repo:
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
    def edit_admin_profile(data, id):
        db.execute(
            "UPDATE users SET display_name = ? WHERE id = ?;",
            data["display_name"],
            id,
        )

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

    @staticmethod
    def add_admin(id, username, password, name, manage, announce, alumni_data, mod):
        return db.execute(
            "INSERT INTO admins (id, username, password_hash, mod, name, manage, announce, alumni_data) VALUES (?, ?, ?, ?, ?, ?, ?, ?);",
            id,
            username,
            generate_password_hash(password),
            mod,
            name,
            manage,
            announce,
            alumni_data,
        )

    @staticmethod
    def add_admin(data):
        id = repo.get_last_user_id() + 1
        return db.execute(
            "INSERT INTO admins (id, username, password_hash, mod, manage, announce, stats) VALUES (?, ?, ?, ?, ?, ?, ?);",
            id,
            data["username"],
            generate_password_hash(data["password"]),
            data["mod"],
            data["manage"],
            data["announce"],
            data["stats"],
        )

    @staticmethod
    def get_admins(username):
        return db.execute("SELECT * FROM admins WHERE username = ?;", username)

    @staticmethod
    def get_admin(username):
        return repo.get_admins(username)[0]

    @staticmethod
    def get_admin_by_id(id):
        return db.execute("SELECT * FROM admins WHERE id = ?;", id)[0]

    @staticmethod
    def edit_admin(data, id):
        db.execute(
            "UPDATE admins SET mod = ?, manage = ?, announce = ?, stats = ? WHERE id = ?;",
            data["mod"],
            data["manage"],
            data["announce"],
            data["stats"],
            id,
        )

    @staticmethod
    def delete_admin(id):
        db.execute("DELETE FROM admins WHERE id = ?;", id)

    @staticmethod
    def get_all_admins(id):
        return db.execute("SELECT * FROM admins WHERE id != ? AND id != 1;", id)

    @staticmethod
    def is_admin(username):
        return repo.get_admins(username)

    @staticmethod
    def get_alumnus(username):
        alumni = repo.get_alumni(username)
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
    def get_alumnus_public_profile(id):
        alumnus = dict(repo.get_alumnus_by_id(id))
        user = dict(repo.get_user(id))
        data = {
            "Display Name": user.get("display_name"),
        }
        if alumnus.get("personal_privacy"):
            if alumnus.get("email"): data["Email"] = alumnus.get("email")
            if alumnus.get("phone_number"): data["Phone Number"] = alumnus.get("phone_number")
            if alumnus.get("home_address"): data["Home Address"] = alumnus.get("home_address")
            if alumnus.get("marital_status_id") != 1: data["Marital Status"] = repo.get_marital_status_by_id(
                alumnus.get("marital_status_id")
            )
        if alumnus.get("academic_privacy"):
            data["Major"] = repo.get_major_by_id(alumnus.get("major_id"))
            data["Degree"] = repo.get_degree_by_id(alumnus.get("degree_id"))
            data["GPA"] = alumnus.get("GPA") / 100
            data["Graduation Year"] = alumnus.get("graduation_year")
        if alumnus.get("employment_privacy"):
            if alumnus.get("work_place"): data["Work Place"] = alumnus.get("work_place")
            if alumnus.get("work_start_date"): data["Work Start Date"] = alumnus.get("work_start_date")
            if alumnus.get("work_address"): data["Work Address"] = alumnus.get("work_address")
            if alumnus.get("public_sector"): data["Sector"] = "Public" if alumnus.get("public_sector") else "Private"
            if alumnus.get("work_phone"): data["Work Phone"] = alumnus.get("work_phone")
        return data

    @staticmethod
    def get_user_public_profile(id):
        if repo.get_alumnus_by_id(id):
            return repo.get_alumnus_public_profile(id)
        user = dict(repo.get_user(id))
        return (
            {"Display Name": user.get("display_name")}
            if user.get("display_name")
            else {}
        )

    @staticmethod
    def get_user_full_profile(id):
        user = dict(repo.get_user(id))
        if repo.get_alumnus_by_id(id):
            user.update(dict(repo.get_alumnus_by_id(id)))
            user.pop("password_hash")
            user.pop("nno_hash")
        return user

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

    @staticmethod
    def get_alumni(username):
        return db.execute("SELECT * FROM alumni WHERE username = ?;", username)

    @staticmethod
    def is_alumni(username):
        return repo.get_alumni(username)

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
    def get_stats():
        return db.execute("SELECT * FROM stats")[0]

    @staticmethod
    def get_perms(username):
        admin = repo.get_admin(username)
        return [
            perm if admin[perm] else None
            for perm in ["mod", "manage", "announce", "stats"]
        ]

    @staticmethod
    def add_alumni(file):
        majors = {
            "علم الحاسوب": 1,
            "هندسة البرمجيات": 2,
            "نظم المعلومات الحاسوبية": 3,
            "الرسم الحاسوبي والرسوم المتحركة": 4,
            "الأمن السيبراني": 5,
        }
        degrees = {
            "بكالوريوس": 1,
            "ماجستير (مسار الرسالة)": 2,
            "ماجستير (مسار الشامل)": 3,
        }
        query = """
INSERT INTO alumni (
id,
username,
password_hash,
student_id,
full_name,
nationality,
nno_hash,
gender,
GPA,
major_id,
degree_id,
graduation_year,
graduation_semester,
phone_number,
work_place,
work_start_date,
work_address,
public_sector,
work_phone,
postgrad,
work
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        id = repo.get_last_user_id() + 1
        reader = csv.reader(StringIO(file.read().decode("utf-8")))
        next(reader)  # Skip header
        params = [
            (
                id + i,  # id
                row[0],  # username
                row[3],  # password_hash
                row[0],  # student_id
                row[1],  # full_name
                row[2],  # nationality
                row[3],  # nno_hash
                0 if row[4] == "ذكر" else 1,  # gender
                int(float(row[5]) * 100),  # GPA
                majors[row[6]],  # major_id
                degrees[row[7]],  # degree_id
                row[8].split("/")[1],  # graduation_year
                row[9],  # graduation_semester
                row[10],  # phone
                row[11],  # work_place
                row[12],  # work_start_date
                row[13],  # work_address
                (
                    1 if row[14] == "العام" else 0 if row[14] == "الخاص" else None
                ),  # public_sector
                row[15],  # work_phone
                1 if row[7] != "بكالوريوس" else None,  # postgrad
                1 if row[11] else None,  # work
            )
            for i, row in enumerate(reader)
        ]
        db.execute_many(query, params)
        return len(params)

    @staticmethod
    def hash_file(file_path):
        rows = []
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            rows.append(next(reader))  # header
            for row in reader:
                row[3] = generate_password_hash(row[3])
                rows.append(row)
        with open(file_path, "w") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
