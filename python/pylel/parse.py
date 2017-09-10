from pylel.token import Symbols

def _unescape_characters(str):
	return str.replace(r'\n', '\n') \
	.replace(r'\r', '\r') \
	.replace(r'\f', '\f') \
	.replace(r'\b', '\b') \
	.replace(r'\t', '\t') \
	.replace(r'\v', '\v') \
	.replace(r'\;', ';')

def _clean_string(str):
	return _unescape_characters(str[1:-1])

def _clean_bool(bool):
	return bool == "true"

def _clean_number(number):
	return float(number)

def _clean_token(token):
	if token.type == Symbols.STRING:
		token.value = _clean_string(token.value)
	elif token.type == Symbols.NUMBER:
		token.value = _clean_number(token.value)
	elif token.type == Symbols.BOOLEAN:
		token.value = _clean_bool(token.value)
	return token

class Parse(object):
	depth_pointer = 0
	
	@staticmethod
	def _add_token_to_expr_tree(ast, token):
		level = ast
		for i in range(Parse.depth_pointer):
			level = level[len(level) - 1]
		level.append(token)
	
	@staticmethod
	def _pop_expr():
		Parse.depth_pointer -= 1

	@staticmethod
	def _push_expr(ast):
		Parse._add_token_to_expr_tree(ast, [])
		Parse.depth_pointer += 1

	@staticmethod
	def parse(tokens):
		Parse.depth_pointer = 0
		clean_tokens = [_clean_token(token) for token in tokens]
		ast = []
		for token in clean_tokens:
			if token.type == Symbols.LPAREN:
				Parse._push_expr(ast)
			elif token.type == Symbols.RPAREN:
				Parse._pop_expr()
			else:
				Parse._add_token_to_expr_tree(ast, token)
		return ast
