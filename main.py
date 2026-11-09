from pyscript import document

# Non-metal elements, indexed by symbol
Elements = {
    'H': 'Symbol: H <br> Name: Hydrogen <br> Atomic Number: 1 <br> Molar Mass: 1.008 g/mol',
    'He': 'Symbol: He <br> Name: Helium <br> Atomic Number: 2 <br> Molar Mass: 4.0026 g/mol',
    'C': 'Symbol: C <br> Name: Carbon <br> Atomic Number: 6 <br> Molar Mass: 12.011 g/mol',
    'N': 'Symbol: N <br> Name: Nitrogen <br> Atomic Number: 7 <br> Molar Mass: 14.007 g/mol',
    'O': 'Symbol: O <br> Name: Oxygen <br> Atomic Number: 8 <br> Molar Mass: 15.999 g/mol',
    'F': 'Symbol: F <br> Name: Fluorine <br> Atomic Number: 9 <br> Molar Mass: 18.998 g/mol',
    'Ne': 'Symbol: Ne <br> Name: Neon <br> Atomic Number: 10 <br> Molar Mass: 20.180 g/mol',
    'P': 'Symbol: P <br> Name: Phosphorus <br> Atomic Number: 15 <br> Molar Mass: 30.974 g/mol',
    'S': 'Symbol: S <br> Name: Sulfur <br> Atomic Number: 16 <br> Molar Mass: 32.06 g/mol',
    'Cl': 'Symbol: Cl <br> Name: Chlorine <br> Atomic Number: 17 <br> Molar Mass: 35.45 g/mol',
    'Ar': 'Symbol: Ar <br> Name: Argon <br> Atomic Number: 18 <br> Molar Mass: 39.948 g/mol',
    'Se': 'Symbol: Se <br> Name: Selenium <br> Atomic Number: 34 <br> Molar Mass: 78.971 g/mol',
    'Br': 'Symbol: Br <br> Name: Bromine <br> Atomic Number: 35 <br> Molar Mass: 79.904 g/mol',
    'Kr': 'Symbol: Kr <br> Name: Krypton <br> Atomic Number: 36 <br> Molar Mass: 83.798 g/mol',
    'I': 'Symbol: I <br> Name: Iodine <br> Atomic Number: 53 <br> Molar Mass: 126.90 g/mol',
    'Xe': 'Symbol: Xe <br> Name: Xenon <br> Atomic Number: 54 <br> Molar Mass: 131.29 g/mol',
    'Rn': 'Symbol: Rn <br> Name: Radon <br> Atomic Number: 86 <br> Molar Mass: (222) g/mol'
}
#displays the element typed
def show_element(_):
    symbol = document.getElementById('elementInput').value.strip().capitalize()
    results = document.getElementById('results')
    results.innerHTML = Elements.get(symbol, 'Element not found. Enter a valid non-metal symbol.') #if non metal is not typed or if nothing is type at all