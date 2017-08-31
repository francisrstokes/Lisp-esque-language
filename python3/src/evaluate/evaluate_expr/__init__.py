from token import Symbols, Token
from .language_core import core
from .find_base_path import find_base_path

def find_in_scope(scope, name):
	if not scope:
		return None
	if name in scope.variables:
		return scope.variables[name]
	return find_in_scope(scope.upper_scope, name)

def evaluate_expr(scope, expr):
	if type(expr) == list:
		# Evaluate empty block
		if len(expr) == 0:
			return Token(Symbols.LIST, [])

		# List of expressions?
		# Evaluate a block in series
		if type(expr[0]) == list:
			values = list( \
				map(lambda block_expr: evaluate_expr(scope, block_expr), \
					expr))
			return values[-1]
	
		# The rest of the expressions are based on identifiers
		identifier_token = expr[0]
		if identifier_token.type == Symbols.IDENTIFIER:
			# Core language functions
			if identifier_token.value in core:
				return core[identifier_token.value](evaluate_expr, scope, expr)
		
		# Try and evaluate as a single expression
		return evaluate_expr(scope, expr[0])
	else:
		# Return the value of primitives directly in their tokenised form
		if expr.is_token and \
			( \
				expr.type == Symbols.RANGE \
				or expr.type == Symbols.STRING \
				or expr.type == Symbols.NUMBER \
				or expr.type == Symbols.BOOLEAN \
				or expr.type == Symbols.FUNCTION_REFERENCE \
				or expr.type == Symbols.LIST \
			):
			return expr

		# Identifiers will be a function reference or a variable
		if expr.type == Symbols.IDENTIFIER:
			identifier_type = expr.value

			# Pass back variable value. Explicitly check null instead of other
			# falsey values that might really be contained in the variable
			variable_in_scope = find_in_scope(scope, identifier_type)
			if variable_in_scope:
				return variable_in_scope

	raise Exception("Unrecognised expression: {}".format(expr));
