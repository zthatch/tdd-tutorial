Crib for how to run the tutorial
================================

Goals of the tutorial
---------------------
1. to understand the importance of TDD
1. to learn basics of how to do it.

Pair Programming
----------------
1. introduce the concept:
    1. Driver and Navigator
    1. Driver generally the less experienced 
    1. RULE: only driver is allowed to type (except for Googling)
1. Show people who will be their pairs
1. Pick a pair and have them do a hello-world program as a demo
    1. learning objective is a functional pair
    1. how to talk to each other
    1. reach consensus before moving forward but be quick
    1. if navigator knows the answer, give driver space to find it themselves 
       before prescribing what to type
1. Test pair programming organization infrastructure

Demo - our very first test
--------------------------
1. hello world function simply returns 'hello world' string
1. how would we test it? 
    1. ``if __main__ == '__name__'`` calls then prints
    1. show that this can now be run on CL
    1. show how to set up pycharm to run it from pycharm
1. this is not a test!  or it might be called a functional test but it is not 
   we are talking about when we talk about unit-testing
1. python unittest vs pytest.  We will use pytest
1. write our first test.  
    1. in the same file for now
    1. ``test_hello`` but just ``assert True``
    1. show how to run it at the CL
    1. show how to set up pycharm to run it
1. The purpose of tests is not to pass!  Or we would be done. It is to  make
   sure the function has the functionality we want it to have
1. We want it to return a string ``hello world``
    1. assert isinstance(str)
    1. assert the string is ``hello world``
1. make the test more interesting ``hello(person)``
1. This is where TDD comes in
    1. write the test first
    1. make sure it fails
    1. write the code until it passes
1. how to test multiple times => multiple asserts
    1. just use different people for now
1. how to test multiple times => pytest.parametrize
1. want capitalization because we are polite people
1. want it to just return a first name because we are friendly
1. how to handle names written in different ways
1. how to handle a list of names
1. how to handle something it doesn't know what to do with

Making a more robust testing structure in your package
------------------------------------------------------
1. move testing code to module named test_module_name.py in directory tests

Second testing demo - shopping list
-----------------------------------
1. Introduce STOP, THINK, use paper
1. introduce the UC.  Put it in the module docstring.
1. sketch out the structure of the class
    1. constructor
    1. add_item(item)
    1. sort_for(shop)
    1. find(item)
    1. cant_find(item)
1. write the class but each method is just pass
1. start the docstring
1. TDD, write tests for each to capture the functionality in the UC
1. iterate the docstring as you struggle to understand the UC
1. start coding until each test passes, one by one

Hands on task (in pairs)
------------------------
1. read the readme in the hands_on folder for instructions
1. use the standard pair programming workflow, though when you are both more
   experienced you can split up so one person writes the tests and the other
   person writes the code
   
Follow on tasks
---------------
if you have time, pick an issue from regolith and bang it out together

    
