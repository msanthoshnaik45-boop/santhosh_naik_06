class student:
    college_name="AUS"
    def read(self,rno,name):
        self.rno=rno
        self.name=name
    def write(self):
        print(self.rno,"\n",self.name,"\n",student.college_name)


stu1=student()
stu1.read(1,"sowmya")
stu1.write()
