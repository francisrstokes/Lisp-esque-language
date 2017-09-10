from .lel_if import lel_if
from .lel_let import lel_let
from .lel_lambda import lel_lambda
from .lel_list import lel_list
from .lel_map import lel_map
from .lel_filter import lel_filter
from .lel_call import lel_call
from .lel_apply import lel_apply
from .lel_mutate import lel_mutate
from .lel_import import lel_import
from .lel_function import lel_function

core = {
	"if": lel_if,
	"let": lel_let,
    "function": lel_function,
    "lambda": lel_lambda,
    "list": lel_list,
    "map": lel_map,
    "filter": lel_filter,
    "call": lel_call,
    "apply": lel_apply,
    "mutate": lel_mutate,
    "import": lel_import
}
