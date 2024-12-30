from database.database import db


class Repo:
    @staticmethod
    def get_news():
        return db.execute(
            "SELECT * FROM posts INNER JOIN news ON posts.id = news.id ORDER BY publish_date DESC;"
        )

    @staticmethod
    def get_post(id):
        return db.execute("SELECT * FROM posts JOIN news WHERE posts.id = ?;", id)[0]
