from functools import wraps
from flask import redirect, session


def login_required(f):
    """
    Decorate routes to require login.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def alumni_required(f):
    """
    Decorate routes to require alumni.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("role") != "alumnus":
            return redirect("/")
        return f(*args, **kwargs)

    return decorated_function


def admin_required(f):
    """
    Decorate routes to require an admin account.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("role") != "admin":
            return redirect("/")
        return f(*args, **kwargs)

    return decorated_function


def manager_required(f):
    """
    Decorate routes to require a manager account.
    """

    @admin_required
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "manage" not in session.get("perms"):
            return redirect("/")
        return f(*args, **kwargs)

    return decorated_function


def data_access_required(f):
    """
    Decorate routes to require access to alumni info.
    """

    @admin_required
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "stats" not in session.get("perms"):
            return redirect("/")
        return f(*args, **kwargs)

    return decorated_function


def announcer_required(f):
    """
    Decorate routes to require announcing permission.
    """

    @admin_required
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "announce" not in session.get("perms"):
            return redirect("/")
        return f(*args, **kwargs)

    return decorated_function


def mod_permission_required(f):
    """
    Decorate routes to require mod permissions.
    """

    @admin_required
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "mod" not in session.get("perms"):
            return redirect("/")
        return f(*args, **kwargs)

    return decorated_function
