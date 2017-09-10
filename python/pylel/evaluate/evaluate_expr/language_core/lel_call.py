from pylel.token import Symbols
from .lel_call_function import lel_call_function
from .lel_lambda import lel_lambda

def _perform_function_call(evaluate_expr, scope, expr, function_descriptor):
	def func(args):
		return lel_call_function(evaluate_expr, scope, args, function_descriptor)
	return func

def _get_function_args(evaluate_expr, scope, expr):
	def func(f_reference):
		if f_reference and f_reference.is_token and f_reference.type == Symbols.FUNCTION_REFERENCE:
			function_descriptor = f_reference.value
			if len(expr) >= 3:
				expressions = list(\
					map(lambda sub_expr: evaluate_expr(scope, sub_expr), expr[2:]))
				return _perform_function_call(evaluate_expr, scope, expr, function_descriptor)\
				(expressions)
			else:
				return _perform_function_call(evaluate_expr, scope, expr, function_descriptor)([])
		else:
			raise Exception("First argument must be a FUNCTION_REFERENCE. Got {} for expression ${}"\
				.format(expr[1].type, expr))
	return func

def lel_call(evaluate_expr, scope, expr):
	if len(expr) >= 2:
		if type(expr[1]) == list or \
		(expr[1].is_token and expr[1].type == Symbols.IDENTIFIER):
			return _get_function_args(evaluate_expr, scope, expr)(evaluate_expr(scope, expr[1]))
	raise Exception("{} is not a valid function reference"\
		.format(expr[1]))
	

