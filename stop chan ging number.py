class ConstantNumber:
    def __init__(self, value):
        self._value = value  # Private attribute

    @property
    def value(self):
        return self._value  # Read-only access

num = ConstantNumber(100)
print(num.value)  # Output: 100

# Trying to change num.value will raise an error
# num.value = 200  # ❌ This will cause an AttributeError
