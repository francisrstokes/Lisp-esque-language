from .evaluate_expr import evaluate_expr
from pylel.tools import get_real_dir_name
from .scope import Scope

def evaluate(ast, base_path = None):
	if not base_path:
		base_path = get_real_dir_name(__file__)
	root_scope = Scope(None, base_path)
	ast_evaluated = list( \
		map(lambda expr: evaluate_expr(root_scope, expr), ast))
	return ast_evaluated
