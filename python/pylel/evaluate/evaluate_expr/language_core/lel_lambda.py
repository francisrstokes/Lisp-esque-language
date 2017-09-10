from pylel.token import Symbols, Token
from pylel.evaluate.scope import Scope
from .lel_function import ScopedFunction

def _create_expected_arguments(token):
	if token.type != Symbols.IDENTIFIER:
		raise Exception()
	return token.value

def lel_lambda(evaluate_expr, scope, expr):
	f_name = "lambda_function"
	try:
		expected_arguments = list(map(_create_expected_arguments, expr[1]))
	except:
		raise Exception("Function declaration arguments must be an IDENTIFIER. Got {} for function {}"\
			.format(token.type, f_name))
	f_body = expr[2:]
	if len(f_body) == 0:
		raise Exception("Function body must contain at least one statement. Got none for function {}"\
			.format(f_name))
	function_scope = Scope(scope)
	return Token(Symbols.FUNCTION_REFERENCE, \
		ScopedFunction(f_name, f_body, expected_arguments, function_scope))
