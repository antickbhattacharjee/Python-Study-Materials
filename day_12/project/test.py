# python program to input list

def input_list():
    lst = []
    n = int(input("Enter number of elements in the list: "))
    for i in range(n):
        element = input(f"Enter element {i+1}: ")
        lst.append(element)
    return lst
if __name__ == "__main__":
    my_list = input_list()
    print("The input list is:", my_list)