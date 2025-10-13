from flask import Flask , render_template , request , redirect
from flask_sqlalchemy import SQLAlchemy
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

    def __repr__(self):
        return f"<EXPENSE {self.category} - {self.amount}>"
    

@app.route("/")
def index():
    expenses = Expense.query.all()
    total = sum(exp.amount for exp in expenses)
    return render_template("index.html" , expenses = expenses , total = total )


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
    if Expense:
        db.session.delete(Expense)
        db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)