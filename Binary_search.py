list1=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

n=len(list1)
m=n/2
m=round(m)
first=0
last=n
mid=m
print(first, last, mid)

user_input=int(input("Enter the number position you want to search(0-100): "))
count=0
while first<=last:#and last>100:# and list1[mid]!=user_input:
    m=n/2
    count=count+1
    print(count)
    if user_input==list1[mid]:
        print("matched at position: ", mid)
        break
    elif user_input<list1[mid]:
        last=mid
        mid=round(int((first+last)/2))
        print("sec1_executed",mid)
    elif user_input>list1[mid]:
        first=mid
        mid=round(int((first+last)/2))
        print("sec2_executed",mid)
    else: print("something gone wrong")