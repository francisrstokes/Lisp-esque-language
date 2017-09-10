import math, functools
from pylel.token import Symbols, Token

def _addition(*numbers):
	if any([number.type != Symbols.NUMBER for number in numbers]):
		raise Exception("+ only operates on NUMBER type")
	return functools.reduce(lambda acc, cur: Token(Symbols.NUMBER, acc.value + cur.value), numbers)

def _subtraction(x, y):
	if x.type != Symbols.NUMBER or y.type != Symbols.NUMBER:
		raise Exception("- only operates on NUMBER type")
	return Token(Symbols.NUMBER, x.value - y.value)

def _division(x, y):
	if x.type != Symbols.NUMBER or y.type != Symbols.NUMBER:
		raise Exception("/ only operates on NUMBER type")
	if y.value == 0:
		raise Exception("Divison by zero error")
	return Token(Symbols.NUMBER, x.value / y.value)

def _multiplication(*numbers):
	if any([number.type != Symbols.NUMBER for number in numbers]):
		raise Exception("* only operates on NUMBER type")
	return functools.reduce(lambda acc, cur: Token(Symbols.NUMBER, acc.value * cur.value), numbers)

def _power(x, y):
	if x.type != Symbols.NUMBER or y.type != Symbols.NUMBER:
		raise Exception("** only operates on NUMBER type")
	return Token(Symbols.NUMBER, pow(x.value, y.value))

def _mod(x, y):
	if x.type != Symbols.NUMBER or y.type != Symbols.NUMBER:
		raise Exception("\% only operates on NUMBER type")
	if y.value == 0:
		raise Exception("Divison by zero error")
	return Token(Symbols.NUMBER, x.value % y.value)

def _sin(x):
	if x.type != Symbols.NUMBER:
		raise Exception("sin only operates on NUMBER type")
	return Token(Symbols.NUMBER, math.sin(x.value))

lel_math = {
	"+": _addition,
	"-": _subtraction,
	"*": _multiplication,
	"/": _division,
	"**": _power,
	"%": _mod,
	"sin": _sin 
}
