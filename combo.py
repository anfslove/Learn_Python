# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]
# If you use .append(), you'll want to pass it a tuple of new values.
list1 = list("123")
list2 = list("abc")
def combo(list1, list2):
    list3 = []
    for index, it in enumerate(list1):
        print(it)
        print(list2[index])
        list3.append((it, list2[index]))
    print(list3)

combo(list1, list2)