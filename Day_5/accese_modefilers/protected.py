class protected:
    def __init__(self):
        self._protected_variable="protected variable"
    def _show(self):
        print("protected method")
obj=protected()
print(obj._protected_variable)
print(obj._show())