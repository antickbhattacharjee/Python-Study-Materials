def mean(data):
    return sum(data)/len(data)
def median(data):
    data = sorted(data)
    n = len(data)
    mid = n//2
    if n%2==0:
        return (data[mid-1]+data[mid])/2
    else:
        return data[mid]
def maximum(data):
    res=max(data)
    return res

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print(f'Mean: {mean(data)}')
    print(f'Median: {median(data)}')
    print(f'Maximum: {maximum(data)}')