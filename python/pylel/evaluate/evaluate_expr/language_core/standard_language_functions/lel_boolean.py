from pylel.token import Symbols, Token

lel_boolean = {
	'=': lambda x, y: Token(Symbols.BOOLEAN, x.value == y.value ),
	'<': lambda x, y: Token(Symbols.BOOLEAN, x.value < y.value ),
	'>': lambda x, y: Token(Symbols.BOOLEAN, x.value > y.value ),
	'<=': lambda x, y: Token(Symbols.BOOLEAN, x.value <= y.value ),
	'>=': lambda x, y: Token(Symbols.BOOLEAN, x.value >= y.value ),
}
