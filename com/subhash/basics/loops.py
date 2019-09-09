

# various loop statements

# range(static list of integers created in advance) vs xrange (dynamic int generator - low memory requirement,
# good for range of billions)
# xrange() - deprecated in python 3

# for


def test_for_loop(arr):
    print("print array using for loop: i as an object")
    for i in arr:
        print(i)

    print("print array using for loop: i as an index in range object")
    for i in range(len(arr)):
        if i == 2:
            print("skipping for index 2")
            continue
        print(arr[i])

    # xrange not supported at all :O
    # for i in xrange(len(arr)):
        # print(arr[i])

# while


def test_while_loop(arr):
    print("print array using while loop")
    i = 0;
    while i < len(arr):
        print(i, " : ", arr[i])
        i += 1
        if i == 4:
            print ("breaking while loop here")
            break

# with


if __name__ == "__main__":
    array = ["hi", "there", "how", "are", "you", "?"]
    test_for_loop(array)
    test_while_loop(array)
