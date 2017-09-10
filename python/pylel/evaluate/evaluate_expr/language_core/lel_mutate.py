from pylel.token import Symbols

def lel_mutate(evaluate_expr, scope, expr):
  if expr[1].type != Symbols.IDENTIFIER:
    raise Exception("Variable name must be an IDENTIFER. Got {} for {}"\
      .format(expr[1].type, expr[1].value))
  name = expr[1].value
  if not name in scope.variables:
    raise Exception("No variable '{}' to mutate in the local scope"\
      .format(name))
  value = evaluate_expr(scope, expr[2])
  scope.variables[name] = value
  return value
