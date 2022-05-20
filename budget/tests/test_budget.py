from applications.Budget import BudgetApp

def test_budget1():
    testobj = BudgetApp("category")
    assert test_budget1.get_balance() == 0
    
def test_budget2():
    testobj = BudgetApp("category")
    assert test_budget1.deposit(429)
    assert test_budget1.get_balance() == 429
    