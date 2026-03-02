class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    
    def pass_fail(self):
        if self.marks > 40:
            print("Pass")
        else:
            print("Fail")
    
    def print(self):
        print(self.name, self.rollno, self.marks)

S1 = Student("Nihal", 25, 39)
S2 = Student("Sowmya", 45, 80)
S1.print()
S1.pass_fail()
S2.pass_fail()

# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

# np.random.seed(42)

# X = np.random.rand(50, 1) * 100  

# Y = 3.5 * X + np.random.randn(50, 1) * 20

# model = LinearRegression()
# model.fit(X, Y)
# Y_pred = model.predict(X)