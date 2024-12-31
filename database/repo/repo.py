from database.database import db


class Repo:
    @staticmethod
    def get_news():
        return db.execute(
            "SELECT * FROM posts INNER JOIN news ON posts.id = news.id ORDER BY publish_date DESC;"
        )

    @staticmethod
    def get_news_post(id):
        post = dict(db.execute("SELECT * FROM posts WHERE id = ?;", id)[0])
        post["thumbnail"] = db.execute("SELECT thumbnail FROM news WHERE id = ?;", id)[
            0
        ]["thumbnail"]
        return post

    @staticmethod
    def get_post(id):
        return db.execute("SELECT * FROM posts WHERE id = ?;", id)[0]

    @staticmethod
    def get_thumbnail(id):
        return db.execute("SELECT thumbnail FROM news WHERE id = ?;", id)[0]["thumbnail"]