print("----------Geometry Calculator----------" )


while True:
    print("1. Perimeter: ")
    print("2. Area: ")
    choice1 = int(input("Please enter what do you want to calculate: "))
     
    if choice1 == 1:
    
     print("1. Circle: ")
     print("2. Rectangle: ")
     print("3. Triangle: ")
     print("4. Quit")
     choice2 = int(input("Please enter the shape: "))
     
     if choice2 == 1:
        radius = int(input("Enter radius:"))
        Perimeter_Circle = 2 * 3.14 * radius
        print("Perimeter of Circle is ",Perimeter_Circle)

     elif choice2 == 2:
        height = int(input("Enter the height of the rectangle: "))
        width = int(input("Enter the width of the rectangle:")) 
        Perimeter_Rectangle = 2 * height + width  
        print("Perimeter of Rectangle is ",Perimeter_Rectangle)

     elif  choice2 == 3:
        a = int(input("Enter the a side of the triangle: "))
        b = int(input("Enter the b side of the triangle: "))
        c = int(input("Enter the c side of the triangle: "))        
        Perimeter_Triangle = a+b+c 
        print("Perimeter of Triangle is ",Perimeter_Triangle)

     else:
        print("Invalid choice selected")
        break
    elif choice1 == 2:
     print("1. circle: ")
     print("2. rectangle: ")
     print("3. triangle: ")
     print("4. Quit")
     choice3 = int(input("Enter your choice: "))
     
     if choice3 == 1:
        radius = int(input("Enter radius:"))
        Area_Circle = 3.14 * radius * radius
        print("Area of Circle is ",Area_Circle)

     elif choice3 == 2:
        height = int(input("Enter Height: "))
        width = int(input("Enter width:")) 
        Area_Rectangle = height * width  
        print("Area of Rectangle is ",Area_Rectangle)

     elif choice3 == 3:
        height = int(input("Enter the height of the tiangle:"))
        width = int(input("Enter the width of the triangle:"))                
        Area_Triangle = height * width / 2  
        print("Area of Triangle is ",Area_Triangle)

     else:
        print("Enter valid option ")
