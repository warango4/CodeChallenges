# Python code​​​​​​‌​​​‌‌​​‌​​​​‌‌​‌​‌​​‌​​‌ below
# Use print("messages...") to debug your solution.


def reshape(n, string):
    # Your code goes here
    string = string.replace(" ", "")
    new_string = []
    i = 0
    while i <= len(string) - n:
        new_string.append(string[i:i + n])
        i += n
    if i < len(string) and (i + n > len(string)):
        new_string.append(string[i: len(string)])
    result = new_string[0]
    for j in range(1, len(new_string)):
        result = result + "\n" + new_string[j]
    return result

print(reshape(3, "abc de fgh ij"))
