# Python does not have switch-case, use dictionary mapping instead

def switch_case(option):
    switcher = {
        1: "Option 1 selected",
        2: "Option 2 selected",
        3: "Option 3 selected",
    }
    return switcher.get(option, "Invalid option")

print(switch_case(2))  # Output: Option 2 selected
