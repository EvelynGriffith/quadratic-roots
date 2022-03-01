"""Calculate the roots of a quadratic equation given values for a, b, and c."""

from rich.console import Console

import typer

from rootfinder import rootfind

# create a Typer object to support the command-line interface
cli = typer.Typer()


@cli.command()
def main(
    a: float = typer.Option(1), b: float = typer.Option(2), c: float = typer.Option(2)
):
    """Calculate the roots of a quadratic equation using the quadratic formula."""
    # create a console for rich text output
    console = Console()
    console.print()
    # TODO: display the debugging output for the program's command-line arguments
    # display three lines of output following the expected output
    # --> A label describing the output values
    console.print()
    console.print(":Star: Calculating the roots of the quadratic equation with:")
    # --> The value of a
    console.print(f"a = {a}")
    # --> The value of b
    console.print(f"b = {b}")
    # --> The value of c
    console.print(f"c = {c}")
    # --> You can display the "star" emoji by using :star:
    # call the function that performs the calculation of the roots for the quadratic equation
    x_one, x_two = rootfind.calculate_quadratic_equation_roots(a,b,c)
    # output the values from running the calculation of the quadratic
    # equation's roots with the calculate_quadratic_equation_roots function
    console.print(f":star: Finished computing the roots of the equation as:")
    # display three lines of output following the expected output
    # --> A label describing the output values
    # --> The value of x_one
    console.print(f"x_one = {x_one}")
    # display a blank line for separation from the first output segment
    console.print()
    # --> The value of x_two
    console.print(f"x_two = {x_two}")
    console.print()
