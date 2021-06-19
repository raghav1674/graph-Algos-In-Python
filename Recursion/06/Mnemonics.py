keypad_mapping = {

    '1': '1',
    '0': '0',
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'

}


def generate_mnemonics_helper(phone_number, current_index, output_mnemonic, output_arr):

    if current_index == len(phone_number):
        output_arr.append(output_mnemonic)
    else:

        for each_word in keypad_mapping[phone_number[current_index]]:

            current_index += 1
            generate_mnemonics_helper(
                phone_number, current_index, output_mnemonic + each_word, output_arr)
            current_index -= 1


def generate_mnemonics(phone_number):

    current_index = 0
    output_mnemonics = ""
    output_arr = []

    generate_mnemonics_helper(
        phone_number, current_index, output_mnemonics, output_arr)

    return output_arr


for each_mnemonic in generate_mnemonics("6005438027"): print(each_mnemonic)
