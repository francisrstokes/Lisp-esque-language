# -*- coding: utf-8 -*-
from __future__ import print_function
import re
import six
from pylel.tools import get_real_dir_name
from pylel.token import tokenise, Symbols
from pylel.parse import Parse
from pylel.evaluate.scope import Scope
from pylel.evaluate.evaluate_expr import evaluate_expr

LPAR = "("
RPAR = ")"
REPL_LINE = "> "

def parantheses_balance(str):
	left = len(re.findall("\(", str))
	right = len(re.findall("\)", str))
	return 0 if left == right else -1 if left > right else 1

def repl_execute(expr_str, root_scope):
	tokens = tokenise(expr_str)
	ast = Parse.parse(tokens)
	evaluate_expr(root_scope, ast[0])
	print("")

def _repl(root_scope, strikes = 0):
	expr = ""
	try:
		while True:
			line = six.moves.input()
			if len(line) == 0:
				print(REPL_LINE, end = '')
				continue
			expr += line
			balance = parantheses_balance(expr)
			if balance == 0:
				if expr[0] != LPAR:
					expr = LPAR + expr + RPAR
				strikes = 0
				repl_execute(expr, root_scope)
				expr = ""
			elif balance == -1:
				expr += " "
			else:
				print("Too many ')'!")
				expr = ""
			print(REPL_LINE, end = '')
	except KeyboardInterrupt:
		print("\n")
		if strikes == 0:
			print(REPL_LINE, end = '')
			_repl(root_scope, strikes + 1)
	except Exception as e:
		print(e)
		print(REPL_LINE, end = '')
		_repl(root_scope)

def repl():
	print("Lel REPL - Ömer Saatcioglu 2017\n(Original Node.js version by Francis Stokes)")
	print(REPL_LINE, end = '')
	root_scope = Scope(None, get_real_dir_name(__file__))
	_repl(root_scope)
