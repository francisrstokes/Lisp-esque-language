from pylel.token import Symbols

def lel_let(evaluate_expr, scope, expr):
	if expr[1].type != Symbols.IDENTIFIER:
		raise Exception("Variable name must be an IDENTIFER. Got {} for {}"\
			.format(expr[1].type, expr[1].value))
	name = expr[1].value
	if name in scope.variables:
		raise Exception("Can't implicitly mutate previously assigned scoped variable '{}'"\
			.format(name))
	value = evaluate_expr(scope, expr[2])
	scope.variables[name] = value
	return value
