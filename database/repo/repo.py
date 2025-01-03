from database.database import db


class Repo:
    @staticmethod
    def get_news():
        return db.execute(
            """
            SELECT posts.*, news.*, users.display_name, users.profile_picture 
            FROM posts 
            INNER JOIN news ON posts.id = news.id 
            INNER JOIN users ON posts.user_id = users.id 
            WHERE archived = FALSE 
            ORDER BY publish_date DESC;
            """
        )

    @staticmethod
    def get_news_post(id):
        post = dict(
            db.execute(
                """
SELECT posts.*, users.display_name, users.profile_picture 
FROM posts 
INNER JOIN users ON posts.user_id = users.id 
WHERE posts.id = ?;
                """,
                id,
            )[0]
        )
        post["thumbnail"] = db.execute("SELECT thumbnail FROM news WHERE id = ?;", id)[
            0
        ]["thumbnail"]
        if not post.get("profile_picture"):
            with open("static/pics/pfp.png", "rb") as f:
                post["profile_picture"] = f.read()
        return post

    @staticmethod
    def get_post(id):
        post = dict(
            db.execute(
                """
SELECT posts.*, users.display_name, users.profile_picture 
FROM posts 
INNER JOIN users ON posts.user_id = users.id 
WHERE posts.id = ?;
                """,
                id,
            )[0]
        )
        if not post.get("profile_picture"):
            with open("static/pics/pfp.png", "rb") as f:
                post["profile_picture"] = f.read()
        return post

    @staticmethod
    def get_thumbnail(id):
        return db.execute("SELECT thumbnail FROM news WHERE id = ?;", id)[0][
            "thumbnail"
        ]

    @staticmethod
    def get_comments(id):
        return db.execute(
            """
            SELECT comments.*, users.display_name, users.profile_picture 
            FROM comments 
            INNER JOIN users ON comments.user_id = users.id 
            WHERE post_id = ? 
            ORDER BY publish_date DESC;
            """,
            id,
        )