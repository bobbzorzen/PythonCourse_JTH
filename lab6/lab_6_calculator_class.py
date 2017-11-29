"""
    Basic calculator module
"""
class Calculator(object):
    """
        Calculator class with basic functionality
    """
    def __init__(self, start_value=0):
        self._memory_value = start_value
        self._memory_values = [self._memory_value]

    def get_memory_value(self):
        """
            Return current memory value
        """
        return self._memory_value

    def add(self, value):
        """
            Adds given value to current memory value
        """
        self._memory_value += value
        self._memory_values.append(self._memory_value)
