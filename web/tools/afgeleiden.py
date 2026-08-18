from pyscript import web, when


def bereken_afgeleide(termen):
    """Berekent de afgeleide van een veelterm met de machtsregel.

    termen is een lijst van (coëfficiënt, macht) tuples.
    Geeft een nieuwe lijst van (coëfficiënt, macht) tuples terug.
    """
    afgeleide_termen = []

    for coefficient, macht in termen:
        if macht > 0:
            nieuwe_coefficient = coefficient * macht
            nieuwe_macht = macht - 1
            if nieuwe_coefficient != 0:
                afgeleide_termen.append((nieuwe_coefficient, nieuwe_macht))

    return afgeleide_termen


def naar_tekst(termen):
    """Zet een lijst (coëfficiënt, macht) termen om naar leesbare tekst, bijv. '4x^3 + 2x'."""
    if not termen:
        return "0"

    delen = []
    for coefficient, macht in termen:
        if macht == 0:
            delen.append(f"{coefficient:g}")
        elif macht == 1:
            delen.append(f"{coefficient:g}x")
        else:
            delen.append(f"{coefficient:g}x^{macht}")

    return " + ".join(delen).replace("+ -", "- ")


@when("click", "#bereken-knop")
def on_klik(event):
    velden_en_machten = [("coef-4", 4), ("coef-3", 3), ("coef-2", 2), ("coef-1", 1), ("coef-0", 0)]

    termen = []
    for veld_id, macht in velden_en_machten:
        coefficient = float(web.page[veld_id].value or 0)
        termen.append((coefficient, macht))

    afgeleide = bereken_afgeleide(termen)
    web.page["uitkomst"].innerText = f"f'(x) = {naar_tekst(afgeleide)}"
