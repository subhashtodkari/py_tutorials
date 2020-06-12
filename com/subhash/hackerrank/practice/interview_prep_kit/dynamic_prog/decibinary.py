import math


def decibinary_to_decimal(db):
    pos = 0
    val = db
    decimal = 0
    while val > 0:
        decimal += (val % 10) * (1 << pos)
        pos += 1
        val = val // 10
    return decimal


max_decibinary_value_cache = dict()


def get_max_decibinary_value(num_of_digits: int):
    if num_of_digits in max_decibinary_value_cache:
        return max_decibinary_value_cache[num_of_digits]

    if num_of_digits < 1:
        raise Exception("number of digits cannot be less than 1: passed value: " + str(num_of_digits))

    max_val = 0
    while num_of_digits > 0:
        max_val += ((1 << (num_of_digits-1)) * 9)
        num_of_digits -= 1

    max_decibinary_value_cache[num_of_digits] = max_val
    return max_val


decimal_to_decibinary_cache = dict()

base_10_map = dict()

for i in range(20):
    base_10_map[i] = int(math.pow(10, i))


def decimal_to_decibinaries(decimal: int, num_of_digits: int):

    if (decimal, num_of_digits) in decimal_to_decibinary_cache:
        # print("cache used for : ", (decimal, num_of_digits))
        return decimal_to_decibinary_cache[(decimal, num_of_digits)]

    # range check
    min_val = 1 << (num_of_digits - 1)
    max_val = get_max_decibinary_value(num_of_digits)

    if decimal > max_val:
        return None

    if decimal < 2 or (decimal < 10 and num_of_digits == 1):
        if (decimal, num_of_digits) not in decimal_to_decibinary_cache:
            decimal_to_decibinary_cache[(decimal, num_of_digits)] = [decimal]
        return decimal_to_decibinary_cache[(decimal, num_of_digits)]

    decibinaries = []

    val = decimal
    base_2 = min_val
    table_idx = 1
    while table_idx < 10 and table_idx * base_2 <= val:
        decibinary = table_idx * base_10_map[num_of_digits - 1]
        remainder = val - (table_idx * base_2)
        remainder_decibinary = decimal_to_decibinaries(remainder, num_of_digits - 1)
        if remainder_decibinary:
            dbs = [(decibinary + x) for x in remainder_decibinary]
            decibinaries.extend(dbs)
        table_idx += 1

    if num_of_digits > 1:
        lower_bit_combinations = decimal_to_decibinaries(decimal, num_of_digits-1)

        if lower_bit_combinations:
            decibinaries[0:0] = lower_bit_combinations

    decimal_to_decibinary_cache[(decimal, num_of_digits)] = decibinaries

    return decibinaries


def num_bit_len(num: int):
    if num == 0:
        return 1
    length = 0
    while num:
        num >>= 1
        length += 1
    return length


if __name__ == "__main__":

    num_of_queries = int(input())
    # print(num_of_queries)
    queries = []
    max_num = int(input())-1
    min_num = max_num
    queries.append(max_num)
    for _ in range(num_of_queries-1):
        num = int(input())-1
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
        queries.append(num)
    # print(queries)

    # sort them
    sorted_queries = queries.copy()
    sorted_queries.sort()

    results = dict()

    prev_count = 0
    count = 0
    num = 0
    arr_idx = 0
    while count <= max_num:
        # odd numbers have same count of decibinary numbers as of previous even number
        if 1 & num == 0 or sorted_queries[arr_idx] < (count + prev_count):
            decimal_to_decibinary_cache = dict()
            nums = decimal_to_decibinaries(num, num_bit_len(num))
            prev_count = len(nums)
            while arr_idx < num_of_queries and sorted_queries[arr_idx] < count + prev_count:
                results[sorted_queries[arr_idx]] = nums[sorted_queries[arr_idx] - count]
                arr_idx += 1
            # print(num, " : ",  len(nums))
        count += prev_count
        num += 1
    # print(results)

    for q in queries:
        # print(q, " ==> arr[", q-min_num, "]: ")
        print(results[q])

