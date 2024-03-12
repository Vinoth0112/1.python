class MultipleFunctions1():
    
    def SubfieldsInAI():
        List=['Sub-fields in AI are:','Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language processing']
        for AI in List:
            print(AI)
            message=AI
        return message

    
    def OddEven():
        num=int(input("Enter a number: "))
        if((num%2)==0):
            print(num,"is Even Number")
            message="is Even Number"
        else:
            print(num,"is Odd Number")
            message="is Odd number"
        return message
    
    def ElegiblityForMarriage():
        Gender=input("Your Gender:")
        Age=int(input("Your Age:"))
        if((Gender=='Male') and (Age>20)):
            print("ELIGIBLE")
            message="ELIGIBLE"
        elif((Gender=='Female') and (Age>17)):
            print("ELIGIBLE")
            message="ELIGIBLE"

        else:
            print("NOT ELIGIBLE")
            message="NOT ELIGIBLE"
            return message
    
    def percentage():
        Subject1=int(input("Subject1= "))
        Subject2=int(input("Subject2= "))
        Subject3=int(input("Subject3= "))
        Subject4=int(input("Subject4= "))
        Subject5=int(input("Subject5= "))

        Total=Subject1+Subject2+Subject3+Subject4+Subject5
        print("Total:",Total)
        percentage=(Total)*(100/500) 

        print ("Percentage is: ",percentage)
        message="Percentage is",percentage

        return message
    
    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        Area_of_triangle=(Height*Breadth)/2
        print("Area of Triangle",Area_of_triangle)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        Perimeter_of_Triangle=(Height1+Height2+Breadth)
        print("Perimeter of Triangle: ",Perimeter_of_Triangle)
        message=Perimeter_of_Triangle
        return message

