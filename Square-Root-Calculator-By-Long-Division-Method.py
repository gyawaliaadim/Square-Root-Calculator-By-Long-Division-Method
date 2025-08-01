'''
Made By: Aadim Gyawali
Inital Publish Date: 1/16/2023
'''
def pair(s):
    return [s[i:i+2] for i in range(0, len(s), 2) if i+1 < len(s)]

def calculation(num, side_num):
    num = int(num)
    for x in range(9, -1, -1):
        if (side_num + x) * x <= num:
            sq_num = x
            break
    else:
        sq_num = 0
    sub_value = num - (side_num + sq_num) * sq_num
    side_num = (side_num + 2 * sq_num) * 10
    return side_num, sub_value, sq_num

def SquareRootOf(number_str, decimal_points):
    if '.' in number_str:
        int_part, frac_part = number_str.split('.')
    else:
        int_part = number_str
        frac_part = ''
    if len(int_part) % 2 == 1:
        int_part = '0' + int_part
    if len(frac_part) % 2 == 1:
        frac_part += '0'
    int_pairs = pair(int_part)
    frac_pairs = pair(frac_part) if frac_part else []
    side_num = 0
    sub_value = 0
    final_result = ""
    for i, p in enumerate(int_pairs):
        if i == 0:
            num = p
        else:
            num = str(sub_value) + p
        side_num, sub_value, sq_num = calculation(num, side_num)
        final_result += str(sq_num)
    final_result += "."
    for i in range(decimal_points):
        if i < len(frac_pairs):
            p = frac_pairs[i]
        else:
            p = "00"
        num = str(sub_value) + p
        side_num, sub_value, sq_num = calculation(num, side_num)
        final_result += str(sq_num)
    return final_result

if __name__ == "__main__":
    while True:
        number_str = input("Enter a number: ")
        decimal_points = int(input("Enter number of decimal points: "))
        result = square_root(number_str, decimal_points)
        print(f"The square root of {number_str} is {result}")
        ask = input("Do you want to continue (y/n): ")
        if ask.lower() != 'y':
            break
'''
Use SquareRootOf(number, decimal_points) to find the square root of a number
'''

