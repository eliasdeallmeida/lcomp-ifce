from functions import *


formula1 = Implies(Not(Atom('P')), Or(Atom('Q'), Atom('R')))
formula2 = Not(Implies(Atom('p'), Atom('q')))
formula3 = And(Not(Atom('p')), Atom('q'))

print(formula1)
print(length(formula1))
print(subformulas(formula1))
print(atoms(formula1))
print(number_of_atoms(formula1))
print(number_of_connectives(formula1))
print(is_literal(formula1))
# print(substitution(formula1, Atom('p'), Or(Atom('b'), Not(Atom('a')))))
print(formula3)
print(is_clause(formula3))
print(is_negation_normal_form(formula3))
