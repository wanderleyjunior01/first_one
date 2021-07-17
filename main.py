from flask import Flask, render_template, request, redirect, jsonify
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from form import StudentForm
from flask_bootstrap import Bootstrap
from werkzeug.datastructures import ImmutableDict

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config["SECRET_KEY"] = "myveryhardtodiscoverysecretkey"

db = SQLAlchemy(app)

Bootstrap(app)

class StudentData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(264), unique=False, nullable=False)
    subject = db.Column(db.String(264), unique=False)
    fee = db.Column(db.Float(), unique=False)

# db.create_all()

@app.route("/", methods=["GET", "POST"])
def home():
    form  = StudentForm()
    if form.validate_on_submit():
        new_user = StudentData(name=form.name.data, subject=form.subject.data, fee=form.student_fee.data)
        db.session.add(new_user)
        db.session.commit()
    students_list = StudentData.query.all()
    return render_template("form2.html", form = form, data = students_list)

@app.route("/ajax_form", methods=["POST"])
def ajax_form():
    return "Hello, world"

@app.route("/att_list", methods=["POST"])
def att_list():
    data = StudentData.query.all()
    return data

@app.route("/delete", methods=["POST"])
def delete():
    if request.method == "POST":
        id_to_del = request.form["string"]
        delete_student = StudentData.query.filter_by(id=id_to_del).first()
        db.session.delete(delete_student)
        db.session.commit()
        return "Sucess", 200

@app.route("/edit", methods=["POST"])
def edit():
    imd = request.form
    transformed_data = imd.to_dict(flat=False)
    edit_student = StudentData.query.filter_by(id=str(transformed_data["id"][0])).first()
    edit_student.name = str(transformed_data["name"][0])
    edit_student.subject = transformed_data["subject"][0]
    edit_student.fee = transformed_data["fee"][0]
    db.session.commit()
    return "Sucess", 200


if __name__ == "__main__":
    app.run(debug=True)