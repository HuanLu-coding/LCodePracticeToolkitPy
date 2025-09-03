# 1169. Invalid Transactions

# A transaction is possibly invalid if:
# - The amount exceeds $1000, or
# - It occurs within (and including) 60 minutes of another transaction with the same name in a different city.
#
# You are given an array of strings transactions where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.
#
# Return a list of transactions that are possibly invalid. You may return the answer in any order.
#
# ### Constraints:
# - transactions.length <= 1000
# - Each transactions[i] takes the form "{name},{time},{amount},{city}"
# - Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
# - Each {time} consists of digits, and represent an integer between 0 and 1000.
# - Each {amount} consists of digits, and represent an integer between 0 and 2000.
#
# ### Example 1:
# Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
# Output: ["alice,20,800,mtv","alice,50,100,beijing"]
# Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, has the same name, and is in a different city. Similarly, the second one is invalid too.
#
# ### Example 2:
# Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
# Output: ["alice,50,1200,mtv"]
#
# ### Example 3:
# Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
# Output: ["bob,50,1200,mtv"]

from test.test_suite import run_tests
from typing import *


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # 解析交易并按人名分组
        records = []
        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(',')
            records.append({
                'name': name,
                'time': int(time),
                'amount': int(amount),
                'city': city,
                'index': i,
                'raw': t
            })

        # 按人名分组
        name_to_transactions = {}
        for rec in records:
            if rec['name'] not in name_to_transactions:
                name_to_transactions[rec['name']] = []
            name_to_transactions[rec['name']].append(rec)
        print('name_to_transactions: ', name_to_transactions)

        # 标记无效交易
        invalid = set()
        for name, trans in name_to_transactions.items():
            n = len(trans)
            for i in range(n):
                # 条件 1：金额 > 1000
                if trans[i]['amount'] > 1000:
                    invalid.add(trans[i]['index'])
                # 条件 2：60 分钟内不同城市
                for j in range(i + 1, n):
                    if abs(trans[i]['time'] - trans[j]['time']) <= 60 and trans[i]['city'] != trans[j]['city']:
                        invalid.add(trans[i]['index'])
                        invalid.add(trans[j]['index'])

        # 返回原始无效交易
        return [records[i]['raw'] for i in sorted(invalid)]


test_cases = [
    {
        "method": "invalidTransactions",
        "transactions": ["alice,20,800,mtv", "alice,50,100,beijing"],
        "expected": ["alice,20,800,mtv", "alice,50,100,beijing"],
        "case_id": 1,
        "description": "Two transactions with same name in different cities within 60 minutes"
    },
    {
        "method": "invalidTransactions",
        "transactions": ["alice,20,800,mtv", "alice,50,1200,mtv"],
        "expected": ["alice,50,1200,mtv"],
        "case_id": 2,
        "description": "Transaction amount exceeds $1000"
    },
    {
        "method": "invalidTransactions",
        "transactions": ["alice,20,800,mtv", "bob,50,1200,mtv"],
        "expected": ["bob,50,1200,mtv"],
        "case_id": 3,
        "description": "Different names; only bob's transaction is invalid due to amount"
    },
    {
        "method": "invalidTransactions",
        "transactions": ["alice,20,800,mtv"],
        "expected": [],
        "case_id": 4,
        "description": "Single transaction under $1000; no invalid transactions"
    },
    {
        "method": "invalidTransactions",
        "transactions": ["alice,20,800,mtv", "alice,50,100,mtv"],
        "expected": [],
        "case_id": 5,
        "description": "Same name and city within 60 minutes; both valid"
    },
    {
        "method": "invalidTransactions",
        "transactions": ["alice,20,800,mtv", "alice,85,100,beijing"],
        "expected": [],
        "case_id": 6,
        "description": "Same name, different cities, but time difference > 60 minutes"
    },
    {
        "method": "invalidTransactions",
        "transactions": ["alice,20,800,mtv", "alice,50,100,beijing", "alice,55,100,shanghai"],
        "expected": ["alice,20,800,mtv", "alice,50,100,beijing", "alice,55,100,shanghai"],
        "case_id": 7,
        "description": "Multiple transactions with same name in different cities within 60 minutes"
    }
]

run_tests()
