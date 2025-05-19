# Modifying list while iterating using list comprehension - pitfall
lst = [1, 2, 3]
res = [lst.append(x*10) for x in lst]  # Avoid side effects in comprehensions

print(lst)  # lst modified during iteration

# Best practice: use comprehensions only for creating new lists, no side effects
new_lst = [x*10 for x in [1,2,3]]
print(new_lst)
