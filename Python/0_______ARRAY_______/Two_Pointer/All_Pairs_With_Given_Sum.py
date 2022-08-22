
# Python3 program for the
# above approach
def pairedElements(arr, sum):
   
    low = 0;
    high = len(arr) - 1;
 
    while (low < high):
        if (arr[low] + arr[high] == sum):
            print("The pair is : (", arr[low],", ", arr[high], ")");
        if (arr[low] + arr[high] > sum):
            high -= 1;
        else:
            low += 1;
 
# Driver code
if __name__ == '__main__':
   
    arr = [2, 3, 4, -2,
           6, 8, 9, 11];
    arr.sort();
    pairedElements(arr, 6);