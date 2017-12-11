def simple(num1, num2):
    pass

def simple(numPtr):
    numPtr[0] = 10

def main():
    example = [0,1,2,3,4,5]
    simple(example)
    print(example[0])

main()

