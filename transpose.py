def transpose(lines):
    input_list = lines.split('\n')  # or splitlines
    input_height = len(input_list)
    input_width = get_input_width(input_list)

    output_list = []

    for colnum in range(input_width):
        output = ''
        for rownum in range(input_height):
            output += get_char(input_list, rownum, colnum)
        output = output.rstrip('*').replace('*', ' ')
        output_list.append(output)

    return '\n'.join(output_list)


my_lines = ['Hello', 'World']
input_str = '\n'.join(my_lines)
print(transpose(input_str))
print(repr(transpose(input_str)))
