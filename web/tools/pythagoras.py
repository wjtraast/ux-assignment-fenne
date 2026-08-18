from math import sqrt

from pyscript import web, when


def bereken_zijde(a, b, c):
    """Berekent de ontbrekende zijde van een rechthoekige driehoek.

    Precies één van de drie zijden moet 0 zijn; die wordt berekend.
    Geeft (waarde, naam) terug, of (None, None) als de invoer niet klopt.
    """
    if c == 0:
        return sqrt(a ** 2 + b ** 2), "c"
    elif a == 0:
        return sqrt(c ** 2 - b ** 2), "a"
    elif b == 0:
        return sqrt(c ** 2 - a ** 2), "b"
    else:
        return None, None


@when("click", "#bereken-knop")
def on_klik(event):
    a = float(web.page["zijde-a"].value or 0)
    b = float(web.page["zijde-b"].value or 0)
    c = float(web.page["zijde-c"].value or 0)

    waarde, naam = bereken_zijde(a, b, c)

    if waarde is None:
        web.page["uitkomst"].innerText = "Laat precies één zijde leeg (of op 0)."
    else:
        web.page["uitkomst"].innerText = f"Zijde {naam} is {waarde:.2f}"
