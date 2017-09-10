from pylel.token import Symbols, Token
from pylel.evaluate.scope import Scope

class ScopedFunction(object):
	def __init__(self, name, body_expressions = [], expected_arguments = [], scope = {}):		
		self.name = name
		self.is_function = True
		self.body_expressions = body_expressions
		self.expected_arguments = expected_arguments
		self.scope = scope

	def __repr__(self):
		return str(self.__dict__) + "\n" 

	def __str__(self):
		return self.__repr__()

def _create_expected_args(token):
	if token.type != Symbols.IDENTIFIER:
		raise Exception()
	return token.value

def lel_function(evaluate_expr, scope, expr):
	if expr[1].type != Symbols.IDENTIFIER:
		raise Exception("Function name must be an IDENTIFIER. Got {} for {}"\
			.format(expr[1].type, expr[1].value))

	f_name = expr[1].value
	try:
		expected_arguments = list( \
			map(lambda token: _create_expected_args(token), \
				expr[2]
				))
	except:
		raise Exception("Function declaration arguments must be an IDENTIFIER. Got {} for function {}"\
			.format(token.type, f_name))

	f_body = expr[3:]
	if len(f_body) < 1:
		raise Exception("Function body must contain at least one statement. Got none for function {}"\
			.format(f_name))
	
	function_scope = Scope(scope)
	scope.variables[f_name] = Token( \
		Symbols.FUNCTION_REFERENCE, \
		ScopedFunction(f_name, f_body, expected_arguments, function_scope)
		)
	return scope.variables[f_name]
