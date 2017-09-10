
def find_base_path(scope):
	if not scope:
		return None
	if scope.upper_scope:
		return find_base_path(scope.upper_scope)
	return scope.base_path

