# import re
#
# patterns = r"^@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+$"
#
# regex = re.compile(patterns)
# digit_regex = re.compile(r"\d")
# n = int(input())
#
# for _ in range(n):
#     row_data = input()
#
#     if regex.match(row_data):
#         digits = digit_regex.findall(row_data)
#         if digits:
#             product_group = "".join(digits)
#         else:
#             product_group = "00"
#
#         print(f"Product group: {product_group}")
#     else:
#         print("Invalid barcode")

import re

def parse_barcode(barcode_data):
    pattern = r"^@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+$"

    for barcode in barcode_data:
        if re.fullmatch(pattern, barcode):
            product_group = re.findall(r'\d', barcode)
            product_group = ''.join(product_group) if product_group else '00'
            print(f"Product group: {product_group}")
        else:
            print("Invalid barcode")
            

n = int(input())
data = [input() for _ in range(n)]
parse_barcode(data)