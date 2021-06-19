def powerset_helper(string, output_string, output_arr, current_index):

	if current_index == len(string):
		output_arr.append(output_string)
	else:
		powerset_helper(string,output_string+string[current_index],output_arr,current_index+1)
		powerset_helper(string,output_string,output_arr,current_index+1)
	
	

def powerset(string):

    output_arr = []
    output_string = ""
    current_index = 0
    powerset_helper(string, output_string, output_arr, current_index)

    return output_arr


print(powerset("ABC"))