# mutable_default_args.py

def append_to_list(val, lst=None):
    if lst is None:
        lst = []
    lst.append(val)
    return lst

print(append_to_list(1))  # [1]
print(append_to_list(2))  # [2]
