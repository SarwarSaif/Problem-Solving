def print_simple_triangle(pyramid_list, no_of_rows):
    char = '#'
    if(no_of_rows == 0):  
        print("achi ", pyramid_list)   
        print("\n".join(pyramid_list)) 
    else: 
        pyramid_list.append(char*no_of_rows)
        no_of_rows=no_of_rows-1
        print("achi ", pyramid_list)
        print_simple_triangle(pyramid_list, no_of_rows)

def print_simple_pyramid(pyramid_list, no_of_rows, char):
    for i in range(no_of_rows):
        pyramid_list.append(\
            (" "*(no_of_rows-1-i))\
                +(char*(1+(2*i)))\
                    +(" "*(no_of_rows-1-i))\
            )
    print("\n".join(pyramid_list))


no_of_rows = int(input("Enter the number of rows "))
char = input("Enter the character you want: ")[0]
pyramid_list = []
print_simple_pyramid(pyramid_list, no_of_rows, char)