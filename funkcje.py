def greet_name(name):
    print(f"Hello {name}")
greet_name("Alex")



def word_len(word):
    return len(word)
print(word_len("Python123"))




def validate_ip(ipnet):
    param = ipnet.split('.')
    if len(param) != 4:
        return False
    for part in param:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True


print(validate_ip('192.160.5.1'))





def max_min(num1, num2, num3):
    max_num = max(num1, num2, num3)
    min_num = min(num1, num2, num3)
    return min_num, max_num 

print(max_min(50, 20, 30))
