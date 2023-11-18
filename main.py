def temp_list(list):
    avg = sum(list) / len(list)
    count_more_avg = 0
    count_less_avg = 0
    for i in list:
        if i > avg:
            count_more_avg += 1
        elif i <= avg:
            count_less_avg += 1
    count_pairs = 0
    for i in range(0, len(list)):
        if i<=len(list)-2:
            if (list[i] + list[i + 1]) % 2 == 0:
                count_pairs += 1
        else:
            break
    return avg, max(list), min(list), count_more_avg, count_less_avg, count_pairs
