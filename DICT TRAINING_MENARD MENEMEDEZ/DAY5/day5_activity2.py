class DemoClass:
    def __init__(self) -> None:
        print('Called')

    def studentDetails(self, name, course, grade):
        self.name = name
        self.course = course
        self.grade = grade

        msg = f'Student Name : {self.name}\nStudent Course : {self.course}\nStudent Grade : {self.grade}'
        print(msg)


class1 = DemoClass()
class2 = DemoClass()

class1.studentDetails('Menard', 'BSIT', '85')
class2.studentDetails('Gem Rey', 'BSIT', '100')


object_list = []
object_list.append(class1)