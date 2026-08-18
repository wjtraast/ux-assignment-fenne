from pyscript import web, when


def bereken_groei(beginwaarde, groeifactor, stappen):
    """Berekent y = beginwaarde * groeifactor^x voor x = 0 t/m stappen."""
    resultaten = []
    for x in range(stappen + 1):
        y = beginwaarde * groeifactor ** x
        resultaten.append((x, y))
    return resultaten


@when("click", "#bereken-knop")
def on_klik(event):
    beginwaarde = float(web.page["beginwaarde"].value or 0)
    groeifactor = float(web.page["groeifactor"].value or 0)
    stappen = int(web.page["stappen"].value or 0)

    if stappen < 0 or stappen > 20:
        web.page["uitkomst"].innerText = "Kies een aantal stappen tussen 0 en 20."
        return

    resultaten = bereken_groei(beginwaarde, groeifactor, stappen)
    regels = [f"x = {x}: y = {y:.2f}" for x, y in resultaten]
    web.page["uitkomst"].innerText = "\n".join(regels)
