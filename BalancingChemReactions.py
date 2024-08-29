import re
from chempy import balance_stoichiometry
import tkinter as tk
from tkinter import messagebox

# Define the validation function
def validate_equation(equation):
    # Split the equation into reactants and products
    reactants, products = equation.split('->')
    # Find the elements used in reactants  and products
    reactEl = set(split_elements(reactants))
    productEl = set(split_elements(products))
    return reactEl == productEl

def split_elements(expression):
    # Use a regular expression to split the string at uppercase letters, but keep the uppercase letter with the element
    elements = re.findall(r'[A-Z][a-z]*', expression)
    return elements

# Define the balancing function
def balance_equation(equation):
    """
    Balances a chemical equation written in standard notation.

    Args:
        equation (str): The chemical equation to balance, with reactants on the left and products on the right, separated by '->'.

    Returns:
        The balanced equation as a string 
    """
    # Check if the equasion is valid
    if not validate_equation(equation):
        raise ValueError("Invalid equation: all elements must be present on both sides")
    
    # Split the equation into reactants and products
    reactants, products = equation.split('->')

    # Split the reactants and products into individual compounds
    reactants = reactants.split('+')
    products = products.split('+')

    # Strip any leading or trailing whitespace from the compounds
    reactants = [r.strip() for r in reactants]
    products = [p.strip() for p in products]

    # Balance the equation
    reac, prod = balance_stoichiometry(reactants, products)

    # Create a dictionary with the coefficients for each compound
    coefficients = {**reac, **prod}
    # Create the balanced equation string
    balanced_equation = ' + '.join(f'{coefficients[r]} {r}' if coefficients[r] > 1 else r for r in reactants)
    balanced_equation += ' -> '
    balanced_equation += ' + '.join(f'{coefficients[p]} {p}' if coefficients[p] > 1 else p for p in products)
    
    return balanced_equation

# Define the function to be called when the button is clicked
def on_balance():
    """
    Callback function for the "Balance Equation" button.

    Retrieves the equation from the input field, balances it, and updates the result label.

    """
    equation = equation_entry.get()
    try:
        balanced_equation = balance_equation(equation)
        result_var.set(f"Balanced Equation: {balanced_equation}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Set up the main window
root = tk.Tk()
root.title("Chemical Equation Balancer")

# Create and place the widgets
equation_label = tk.Label(root, text="Enter Chemical Equation:")
equation_label.pack(pady=10)

equation_entry = tk.Entry(root, width=50)
equation_entry.pack(pady=10)

balance_button = tk.Button(root, text="Balance Equation", command=on_balance)
balance_button.pack(pady=10)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, justify="left", anchor="w")
result_label.pack(pady=10, padx=10)

# Run the GUI event loop
root.mainloop()
