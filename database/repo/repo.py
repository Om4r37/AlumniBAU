from database.database import db


class Repo:
    @staticmethod
    def get_news():
        return db.execute(
            "SELECT * FROM posts WHERE id IN (SELECT id FROM news) ORDER BY publish_date DESC;"
        )
