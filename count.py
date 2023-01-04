from collections import Counter
import operator

array = [1, 2, 3, 3, 3, 4]   
sort_array = Counter(array)
sort_array1 = dict(sorted(sort_array.items() , key=operator.itemgetter(1)))
print(sort_array1)
array_cnt =[]
array_key = []
answer = ()
max_cmt =0
max_key = 0
for key,value in sort_array1.items():
    if(value == max(sort_array1.values())):
        max_cmt = max_cmt+1
        max_key = key

if(max_cmt > 1):
    answer = -1
else:
    answer = max_key;

print(answer)

array = {}

array[1] = 10
array['b'] = 20

print(array)          #{1: 10, 'b': 20}
print(array.keys())   #dict_keys([1, 'b'])
print(array.values()) #dict_values([10, 20])
print(array.items()) #dict_items([(1, 10), ('b', 20)])
print(array[1])     #10
print(array.get(2)) #None
print(array.get(1)) #10


#from collections import Counter
#
#def solution(array):
#    
#    sort_array = Counter(array)
#    array_cnt =[]
#    answer = 0
#    for key,value in sort_array.items():
#        array_cnt.append(value)
#    array_cnt.sort()
#    if(len(array_cnt) > 1):
#        if(array_cnt[len(array_cnt)-1] == array_cnt[len(array_cnt)-2]):
#            answer = -1
#        else:
#            answer = array_cnt[len(array_cnt)-1]
#    else:
#        answer = array_cnt[len(array_cnt)-1]
    
#    return answer


# print(sort_array1.get(4))
# print(max(sort_array1.values()))
# print(max(sort_array1).keys())
# if(len(sort_array1) > 1):
#     if(sort_array1[len(sort_array1)] == sort_array1[len(sort_array1)-1]):
#         answer = -1
#     else:
#         answer = sort_array1[len(sort_array1)]
# else:
#    answer = sort_array1[len(sort_array1)].keys()