# Quadratic Roots

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

```x_one, x_two = rootfind.calculate_quadratic_equation_roots(a,b,c)```

This peice of code lies in the command line interface function. It is important because it is the line that actually calls on the rootfind.py file and then uses its function called ```calculate_quadratic_equation_roots```. However, this peice of code also calls directly on the functions inputs and outputs. You can see that it is using a,b,and c which are defined as float values, but it is also stating that we will have a Tuple as a output with the values x_one, and x_two making up its data points.

#### A source code statement that creates a new instance of the `Console` class

```console = Console()
    console.print()
```

These two lines are doing two important things in the main.py file within the CLI function. The first line of code is the instance that is creating a new Console class from the ```from rich.console import Console``` import statement at the top of the file. This then allows us to use the second line of the example in order to print things through the console. This is particularly useful whe using f-strings with several different variables.

### After reading the assignment sheet and the referenced resources, what are "imaginary" numbers?

The way that I understand imaginary numbers after doing a bit of research is that they are used to measure numbers that "do not exist". In math this is represented as i but in python this is represented as j. However, just because these numbers are said to "not exist" in math doesnt mean that they aren't important. The way that I have chosen to think of them is that they represent space and time that isnt actually there. Like negative space, or negative time. It doesnt really make sense because the world is made up of some kind of matter, and time can't move backwards. However, these numbers are still important because they represent the idea of something that we can comprehend but doesnt necessarily exist, and they can obviously still lead to important "real" answers.

### After completing this assignment, what is one experience for which you are grateful?

I am really grateful that during this lab I was able to have a relatively smooth experience. I am thankful that I understand the code well and I am really happy that I was able to get it working well. I think I have had A LOT of experiences where labs were difficult or tedious and this one, although there were defintely challenges to it, it was nice because it made me feel capable of being successful in this feild. I dont feel like that very often so this was a welcome change.
