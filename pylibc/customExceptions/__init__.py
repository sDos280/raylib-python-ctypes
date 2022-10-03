"""
where are some Exception/Error that pylibc use
"""


class OverloadFunction(Exception):
    """the function was already loaded"""
    pass


class UnknownType(Exception):
    """this type is unknown"""
    pass

class NotOneReturnType(Exception):
    """not one return type"""
    pass

