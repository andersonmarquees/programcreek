"""Two Sum"""


# def two_sum(vet, target):
#     """
#     Give an array of integers, return indices of two numbers
#     such that they add up to a specific target
#     :param vet: array --> intergers
#     :param key: target --> key
#     :return: sum of two numbers
#     """
#     # cria dict para armazenar os valores
#     dic = {}
#     # percorre a lista formecida
#     for i in range(len(vet)):
#         if vet[i] not in dic:
#             dic[target - vet[i]] = i
#         else:
#             return [dic[vet[i]], i]
#
#
# h = [87, 99, 14, 3, 2, 7, 11, 15]
# print(two_sum(h, 9))

# vet = [7, 8, 6, 5]
# # dic = dict((k, i) for i, k in vet)
# # print(dic)
# d = {key: value for (key, value) in enumerate(vet)}
# #d = {(key, value) for (key, value) in zip(key_list, value_list)}
# print(d)

class Solution:

    def two_sum(self, vet, target):
        """
        Give an array of integers, return indices of two numbers
        such that they add up to a specific target
        :param vet: array --> intergers
        :param target: target --> key
        :return: sum of two numbers
        """
    # dic = {}
    # for i in range(len(vet)):
    #     if vet[i] not in dic:
    #         dic[target - vet[i]] = i
    #     else:
    #         return [dic[vet[i]], i]

        dic = {}  # dict vazio
        # percorrendo a list
        for i in range(len(vet)):
            # Se o valor não estiver no dict, faz a subtração da key e guardamos o valor como key e a posição como
            # valor.
            if vet[i] not in dic:
                dic[target - vet[i]] = i
            else:
                # Qdo estivermos olhando para os valores da list e esse valor coincidir com alguma key já guardade no
                # dict, saberemos que a soma das keys será igual ao target e asim retornamos os indices
                return [dic[vet[i]], i]


h = [87, 99, 14, 3, 2, 7, 11, 15]
f = Solution()
print(f.two_sum(h, 9))
