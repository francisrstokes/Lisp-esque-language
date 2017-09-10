from pylel.token import Symbols, Token

def _expand_ranges(values):
	found_range = any(value.type == Symbols.RANGE for value in values)
	if not found_range:
		return Token(Symbols.LIST, values)

	if len(values) != 3:
		raise Exception("List with range operator requires exactly 3 arguments")
	prev = values[0]
	next_ = values[2]
	if prev.type != Symbols.NUMBER or next_.type != Symbols.NUMBER:
		raise Exception("Cannot make range from non-number")

	range_direction = prev.value < next_.value
	start = prev.value if range_direction else next_.value
	end = next_.value if range_direction else prev.value
	expanded_range = []

	for j in range(int(start), int(end) + 1):
		expanded_range.append(Token(Symbols.NUMBER, j))
	if not range_direction:
		expanded_range = expanded_range[::-1]
	return Token(Symbols.LIST, expanded_range)

def lel_list(evaluate_expr, scope, expr):
	expressions = list(\
		map(lambda sub_expr: evaluate_expr(scope, sub_expr), expr[1:]))
	return _expand_ranges(expressions)
