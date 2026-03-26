#Freqency calculation using dictionary
def count_frequency(x):
    f={}
    for i in x:
        if i in f:
            f[i]+=1
        else:
            f[i]=1
    return f

#duplicate finding using the dictionary(reused)
def finding_duplicates(f):
    duplicates=[]
    for i in f:
        if f[i] > 1:
            duplicates.append(i)
    return duplicates

#high frequent element in list using dictionary
def most_frequent(f):
    max_count=0
    high_frequent_element=0
    for i in f:
        if f[i] > max_count:
            max_count=f[i]
            high_frequent_element=i
    return high_frequent_element

#low frequent element in list using dictionary
def least_frequent(f):
    least_count=999999   
    low_frequent_element=0
    for i in f:
        if f[i] < least_count:
            least_count=f[i]
            low_frequent_element=i
    return low_frequent_element

#calculating common elements from 2 lists
def common_elements(y,z):
    common=[]
    for i in y:
        if i in z:
            common.append(i)
    return common

#control module
#MENU
def main():
    print("print your input seperated by space...")
    x=list(map(int,input("Enter the numbers: ").split()))  
  

    while True:
        print("#MENU")
        print("--------------------------------")
        print("1.Frequency of Elements")
        print("2.Find Duplicates")
        print("3.Find Highly Frequent")
        print("4.Find Low Frequent")
        print("5.Common Elements in Lists")
        print("6.Exit..")
        print("--------------------------------")

        choice=int(input("Enter your Choice:"))

        if choice == 1:
            f = count_frequency(x)  
            print("Frequency of Elements:",f)

        elif choice == 2:
            duplicates=finding_duplicates(f)
            print("Duplicates in List:",duplicates)

        elif choice == 3:
            high_frequent_element=most_frequent(f)
            print("Highest Frequent Element:",high_frequent_element)

        elif choice == 4:
            low_frequent_element=least_frequent(f)
            print("Lowest Frequent Element:",low_frequent_element)

        elif choice == 5:
            y=list(map(int,input("Enter the numbers: ").split()))   
            z=list(map(int,input("Enter the numbers: ").split()))   
            common=common_elements(y,z)
            print("Common Elements:",common)

        elif choice == 6:
            print("Exiting...")
            break


main()
