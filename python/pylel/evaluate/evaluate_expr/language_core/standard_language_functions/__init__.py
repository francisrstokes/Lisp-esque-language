from .lel_boolean import lel_boolean
from .lel_general import lel_general
from .lel_list import lel_list
from .lel_math import lel_math
from .lel_string import lel_string

standard = lel_general.copy()
standard.update(lel_boolean)
standard.update(lel_math)
standard.update(lel_list)
standard.update(lel_string)
