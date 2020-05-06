from tdd_tutorial.demo.shoppinglist import ShoppingList


def test_constructor():
    testlist = ShoppingList()
    assert testlist.__len__() == 0
