# O(n*n!)
def permutation_helper(input_str, count, output, out, level):

    if level == len(input_str):
        output.append(out)
    else:
        for i in range(len(input_str)):
            if count[i] == 1:
                count[i] = 0
                level += 1
                permutation_helper(input_str, count, output,
                                   out+input_str[i], level)
                count[i] = 1
                level -= 1


def permutation(string):

    count = [1]*len(string)
    output_arr = []
    output_string = ""
    level = 0
    permutation_helper(string, count, output_arr, output_string, level)

    return output_arr


print(permutation("ABC"))
