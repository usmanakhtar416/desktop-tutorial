class Father:

    family_name = "Smith"  

    def __init__(self, occupation):
        self.occupation = occupation 

    def father_info(self):
       
        print(f"Father's Occupation: {self.occupation}")

    @classmethod
    def family_name_info(cls):

        print(f"Family Name: {cls.family_name}")

    @staticmethod
    def hobby():
      
        print("Father loves fishing.")


print("-----------------------------------------")

class Mother:

    family_name = "Smith"  

    def __init__(self, profession):
        self.profession = profession  

    def mother_info(self):

        print(f"Mother's Profession: {self.profession}")

    @classmethod
    def family_name_info(cls):

        print(f"Family Name: {cls.family_name}")

    @staticmethod
    def hobby():

        print("Mother loves gardening.")

class Child(Father, Mother):

    def __init__(self, father_occupation, mother_profession, school):
        Father.__init__(self, father_occupation)
        Mother.__init__(self, mother_profession)
        self.school = school  

    def child_info(self):

        print(f"Child studies at {self.school}")


child = Child("Engineer", "Doctor", "Greenwood High")
child.father_info()
child.mother_info()
child.child_info()
child.family_name_info()
Father.hobby()
Mother.hobby()


print("-----------------------------------------------")


class Grandpa:

    family_origin = "Canada"  

    def __init__(self, wisdom):
        self.wisdom = wisdom  

    def grandpa_info(self):

        print(f"Grandpa's Wisdom: {self.wisdom}")

    @classmethod
    def origin_info(cls):

        print(f"Family Origin: {cls.family_origin}")

    @staticmethod
    def legacy():

        print("Grandpa is known for his woodworking skills.")

class Father(Grandpa):

    def __init__(self, wisdom, occupation):
        super().__init__(wisdom)
        self.occupation = occupation  

    def father_info(self):

        print(f"Father's Occupation: {self.occupation}")

class Child(Father):

    def __init__(self, wisdom, occupation, school):
        super().__init__(wisdom, occupation)
        self.school = school  # Instance variable

    def child_info(self):

        print(f"Child studies at {self.school}")


grandpa = Grandpa("Wise")
grandpa.grandpa_info()
grandpa.origin_info()
Grandpa.legacy()

father = Father("Very Wise", "Engineer")
father.father_info()
father.grandpa_info()

child = Child("Extremely Wise", "Teacher", "Greenwood High")
child.child_info()
child.father_info()
child.grandpa_info()