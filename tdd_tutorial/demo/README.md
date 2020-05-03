Instructions for running the demo
=================================
The instructor will demonstrate a TDD example which has been shamelessly stolen 
from the Realpython TDD tutorial: 
https://realpython.com/courses/test-driven-development-pytest/

Please feel free to visit tutorial Realpython, but we want to do it live here so
that we can inject our own prejudices and propaganda.

The objective is to develop a python class called ``ShoppingList`` that does 
more or less exactly 
what`a list does in Python, so it is pretty pointless, but the point is NOT
 1. what the class does
 1. how it does it
 1. whether there is a better way to do it
 
so please try to hold back with any thoughts you have on that (I am looking at 
you Songsheng).  The entire purpose is to explore the test-driven development
***philosophy*** and ***workflow*** with a somewhat simple example.

Step 1
------
1. STOP (this is the opposite of what you usually do, I know, so let's start
   by breaking bad habits)
1. THINK (I know, breaking more bad habits)
1. Ask the question, What do I want this code to do?  In this example we want
   to make a Python class that holds a shopping list.  Simon likes to iterrogate
   the situation with what he calls Use Cases.  So let's pause and make a UC to
   get a clear idea of what the code should do.  It consists of a series of 
   actions, written in a bullet list, each one starting with an actor.  This
   avoids the situation where the customer (e.g., beamline scientist) says, 
   "I want a program to make data acquisition easier" and you are expected to
   code to that specification.
1. 