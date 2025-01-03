from flask import Blueprint, redirect, render_template, request, session, send_file
from utils import alumni_required
from database.repo.alumnus import Alumnus
from database.repo.survey import Survey
from forms.survey.personal import PersonalForm
from forms.survey.academic import AcademicForm
from forms.survey.cv import CVForm
from forms.survey.employment import EmploymentForm
from forms.survey.feedback import FeedbackForm
from io import BytesIO

bp = Blueprint("survey", __name__)


@bp.route("/survey")
@alumni_required
def survey():
    alumnus = Alumnus.get_alumnus(session.get("username"))
    forms = [
        form(data=data(alumnus))
        for data, form in zip(
            (
                Survey.get_personal,
                Survey.get_academic,
                Survey.get_cv,
                Survey.get_employment,
                Survey.get_feedback,
            ),
            (PersonalForm, AcademicForm, CVForm, EmploymentForm, FeedbackForm),
        )
    ]

    for data, form in zip(
        (
            Survey.get_personal,
            Survey.get_academic,
            Survey.get_cv,
            Survey.get_employment,
            Survey.get_feedback,
        ),
        forms,
    ):
        form.is_completed = data(alumnus)["is_completed"]
    return render_template("alumni/survey.jinja", forms=forms)


@bp.route("/personal", methods=["POST"])
@alumni_required
def personal():
    alumnus = Alumnus.get_alumnus(session.get("username"))
    form = PersonalForm(data=alumnus)
    if form.validate_on_submit():
        Survey.update_personal(form.data, alumnus.get("id"))
    return redirect("/survey")


@bp.route("/academic", methods=["POST"])
@alumni_required
def academic():
    alumnus = Alumnus.get_alumnus(session.get("username"))
    form = AcademicForm(data=alumnus)
    if form.validate_on_submit():
        Survey.update_academic(form.data, alumnus.get("id"))
    return redirect("/survey")


@bp.route("/cv", methods=["GET", "POST"])
@alumni_required
def cv():
    if request.method == "GET":
        cv = Survey.get_cv_file(session.get("id"))
        cv_file = cv["cv"]
        cv_name = cv["cv_file_name"]
        return send_file(BytesIO(cv_file), as_attachment=True, download_name=cv_name)
    alumnus = Alumnus.get_alumnus(session.get("username"))
    form = CVForm(data=alumnus)
    if form.validate_on_submit():
        Survey.update_cv(form.data, alumnus.get("id"))
    return redirect("/survey")


@bp.route("/employment", methods=["POST"])
@alumni_required
def employment():
    alumnus = Alumnus.get_alumnus(session.get("username"))
    form = EmploymentForm(data=alumnus)
    if form.validate_on_submit():
        Survey.update_employment(form.data, alumnus.get("id"))
    return redirect("/survey")


@bp.route("/feedback", methods=["POST"])
@alumni_required
def feedback():
    alumnus = Alumnus.get_alumnus(session.get("username"))
    form = FeedbackForm(data=alumnus)
    if form.validate_on_submit():
        Survey.update_feedback(form.data, alumnus.get("id"))
    return redirect("/survey")
