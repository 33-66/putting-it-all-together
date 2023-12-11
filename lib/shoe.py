class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size

    def get_size(self):
        return self._size

    def set_size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

    # Property definition
    size = property(get_size, set_size)


stan_smith = Shoe("Adidas", "s")  # Passing a string "s" as size
print(
    stan_smith.size
)  # This will print 'None' because the size wasn't set to an integer
stan_smith.size = "y"  # Setting size to an integer value
print(
    stan_smith.size
)  # Now it will print the size value set previously (9 in this case)
