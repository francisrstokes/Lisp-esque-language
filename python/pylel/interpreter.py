from pylel.token import tokenise, Symbols
from pylel.tools import read_file, get_real_dir_name
from pylel.parse import Parse
from pylel.evaluate import evaluate

def validate(tokens):
	left = 0
	right = 0
	for token in tokens:
		if token.type == Symbols.LPAREN: left += 1 
		if token.type == Symbols.RPAREN: right += 1 
		if right > left:
			return False
	return left == right

def interpreter(file_name):
	data = read_file(file_name)
	tokens = tokenise(data)
	if not validate(tokens):
		raise Exception('Unmatched parentheses.')
	ast = Parse.parse(tokens)
	base_path = get_real_dir_name(file_name)
	return evaluate(ast, base_path)
