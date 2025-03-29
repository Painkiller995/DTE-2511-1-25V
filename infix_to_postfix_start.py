''' Regler for Shunting Yard-algoritmen:
1. **Operander** (tall og variabler) legges direkte til output_stack.
2. **Operatorer** legges på en operand stack, men før en operator legges på stakken,
   fjernes operatorer fra output_stack hvis de har høyere eller lik presedens.
3. **Venstreparenteser** legges på operator stack.
4. **Høyreparenteser** fjerner operatorer fra stakken til output_stack til en venstreparentes finnes.
'''


# Funksjonen tar et infiksuttrykk som input og returnerer et postfix-uttrykk.
# Eksempel: (6-9)*(3+4)^2 => 6 9 - 3 4 + 2 ^ *
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operator_stack = []
    output_stack = []
    
    for char in expression:
        if char.isnumeric():
            output_stack.append(char)  # Bruker append for liste

        elif char == ' ':
            continue  # Ignorer mellomrom
        elif char == '(':
            operator_stack.append(char)
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_stack.append(operator_stack.pop())  # Bruker append for liste

            operator_stack.pop()  # Remove '(' from operator_stack
        else:
            while operator_stack and operator_stack[-1] != '(' and precedence[char] <= precedence[operator_stack[-1]]:
                output_stack.append(operator_stack.pop())  # Bruker append for liste

            operator_stack.append(char)

    while operator_stack:
        output_stack.append(operator_stack.pop())  # Bruker append for liste

    return ' '.join(output_stack)  # Konverterer liste til string

def eval_postfix(expression):
    #din kode
    return 42

# Eksempel på bruk
expressions = ["(1 + 2) * 3", " 2 * 3 - 4 + 8 * 2","(6-9)*(3+4)^2"]
for expression in expressions:
    postfix_expression = infix_to_postfix(expression)
    result = eval_postfix(postfix_expression)
    print("infix-uttrykk :", expression , " blir postfix-uttrykk:", postfix_expression, " og resultatet er:", result)
  