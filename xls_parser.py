import pandas as pd
import os

from parse_result import ParseResult
from transaction import Transaction


def extract_expenses(df):
    expenses = df[pd.notna(df.expense)].copy()
    return list(expenses.T.to_dict().values())


def parse_xls(filename) -> ParseResult:
    df = pd.read_excel(os.getcwd() + "/" + filename)
    size = len(df)
    df = df[6:size]
    df = df.rename(
        columns={"Unnamed: 1": "date", "Unnamed: 2": "description", "Unnamed: 4": "expense", "Unnamed: 5": "income",
                 "Unnamed: 6": "balance"})
    df = df[['date', 'description', 'expense', 'income', 'balance']]

    initial_balance = round(df[df.description == 'SALDO ANTERIOR'].balance.values[0])
    end_balance = round(df[df.description == 'SALDO FINAL'].balance.values[0])
    expenses = extract_expenses(df)

    return ParseResult(initial_balance, end_balance, expenses, [])
