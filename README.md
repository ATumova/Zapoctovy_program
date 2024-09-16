# Balancing Chemical Reactions
Tento program vyčísluje chemické rovnice. Uživatel zadá rovnici ve standardní notaci a program dopočítá, kolikrát se mají reaktanty a produkty objevit v dané rovnici, aniž by se ztrácela nebo materializovala hmota.
## Instalace
K tomu aby vše správně fungovalo tak je potřeba nainstalovat balíčky **tkinter** a **ChemPy**. To uděláme následovně:

- do terminálu napište *pip install tk* a spusťte, po chvíli byste měli mít balíček tkinter nainstalovaný
- poté udělejte to stejné pro ChemPy a do příkazového řádku napište *pip install chempy*

## Použití

- Po spuštění programu se nám objeví nové okno s políčkem pro zadání rovnice
- Do políčka zadejte vámi zvolenou chemickou reakci ve standardní notaci, kterou chcete vyčíslit
  - rovnice by měla být ve formátu: **reaktanty -> produkty**
  - jednotlivé reaktanty a produkty oddělujte znaménkem **'+'**
  - při zadávání záleží na malých a velkých písmenech
  - příklady správných zadání
    - H2 + O2 -> H2O
    - Pb(NO3)2 + KI -> PbI2 + KNO3
    - K2Cr2O7 + C2H5OH + H2SO4  -> KCr(SO4)2 + CH3CHO + H2O
- Pro získání výsledné vyčíslené rovnice stačí zmáčknout tlačítko **Balance Equation**
  - pro výše uvedené rovnice dostaneme tyto výsledky
    - 2 H2 + O2 -> 2 H2O
    - Pb(NO3)2 + 2 KI -> PbI2 + 2 KNO
    - K2Cr2O7 + 3 C2H5OH + 4 H2SO4  -> 2 KCr(SO4)2 + 3 CH3CHO + 7 H2O

## Jak program funguje
- program dostane zadanou rovnici `equation` ve formě stringu
- dále si program rovnici rozdělí na jednotlivé reaktanty a produkty pomocí této části kódu:
  ```python
    # Split the equation into reactants and products
    reactants, products = equation.split('->')

    # Split the reactants and products into individual compounds
    reactants = reactants.split('+')
    products = products.split('+')

    # Strip any leading or trailing whitespace from the compounds
    reactants = [r.strip() for r in reactants]
    products = [p.strip() for p in products]
  ```
- teď už máme dva seznamy `reactants` a `products` na které můžeme použít funkci balance_stoichiometry z balíčku ChemPy
  ```python
    reac, prod = balance_stoichiometry(reactants, products)
  ```
  - funkce balance_stoichiometry(reactants, products) nám vrátí dva slovníky `reac` a `prod` obsahující námi hledané koeficienty jednotlivých sloučenin
- nakonec jen poskládáme naši výslednou rovnici `balanced_equation`
  ```python
    coefficients = {**reac, **prod}
    # Create the balanced equation string
    balanced_equation = ' + '.join(f'{coefficients[r]} {r}' if coefficients[r] > 1 else r for r in reactants)
    balanced_equation += ' -> '
    balanced_equation += ' + '.join(f'{coefficients[p]} {p}' if coefficients[p] > 1 else p for p in products)
  ```
  
