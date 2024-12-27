import csv
from database.database import db
from werkzeug.security import generate_password_hash
from datetime import datetime
from io import StringIO
from database.repo.user import User


class Admin:
    @staticmethod
    def edit_admin_profile(data, id):
        db.execute(
            "UPDATE users SET display_name = ? WHERE id = ?;",
            data["display_name"],
            id,
        )

    @staticmethod
    def add_admin(data):
        id = User.get_last_user_id() + 1
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
        return Admin.get_admins(username)[0]

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
        name = Admin.get_admin_by_id(id)["username"]
        db.execute("DELETE FROM admins WHERE id = ?;", id)
        return name

    @staticmethod
    def get_all_admins(id):
        return db.execute("SELECT * FROM admins WHERE id != ? AND id != 1;", id)

    @staticmethod
    def is_admin(username):
        return Admin.get_admins(username)

    @staticmethod
    def get_stats():
        return db.execute("SELECT * FROM stats")[0]

    @staticmethod
    def get_perms(username):
        admin = Admin.get_admin(username)
        return [
            perm if admin[perm] else None
            for perm in ["mod", "manage", "announce", "stats"]
        ]

    @staticmethod
    def create_announcement(data, id):
        id = db.execute(
            "INSERT INTO posts (user_id, content, publish_date) VALUES (?, ?, ?);",
            id,
            data["content"],
            datetime.now(),
        )
        db.execute("INSERT INTO news (id) VALUES (?);", id)

    @staticmethod
    def update_password(user_id, password):
        db.execute(
            "UPDATE admins SET password_hash = ? WHERE id = ?;",
            generate_password_hash(password),
            user_id,
        )

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
        id = User.get_last_user_id() + 1
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
