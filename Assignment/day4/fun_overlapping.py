def over(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

print(over([34,33,56],[56,55,34]))