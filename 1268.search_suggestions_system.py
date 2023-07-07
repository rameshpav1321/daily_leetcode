# Brute force
# class Solution:
#     def suggestedProducts(
#         self, products: List[str], searchWord: str
#     ) -> List[List[str]]:
#         my_dict = {}
#         curr_search = ""
#         for char in searchWord:
#             curr_search += char
#             temp = []
#             for product in products:
#                 if curr_search == product[: len(curr_search)]:
#                     temp.append(product)
#             temp.sort()
#             my_dict[curr_search] = temp[:3]
#         return my_dict.values()


# binary search
class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        products.sort()
        res, i, prefix = [], 0, ""
        for char in searchWord:
            print(i)
            prefix += char
            i = bisect.bisect_left(products, prefix, 0)
            res.append(
                [
                    product
                    for product in products[i : i + 3]
                    if product.startswith(prefix)
                ]
            )
        return res
