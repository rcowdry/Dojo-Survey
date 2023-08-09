#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for, session
import datetime

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/checkout", methods=["POST"])
def checkout():
    # form_data =[]
    session["strawberry_count"] = int(request.form.get("strawberry"))
    session["raspberry_count"] = int(request.form.get("raspberry"))
    session["apple_count"] = int(request.form.get("apple"))
    session["total_count"] = (
        session["strawberry_count"]
        + session["raspberry_count"]
        + session["apple_count"]
    )
    session["first_name"] = request.form.get("first_name")
    session["last_name"] = request.form.get("last_name")
    session["customer_name"] = session["first_name"] + session["last_name"]
    session["student_id"] = request.form.get("student_id")
    session["current_time"] = datetime.datetime.now()
    # session['orm_data'] = [
    #     strawberry_count,
    #     raspberry_count,
    #    session['apple_count'],
    #     total_count,
    #    session[' first_name'],
    #    session[' last_name'],
    #     customer_name,
    #     student_id,
    #     current_time,
    # ]
    # form_data.extend(orm_data)

    print(f"Charging {session['first_name']} for {session['total_count']} fruits")

    # return render_template(
    #     "checkout.html",
    #     strawberry_count=strawberry_count,
    #     raspberry_count=raspberry_count,
    #    session['apple_count']=apple_count,
    #     total_count=total_count,
    #    session[' first_name']=first_name,
    #    session[' last_name']=last_name,
    #     customer_name=customer_name,
    #     student_id=student_id,
    #     current_time=current_time,
    # )
    return redirect(url_for("show_checkout"))


@app.route("/show")
def show_checkout():
    return render_template(
        "checkout.html",
        strawberry_count=session["strawberry_count"],
        raspberry_count=session["raspberry_count"],
        apple_count=session["apple_count"],
        total_count=session["total_count"],
        first_name=session["first_name"],
        last_name=session["last_name"],
        customer_name=session["customer_name"],
        student_id=session["student_id"],
        current_time=session["current_time"],
    )


@app.route("/result", methods=["POST"])
def result():
    print(request.form)
    session["user_name"] = request.form.get("user_name")
    session["location"] = request.form.get("dojoLocation")
    session["langauge_choice"] = request.form.get("languageChoice")
    session["comment"] = request.form.get("textarea")
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)
