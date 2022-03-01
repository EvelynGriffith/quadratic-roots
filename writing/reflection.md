# Quadratic Roots

TODO: Please delete each of the TODO markers entirely and ensure that all of
the text including in this document is written and formatted in a professional
fashion. Do not leave the remainder of a TODO prompt in this document unless
it supports your response to a specific question.

## Evelyn Griffith

## Program Output

### What is the output from running the `rootfinder` program?

```⭐ Calculating the roots of the quadratic equation with:
a = 4.0
b = 6.0
c = 2.0
⭐ Finished computing the roots of the equation as:
x_one = -0.5

x_two = -1.0
```

```⭐ Calculating the roots of the quadratic equation with:
a = 12.0
b = 13.0
c = 7.0
⭐ Finished computing the roots of the equation as:
x_one = (-0.5416666666666666+0.5384519993050035j)

x_two = (-0.5416666666666666-0.5384519993050035j)
```

### What is the output from running the test suite for the `rootfinder` program?

```===================================================== test session starts ======================================================
platform win32 -- Python 3.8.2, pytest-7.0.1, pluggy-1.0.0
rootdir: C:\Users\gforc\computer-science-102-spring-2022-ee-2-quadratic-roots-EvelynGriffith\rootfinder
collected 3 items

tests\test_rootfind.py ...

====================================================== 3 passed in 0.08s ======================================================
```

## Source Code and Configuration Files

### Describe in detail how your provided source code works

#### A source code statement that makes the `rootfind` module available to `main`

```from rootfinder import rootfind```

This statement lies in the main.py file as an import statement. This is a very interesting import because it lives in the main module(or file) and it reaches into the directory of the rootfind.py file and it links together the two files so that functions can be accessed between the two of them. This is really important for the main.py because when the main.py runs the CLI function it needs the ```calculate_quadratic_equation_roots``` function in order to actually calculate any of the information we need.

#### A function signature that defines `rootfind`'s command-line arguments

TODO: Use a fenced code block to provide the requested source code
TODO: Write at least one paragraph to explain the request source code

#### A source code statement that creates a new instance of the `Console` class

TODO: Use a fenced code block to provide the requested source code
TODO: Write at least one paragraph to explain the request source code

### After reading the assignment sheet and the referenced resources, what are "imaginary" numbers?

TODO: Provide a one-paragraph response that answers this question in your own words.

### After completing this assignment, what is one experience for which you are grateful?

TODO: Provide a one-paragraph response that answers this question in your own words.
