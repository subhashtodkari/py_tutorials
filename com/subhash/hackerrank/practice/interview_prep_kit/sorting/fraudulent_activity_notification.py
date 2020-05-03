

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    # print(expenditure, d)
    max_expenditure = 200
    counting_arr = [0] * (max_expenditure + 1)

    c = 0
    odd = d % 2 != 0
    mid = d // 2
    median_indexes = [mid] if odd else [mid-1, mid]
    for i in expenditure[0:d]:
        counting_arr[i] += 1

    for j in range(d, len(expenditure)):

        # print("counting_arr 1 >>", counting_arr)

        # find median numbers
        median_numbers = [0] * (len(median_indexes))
        idx_sum = 0
        med_idx = 0
        for i in range(len(counting_arr)):
            idx_sum += counting_arr[i]
            while med_idx < len(median_indexes):
                if median_indexes[med_idx] < idx_sum:
                    median_numbers[med_idx] = i
                    med_idx += 1
                else:
                    break
            if med_idx >= len(median_indexes):
                break

        # print("median_numbers >> ", median_numbers)

        median = sum(median_numbers) / len(median_numbers)

        # print("median: ", median, ", expenditure[", j, "]: ", expenditure[j])

        c += 1 if expenditure[j] >= (2 * median) else 0
        # print("c: ", c)

        # update array for next day
        counting_arr[expenditure[j - d]] -= 1
        counting_arr[expenditure[j]] += 1

    return c


if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(result)

