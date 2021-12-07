from os import path
from flask import Flask
from flask import request, jsonify
from flask.blueprints import Blueprint
from flask_sqlalchemy import sqlalchemy

from cashman.model.expense import Expense, ExpenseSchema
from cashman.model.income import Income, IncomeSchema
from cashman.model.transaction_type import TransactionType
from flask_login import login_required, current_user


#app = Flask(__name__)
index = Blueprint('index', __name__)

transactions = [

    Income('Salary', 5000),
    Income('Dividends', 200),
    Expense('pizza', 50),
    Expense('Rock Concert', 100)

]

@index.route('/incomes')
@login_required
def get_incomes():
    schema = IncomeSchema(many=True)
    incomes = schema.dump(
        filter(lambda t: t.type == TransactionType.INCOME, transactions)

    )
    return jsonify(incomes)

@index.route('/incomes', methods=['POST'])
def add_income():
    income = IncomeSchema().load(request.get_json())
    transactions.append(income)

    return '', 204

@index.route('/expenses')
@login_required
def get_expenses():
    schema = ExpenseSchema(many=True)
    expenses = schema.dump(

        filter(lambda t: t.type == TransactionType.EXPENSE, transactions)

    )
    return jsonify(expenses)

@index.route('/expenses', methods=['POST'])
def add_expense():
    expense = ExpenseSchema().load(request.get_json())
    transactions.append(expense)
    return "", 204

#if __name__ == "__main__":
#   app.run()