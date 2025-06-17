"""The goal in this module is to define functions that take a formula as input and
do some computation on its syntactic structure."""


from formula import *


def length(formula):
    """Determines the length of a formula in propositional logic."""
    if isinstance(formula, Atom):
        return 1
    if isinstance(formula, Not):
        return 1 + length(formula.inner)
    if isinstance(formula, (And, Or, Implies)):
        return 1 + length(formula.left) + length(formula.right)
    return 0


def subformulas(formula):
    """Returns the set of all subformulas of a formula.

    For example, observe the piece of code below.

    my_formula = Implies(Atom('p'), Or(Atom('p'), Atom('s')))
    for subformula in subformulas(my_formula):
        print(subformula)

    This piece of code prints p, s, (p v s), (p → (p v s))
    (Note that there is no repetition of p)
    """

    if isinstance(formula, Atom):
        return {formula}
    if isinstance(formula, Not):
        return {formula}.union(subformulas(formula.inner))
    if isinstance(formula, (And, Or, Implies)):
        return {formula}.union(subformulas(formula.left), subformulas(formula.right))

#  we have shown in class that, for all formula A, len(subformulas(A)) <= length(A).


def atoms(formula):
    """Returns the set of all atoms occurring in a formula.

    For example, observe the piece of code below.

    my_formula = Implies(Atom('p'), Or(Atom('p'), Atom('s')))
    for atom in atoms(my_formula):
        print(atom)

    This piece of code above prints: p, s
    (Note that there is no repetition of p)
    """
    if isinstance(formula, Atom):
        return {formula}
    if isinstance(formula, Not):
        return atoms(formula.inner)
    if isinstance(formula, (And, Or, Implies)):
        return atoms(formula.left).union(atoms(formula.right))


def number_of_atoms(formula):
    """Returns the number of atoms occurring in a formula.
    For instance,
    number_of_atoms(Implies(Atom('q'), And(Atom('p'), Atom('q'))))

    must return 3 (Observe that this function counts the repetitions of atoms)
    """
    if isinstance(formula, Atom):
        return 1
    if isinstance(formula, Not):
        return number_of_atoms(formula.inner)
    if isinstance(formula, (And, Or, Implies)):
        return number_of_atoms(formula.left) + number_of_atoms(formula.right)


def number_of_connectives(formula):
    """Returns the number of connectives occurring in a formula."""
    if isinstance(formula, Atom):
        return 0
    if isinstance(formula, Not):
        return 1 + number_of_connectives(formula.inner)
    if isinstance(formula, (And, Or, Implies)):
        return 1 + number_of_connectives(formula.left) + number_of_connectives(formula.right)


def is_literal(formula):
    """Returns True if formula is a literal. It returns False, otherwise"""
    if isinstance(formula, Atom):
        return True
    if isinstance(formula, Not) and isinstance(formula.inner, Atom):
        return True
    return False


def substitution(formula, old_subformula, new_subformula):
    """Returns a new formula obtained by replacing all occurrences
    of old_subformula in the input formula by new_subformula."""
    if formula.__eq__(old_subformula):
        return new_subformula
    if isinstance(formula, Atom):
        return formula
    if isinstance(formula, Not):
        return substitution(formula.inner, old_subformula, new_subformula)
    if isinstance(formula, (And, Or, Implies)):
        left = substitution(formula.left, old_subformula, new_subformula)
        right = substitution(formula.right, old_subformula, new_subformula)
        if isinstance(formula, And):
            return And(left, right)
        if isinstance(formula, Or):
            return Or(left, right)
        if isinstance(formula, Implies):
            return Implies(left, right)
    return None


def is_clause(formula):
    """Returns True if formula is a clause. It returns False, otherwise"""
    if isinstance(formula, Or):
        if isinstance(formula.left, Or) and isinstance(formula.right, Or):
            return is_clause(formula.left) and is_clause(formula.right)
        if isinstance(formula.left, Or) and not isinstance(formula.right, Or):
            return is_clause(formula.left) and is_literal(formula.right)
        if not isinstance(formula.left, Or) and isinstance(formula.right, Or):
            return is_literal(formula.left) and is_clause(formula.right)
        return is_literal(formula.left) and is_literal(formula.right)
    return False


def is_negation_normal_form(formula):
    """Returns True if formula is in negation normal form.
    Returns False, otherwise."""
    if isinstance(formula, Not) and isinstance(formula.inner, Atom):
        return True
    if isinstance(formula, (And, Or)):
        return is_negation_normal_form(formula.left) or is_negation_normal_form(formula.right)
    return False


def is_cnf(formula):
    """Returns True if formula is in conjunctive normal form.
    Returns False, otherwise."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_term(formula):
    """Returns True if formula is a term. It returns False, otherwise"""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_dnf(formula):
    """Returns True if formula is in disjunctive normal form.
    Returns False, otherwise."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_decomposable_negation_normal_form(formula):
    """Returns True if formula is in decomposable negation normal form.
    Returns False, otherwise."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========
