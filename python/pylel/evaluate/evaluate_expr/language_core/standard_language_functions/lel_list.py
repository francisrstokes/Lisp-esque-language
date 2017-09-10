from pylel.token import Symbols, Token

EMPTY_LIST = Token(Symbols.LIST, [])

def _join(l):
	if l.type != Symbols.LIST:
		raise Exception("Can't join non-lists. Got {}".format(l.type))
	return Token(Symbols.STRING, "".join(list(map(\
		lambda list_item: list_item.value, l.value))))

def _length(l):
	if l.type != Symbols.LIST:
		raise Exception("length operates on LIST type. Got {}".format(l.type))
	return Token(Symbols.NUMBER, len(l.value))

def _head(l):
	if l.type != Symbols.LIST:
		raise Exception("head operates on LIST type. Got {}".format(l.type))
	return l.value[0] if len(l.value) != 0 else EMPTY_LIST

def _tail(l):
	if l.type != Symbols.LIST:
		raise Exception("tail operates on LIST type. Got {}".format(l.type))
	return Token(Symbols.LIST, l.value[1:])

def _nth(l, n):
	if l.type != Symbols.LIST:
		raise Exception("nth operates on LIST type. Got {}".format(l.type))
	nth = int(n.value)
	if nth >= 0 and nth < len(l.value):
		return l.value[nth]
	raise Exception("nth: bad index {}. Given list has {} elements"\
		.format(n.value, len(l.value)))

def _sublist(l, start, end):
	if l.type != Symbols.LIST:
		raise Exception("sublist operates on LIST type. Got {}".format(l.type))
	list_length = len(l.value)
	s = int(start.value)
	e = int(end.value)

	if s > e:
		raise Exception("start index cannot be greater than the end index for a sublist")
	if s < 0 or e >= list_length:
		raise Exception("sublist indexes out of range. Got start ({}) end ({}) for list of length {}"\
			.format(s, e, list_length))
	return Token(Symbols.LIST, l.value[s:e + 1])

lel_list = {
	"join": _join,
	"length": _length,
	"head": _head,
	"tail": _tail,
	"nth": _nth,
	"sublist": _sublist
}
