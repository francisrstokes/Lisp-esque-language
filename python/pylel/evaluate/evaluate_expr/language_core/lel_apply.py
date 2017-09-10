from pylel.token import Symbols, Token
from .lel_call_function import lel_call_function
from .lel_lambda import lel_lambda

def _perform_function_call(evaluate_expr, scope, expr, function_descriptor):
	def func(args):
		if args.type != Symbols.LIST:
			raise Exception("Referenced arguments must be a LIST apply ({}). Got {} for expression {}"\
				.format(function_descriptor.name, args.type, expr))
		return lel_call_function(evaluate_expr, scope, args.value, function_descriptor)
	return func

def _get_function_args(evaluate_expr, scope, expr):
	def func(f_reference):
		if f_reference and f_reference.is_token and f_reference.type == Symbols.FUNCTION_REFERENCE:
			function_descriptor = f_reference.value
			if len(expr) >= 3:
				return _perform_function_call(evaluate_expr, scope, expr, function_descriptor)\
				(evaluate_expr(scope, expr[2]))
			else:
				empty_list = Token(Symbols.LIST, [])
				return _perform_function_call(evaluate_expr, scope, expr, function_descriptor)(empty_list)
		else:
			raise Exception("First argument must be a FUNCTION_REFERENCE. Got {} for expression ${}"\
				.format(expr[1].type, expr))
	return func

def lel_apply(evaluate_expr, scope, expr):
	if len(expr) >= 2:
		f_ref_is_array = type(expr[1]) == list
		f_ref_is_identifier = expr[1].is_token and expr[1].type == Symbols.IDENTIFIER
		if f_ref_is_array or f_ref_is_identifier:
			return _get_function_args(evaluate_expr, scope, expr)(evaluate_expr(scope, expr[1]))
	raise Exception("{} is not a valid function reference"\
	.format(expr[1]))

