new=''
while True:
    print("------------------------------")
    print("---        APP MENU        ---")
    print("------------------------------")
    print('== press 0 for create new list')
    print('== press 1 for adding the element into list ')
    print('== press 2 for update/replace value')
    print('== press 3 for remove value')
    print('== press 4 for reading  value')
    print('== press 5 for Exit')
    print("------------------------------")
    op=int(input("Select Any Option: "))
    if op==0:
        new=list(new)
        print(new)
    elif op==1:
        n=int(input("Enter any no:"))
        new.append(n)
        print("No added successfully..........","and the list",new)
    elif op==2:
        x=int(input("Enter index no to replace: "))
        y=int(input("Enter new value to replace: "))
        new[x]=y
        print("Value replace successfully:",new)
    elif op==3:
        x=int(input("Enter Number to remove:"))
        new.remove(x)
        print("Value removed sucessfully...",new)
    elif op==4:
        print(new)
    elif op==5:
        print('Thanks for Using My App!!')
        break
    else:
        print('Select Correct Option')