import itertools

if __name__ == "__main__":
    options = ["BufferData", "Timeout", "Delay"]
    testcases = list(itertools.product(
        [True, False, None], repeat=len(options)*2))
    for i in testcases:
        print(i)
    print(len(testcases))
    print(3 ** (len(options)*2))
