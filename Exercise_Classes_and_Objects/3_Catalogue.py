class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [product for product in self.products if product.startswith(first_letter)]
        # get_by_letter_list = []
        # for _ in range(len(self.products)):
        #     list = [str(el) for el in str(self.products[_])]
        #     if list[0] == first_letter:
        #         get_by_letter_list.append(self.products[_])
        # return get_by_letter_list

    def __repr__(self):
        print_list = '\n'.join(sorted(self.products))
        return f"Items in the {self.name} catalogue:\n{print_list}"

# catalogue = Catalogue("Furniture")
# catalogue.add_product("Sofa")
# catalogue.add_product("Mirror")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# print(catalogue.get_by_letter("C"))
# print(catalogue)

