from app import app, render, portofolios
from .forms import MyForm
from flask import redirect, flash
from . import mail, articles
from flask_mail import Message


@app.route("/")
def homepage():
    return render("homepage.html", portofolios=portofolios)
    # return render_template("homepage.html", portofolios=portofolios, path=request.path)


@app.route("/about-me", methods=["GET", "POST"])
def about_me():
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        company = form.company.data
        description = form.description.data
        msg = Message(
            f"{name} - {email} - {company}",
            body=description,
            recipients=["rexsyflaskportofolio@gmail.com"],
        )
        mail.send(msg)
        flash("Email Sent! 😁")
        return redirect("/about-me")
    return render("about-me.html", form=form)


@app.route("/blog")
def blog():
    return render("blog.html", articles=articles)
