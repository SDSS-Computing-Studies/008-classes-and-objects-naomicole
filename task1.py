#! python3
"""
(10 points) 
Create a class object for a student.
It should have the following properties
str name
str studentNumber
int grade
list courses - to corresepond with course names
list grade - to correspond with grades

It should have the following methods:
average()       - determines the mathematical average of all course grades
getHonorRoll()  - determines the average of the top 5 courses if there are at least 5 courses.
                  returns True if the average is 86 or higher (on the honor roll)
                  returns False if not on the honor roll
showCourses()   - prints a list of all courses
showGrade(int)  - takes 1 parameter, the index of the list
                - displays the course name and grade
getCourses(list)- Receives a list of courses and stores that in the class property
getGrades(list) - Receives a list of grades and stores that in the class property
constructor     - should require the student name, studentNumber and grade (in that order)
"""

class student:

    name = ""
    studentNumber = ""
    grade = 0
    courses = []
    grades = []

    # properties should be listed first

    def __init__(self, name, studentNumber, grade): # You will need to create your own input parameters for all methods
        
        self.name = name 
        self.studentNumber = studentNumber
        self.grade = grade
        print("Hello " + self.name)
 
    def getCourses(self, gc):
        
        self.courses = gc
        
    def getGrades(self, grade1=0, grade2=0, grade3=0, grade4=0, grade5=0, grade6=0, grade7=0):
        lisgrade = []
        lisgrade.insert(0,grade1)
        lisgrade.insert(1,grade2)
        lisgrade.insert(1,grade3)
        lisgrade.insert(1,grade4)
        lisgrade.insert(1,grade5)
        lisgrade.insert(1,grade6)
        lisgrade.insert(1,grade7)
        self.grades = lisgrade

    def showCourses(self):
        
       liscourses = print(self.courses)
       return liscourses

    def showGrade(self, index):
        
        lis1 = self.courses
        lis2 = self.grades
        
        x = print("You have " + lis2[index] + "in " + lis1[index])
        return x

    def average(self): 
        
        length = len(self.grades)
        a = sum(self.grades)
        average = a/length 
        return average
        

    def getHonorRoll(self):
        
        lisgrades = self.grades
        lisgrades.sort()
        lisgrades.reverse()
        length = len(lisgrades)
        if length >= 5: 
            g1 = lisgrades[0]
            g2 = lisgrades[1]
            g3 = lisgrades[2]
            g4 = lisgrades[3]
            g5 = lisgrades[4]
            hr = (g1 + g2 + g3 + g4 + g5)/5
            if hr >= 86:
                return True
            else:
                return False
        else:
            x = print(self.name + " is not taking enough courses")
        return x

    def __del__(self):
        
        print("Thank you " + self.name + ", see you soon\n")

def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath","91334",11)
    st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
    st1.getGrades( [91, 94, 87, 99, 82, 100, 73])

    

   
    st2 = student("Joe Lunchbox","12346", 11)
    st2.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st2.getGrades( [71, 98, 93, 95, 68, 81, 71])

    


main()