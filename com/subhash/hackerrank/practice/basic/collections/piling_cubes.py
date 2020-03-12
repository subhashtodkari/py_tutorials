if __name__ == "__main__":
    tc = int(input())
    for t in range(tc):
        n = int(input())
        arr = list(map(int, input().split()))
        # print(arr)
        possible = "Yes"
        slope = None
        prev = arr[0]
        for num in arr[1:]:
            if num > prev:
                slope = 1
            elif num < prev:
                if slope is None:
                    slope = -1
                elif slope == 1:
                    possible = "No"
                    break
            prev = num

        print(possible)
