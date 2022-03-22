
uppercase = [char.upper() for line in line_list if line != ""
                          for char in line.strip()]
# equiv to:
for line in line_list:
    if line != "":
        for c in line.strip():
            c.upper()

#                           1. -------------------------------->
#              2. ---------> |
stripped_list = [line.strip() for line in line_list if line != ""]
# equiv to:
result = []
for line in line_list:
    if line != "":
        result.append(line.strip())

def transpose(lines):
    input_list = lines.split('\n')  # or splitlines
    input_height = len(input_list)
    input_width = max(len(x) for x in input_list)

    output_list = []

    for colnum in range(input_width):
        output = ''
        for rownum in range(input_height):
            output += get_char(input_list, rownum, colnum)
        output = output.rstrip('*').replace('*', ' ')
        output_list.append(output)

    return '\n'.join(output_list)


# def get_input_width(input_list):
#     # generator expression - doesn't use memory to store a whole list we don't need
#     return max(len(x) for x in input_list)

    # python has "comprehensions"
    #   a way to build a new collection based on some other collection(s)
    # lengths = [len(x) for x in input_list]
    # lengths = map(len, input_list)
    # return max(lengths)

    # return max(map(len, input_list))
    # return len(max(input_list, key=len))
    # max_length = 0
    # for row in input_list:
    #     if len(row) > max_length:
    #         max_length = len(row)
    # return max_length
    # max_length = 0
    # for i in range(len(input_list)):
    #     row = input_list[i]
    #     if len(row) > max_length:
    #         max_length = len(row)
    # return max_length


def get_char(input_list, rownum, colnum):
    # try:
    #     return input_list[rownum][colnum]
    # except IndexError:
    #     return '*'
    if rownum < len(input_list) and colnum < len(input_list[rownum]):
        return input_list[rownum][colnum]
    return '*'


# my_lines = ['Hello', 'World']
my_lines = ['A', 'BC']
# my_lines = []
input_str = '\n'.join(my_lines)
print(transpose(input_str))
print(repr(transpose(input_str)))
