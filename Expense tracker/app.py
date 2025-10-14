from flask import Flask , render_template , request , redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from collections import defaultdict
import os

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(BASE_DIR , "expenses.db")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    category = db.Column(db.String(50) , nullable = False )
    amount = db.Column(db.Float, nullable = False)
    date = db.Column(db.DateTime, default=datetime.now)
    VALID_CATEGORIES = ["Food", "Travel", "Shopping", "Bills", "Others"]

    def __repr__(self):
        return f"<EXPENSE {self.category} - {self.amount} - {self.date}>"
    

@app.route("/")
def index():
    expenses = Expense.query.all()
    total = sum(exp.amount for exp in expenses)

    show_more = len(expenses) > 6 
    first_six  = expenses[:6] 
    return render_template("index.html" , expenses = first_six , total = total , show_more=show_more)


@app.route("/add" , methods = ["POST"])
def add_expense():
    category = request.form["category"]
    amount = float(request.form["amount"])
    new_expense = Expense(category=category , amount = amount )
    db.session.add(new_expense)
    db.session.commit()
    return redirect("/")


@app.route("/delete/<int:id>")
def delete_expense(id):
    expense = Expense.query.get_or_404(id)  
    if expense:
     db.session.delete(expense)
     db.session.commit()
    return redirect("/")

@app.route("/all")
def all_expenses():
    expenses = Expense.query.order_by(Expense.date.desc()).all()
    total = sum(exp.amount for exp in expenses)
    return render_template("all_expenses.html", expenses=expenses, total=total)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)