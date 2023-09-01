#Student Registration Program
class Student:
    def __init__(self,fname,lname,strand,grade,section):
        self.fname = fname
        self.lname = lname
        self.strand = strand
        self.grade = grade
        self.section = section

    def introduce(self):
        print("     Name: "+self.fname+" "+self.lname)
        print("     Strand: "+self.strand)
        print("     Grade & Section: "+str(self.grade)+"-"+self.section)


Registree = []
num = int(input("How many students do you want to register?: "))
for x in range(num):
    fname = input("First Name: ")
    lname = input("Last Name: ")
    strand = input("Strand: ")
    grade = int(input("Grade Level: "))
    section = input("Section: ")
    s = Student(fname,lname,strand,grade,section)
    Registree.append(s)
    print()

listing = input("List all students or a specific student? [All/Specific] ")
if listing == "All" or listing == "all":
    y = 1
    for i in Registree:
        print("Student #"+str(y))
        i.introduce()
        y += 1
        print()
elif listing == "Specific" or listing == "specific":
    index = int(input("Which student? Enter a number: "))
    rindex = index - 1
    print("Student #"+str(index))
    Registree[rindex].introduce()

else:
    pass