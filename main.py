# Nadia Al-Salem
# 1203608

from abc import ABC , abstractmethod
import matplotlib.pyplot as plt
import sys

class user_Managment:
    # create a file that contains information of login
    def __init__(self):
        # Open the file in write mode to initialize it
        with open('login_information.txt', 'w') as loginfile:
            loginfile.write('nurse\n')  # Add a newline character to separate username and password
            loginfile.write('123456\n')  # Add a newline character

        # Open the file in read mode to read the data
        with open('login_information.txt', 'r') as loginfile:
            # Read the lines and strip newline characters
            lines = loginfile.readlines()
            self.username = lines[0].strip()
            self.password = lines[1].strip()

        self.loginCount = 0

        # login function
    def login(self , entered_name , entered_password):
        self.loginCount += 1
        if entered_name == self.username and entered_password == self.password:
            return True
        else:
            False

class Test( ABC ):
    # Number of sample of each test
    def __init__(self , samples_count):
        self.samples_count = samples_count

    @abstractmethod
    def start_test(self):
        pass

class A1CTest(Test):
    def start_test(self):
        print("Number of readings ",self.samples_count)
        MyReadings = []
        sum = 0
        # loop to take readings from the user
        for i in range(10):
            # Input the fasting blood sugar level
            result = float(input('Enter yours diabetes readings : '))
            print( f'remaining readings {9 - i}' )
            MyReadings.append(result)
            sum += result
        avg = sum / 10
        # Get the result and print it
        print('your average readings is = ', avg)
        if avg < 5.7 :
            print("Normal")
        elif avg >= 5.7 and avg <= 6.4:
            print('prelude to diabetes')
        else:
            print('You have diabetes')
        # show the result in matplot
        labels = [ 'Reading 1' , 'Reading 2' , 'Reading 3' , 'Reading 4' , 'Reading 5' , 'Reading 6','Reading 7','Reading 8','Reading 9','Reading 10' ]
        plt.plot( labels , MyReadings , color='green' )
        plt.xlabel( 'Hemoglobin Readings' )
        plt.ylabel( 'Hemoglobin Level (mg/dL)' )
        plt.title( 'Hemoglobin A1C test' )
        plt.grid( )
        plt.show( )

class FBCLTTest(Test):
    def start_test(self):
        print("Number of readings ",self.samples_count)
        # Input the fasting blood sugar level (in mg/dL or 5.6 mmol/L)
        result = float(input('Enter yours diabetes readings : '))
        # Get the result and print it
        if result < 100:
            print('Normal (less than 100 mg/dL or 5.6 mmol/L)')
        elif 100 <= result < 126:
            print('Prediabetes (100-125 mg/dL or 5.6-6.9 mmol/L)')
        else:
            print('Diabetes (126 mg/dL or higher, or in two separate tests)')
        # show the result in matplot
        labels = [50,100,150,200]
        plt.plot( labels ,color='gray')
        plt.xlabel( 'sugar Readings' )
        plt.ylabel( 'sugar Level (mg/dL)' )
        plt.title( 'Fasting blood sugar test' )
        plt.grid( )
        plt.show( )

class OGTTTest(Test):
    def	start_test(self):
        print("Number of readings ",self.samples_count)
        MyReadings = []
        sum = 0
        # loop to take the readings from the user
        for i in range(6):
            # Input the fasting blood sugar level
            result = float(input('Enter yours diabetes readings : '))
            print( f'remaining readings {5 - i}' )
            MyReadings.append(result)
            sum += result
        avg = sum / 6
        # Get the result and print it
        print('your average readings is = ', avg)
        if avg < 140 :
            print("Normal (less than 140 mg/dL or 7.8 mmol/L)")
        elif 140 <= avg <= 199:
            print('Prelude to diabetes (140-199 mg/dL or 7.8-11.0 mmol/L)')
        else:
            print('Diabetes (200 mg/dL or higher, or after two hours, indicative of diabetes)')
        # show the result in matplot
        labels = [ 'Reading 1' , 'Reading 2' , 'Reading 3' , 'Reading 4' , 'Reading 5' , 'Reading 6' ]
        plt.plot( labels , MyReadings , color='blue' )
        plt.xlabel( 'Glucose Readings' )
        plt.ylabel( 'Glucose Level (mg/dL)' )
        plt.title( 'Oral Glucose Tolerance Test' )
        plt.grid( )
        plt.show( )

# create instance of each class
user_instance = user_Managment( )
a1ctest = A1CTest(10)
fbclttest = FBCLTTest(1)
ogtttest = OGTTTest(6)

# user will choose Diabetes Screening
def proceed_test():
    test_name = input( 'Enter the Diabetes Screening that you want : ' )
    if test_name == 'A1C':
        a1ctest = A1CTest(10)
        a1ctest.start_test()
        # ask user if he went to do a new test
        new_test = input('Do you want to do new test ? (Yes or No)')
        if new_test == 'yes':
            proceed_test()
        elif new_test == 'No':
            sys.exit( ) # end the system
    elif test_name == 'FBCLT':
        fbclttest = FBCLTTest(1)
        fbclttest.start_test()
        new_test = input('Do you want to do new test ? (Yes or No)')
        if new_test == 'yes':
            proceed_test()
        elif new_test == 'No':
            sys.exit( ) # end the system
    elif test_name == 'OGTT':
        ogtttest = OGTTTest(6)
        ogtttest.start_test()
        new_test = input('Do you want to do new test ? (Yes or No)')
        if new_test == 'yes':
            proceed_test()
        elif new_test == 'No':
            sys.exit() # end the system

# user can try 3 times before end the system
while user_instance.loginCount < 3:
    username = input( 'Enter your name : ' )
    password = input( 'Enter your password : ' )
    if user_instance.login( username , password ):
        proceed_test()
    else:
        print( 'Login Failed , enter your username and password again !' )
        print( f'remaining tries {3 - user_instance.loginCount}' )

