f = open("/Users/indrani.sarkar/Desktop/PYTHON/Functional/some.txt", "r")

list_ = f.read().replace('\n', ' ').split(' ')
# print(list_)


dict_ = {}

for i in list_:
    if i != ' ':
        if i not in dict_.keys():
            dict_[i] = 1
        else:
            dict_[i] += 1
# print(dict_)


max_ = max(dict_.values())
# print(max_)

# for k,v in dict_.items():
#     print(k, " and ", v)

filtered_dict = {k:v for k,v in dict_.items() if k != '' or v == max(dict_.values())}
print(filtered_dict)
