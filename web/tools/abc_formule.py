from math import sqrt

from pyscript import web, when


def bereken_abc(a, b, c):
    """Lost ax^2 + bx + c = 0 op met de ABC-formule."""
    d = b ** 2 - 4 * a * c

    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return f"Twee oplossingen: x = {x1:.2f} of x = {x2:.2f}"
    elif d == 0:
        x = -b / (2 * a)
        return f"Eén oplossing: x = {x:.2f}"
    else:
        return "Geen echte oplossingen (de discriminant is negatief)."


@when("click", "#bereken-knop")
def on_klik(event):
    a = float(web.page["coef-a"].value or 0)
    b = float(web.page["coef-b"].value or 0)
    c = float(web.page["coef-c"].value or 0)

    if a == 0:
        web.page["uitkomst"].innerText = "a mag niet 0 zijn, anders is het geen kwadratische vergelijking."
    else:
        web.page["uitkomst"].innerText = bereken_abc(a, b, c)
