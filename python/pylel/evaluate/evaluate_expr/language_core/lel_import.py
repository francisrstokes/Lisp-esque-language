from os import path
from pylel.token import Symbols
from pylel.evaluate.scope import Scope
from pylel.evaluate.evaluate_expr.find_base_path import find_base_path
from pylel.token import tokenise
from pylel.tools import read_file, get_real_dir_name

def inject_module_to_scope(scope, module_scope, file_path):
	intersect = set(scope.variables.keys()) & set(module_scope.variables.keys())
	if len(intersect) != 0:
		raise Exception("Cannot overwrite variable in scope {} from module {}"\
			.format(intersect, file_path))
	scope.variables.update(module_scope.variables)

def lel_import(evaluate_expr, scope, expr):
	from interpreter import interpreter
	filename = evaluate_expr(scope, expr[1])
	if filename.type != Symbols.STRING:
		raise Exception("Import path must resolve to a string. Got {}"\
			.format(filename))
	file_path = path.join(find_base_path(scope), filename.value)
	base_path = get_real_dir_name(file_path)
	ast = interpreter(file_path)
	module_scope = Scope(None, base_path)
	evaluated = evaluate_expr(module_scope, ast)
	inject_module_to_scope(scope, module_scope, file_path)
	return evaluated

