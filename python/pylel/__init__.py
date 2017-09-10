# -*- coding: utf-8 -*-
import sys

from pylel.repl import repl
from pylel.interpreter import interpreter

help_text = "LEL Language Interpreter in Python by Ömer Saatcioglu 2017\n(Original Node.js version by Francis Stokes)\nhttps://github.com/osaatcioglu/Lisp-esque-language\nUsage:\npylel [filename] [filename] ..."

def main(filename = None):
	sys.setrecursionlimit(0x100000)
	try:
		if filename:
			interpreter(filename)
		else:
			repl()
	except Exception as e:
		print(str(e))
		sys.exit(1)

def package_main():
	if len(sys.argv) == 1:
		return main()
	if "--" in sys.argv[1]:
		print(help_text)
		return
	for filename in sys.argv[1:]:
		main(filename)

if __name__ == "__main__":
	package_main()
