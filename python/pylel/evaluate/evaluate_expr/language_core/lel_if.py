
def lel_if(evaluate_expr, scope, expr):
	if len(expr) < 4:
		raise Exception("Conditional expressions require 3 arguments. Got {} at expression {}"\
			.format(len(expr), expr))

	conditional_result = evaluate_expr(scope, expr[1])
	branch = expr[2] if conditional_result.value else expr[3]
	return evaluate_expr(scope, branch)

