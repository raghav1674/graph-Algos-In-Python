

def max_ways_to_reach_staircase_end(staircase_height, max_step, current_step=1):

    if staircase_height == 0 or current_step == 0:
        return 1
    elif staircase_height >= current_step:
        return max_ways_to_reach_staircase_end(
            staircase_height-current_step, max_step, current_step-1) + staircase_height//current_step


print(max_ways_to_reach_staircase_end(10, 2))
