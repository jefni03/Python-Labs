# Authors: Jeffrey Ni 
# Assignment: Project #1
# Completed (or last revision):  02/20/2023

import math

system = input("Which BMI system would you like to use? Choose USA or Metric: ")
if system == "USA":
    usa_weight = float(input("Please enter your weight in lbs: "))
    usa_height = float(input("Please enter your height in inches: "))
    if usa_weight <= 0:
        print("Please enter a positive weight value in lbs")
    elif usa_height <= 0:
        print("Please enter a positive height value in inches")
    BMI = 703 * usa_weight/pow(usa_height, 2)
elif system == "Metric":
    metric_weight = float(input("Please enter your weight in kg: "))
    metric_height = float(input("Please enter your height in meters: "))
    if metric_weight <= 0:
        print("Please enter a positive weight value in kg")
    elif metric_height <= 0:
        print("Please enter a positive height value in meters")
    BMI = metric_weight/pow(metric_height, 2)
if BMI >= 18 and BMI <= 25:
    print("Your BMI falls within the normal range")
elif BMI > 25:
    print("Your BMI falls within the overweight range")
else:
    print("YOur bodyweight falls within the underweight range")
'''
Results:
Which BMI system would you like to use? Choose USA or Metric: USA
Please enter your weight in lbs: 155   
Please enter your height in inches: 70 
Your BMI falls within the normal range 
Which BMI system would you like to use? Choose USA or Metric: USA
Please enter your weight in lbs: 172   
Please enter your height in inches: 68 
Your BMI falls within the overweight range
Which BMI system would you like to use? Choose USA or Metric: Metric
Please enter your weight in kg: 75
Please enter your height in meters: 1.83
Your BMI falls within the normal range
Which BMI system would you like to use? Choose USA or Metric: Metric
Please enter your weight in kg: 51.5
Please enter your height in meters: 1.68
Your BMI falls within the normal range
Which BMI system would you like to use? Choose USA or Metric: USA
Please enter your weight in lbs: 130
Please enter your height in inches: 62
Which BMI system would you like to use? Choose USA or Metric: Metric
Please enter your weight in kg: 80
Please enter your height in meters: 1.98
Your BMI falls within the normal range
Please enter your weight in lbs: 0
Please enter your height in inches: 120
Please enter a positive weight value in lbs
YOur bodyweight falls within the underweight range
Which BMI system would you like to use? Choose USA or Metric: Metric
Please enter your weight in kg: 69
Please enter your height in meters: 0
Please enter a positive height value in meters
'''

# Task 2


COMPARED_ACCURACY = 0.000001
PROGRAM_END = False

while not False:
    sinx = 0 
    PROGRAM_END = False
    user_choice = input("Please enter the radian or put 'pi' to use pi: ")
    if (user_choice == "pi"):
        denominator = int(input("Enter denominator:")) 
        while(denominator == 0):
            print("The denominator cannot be zero")
            denominator = int(input("Enter the denominator: "))
        if(denominator != 0):
            pi_format = math.pi/denominator
            user_choice = pi_format

            while not PROGRAM_END: 
                for i in range(100000): 
                    print("This is iteration: ", i) 
                    sinx += (((-1)**i)/math.factorial(2*i + 1)) * (math.pow(user_choice, (2*i+1))) 
                    print("Estimated Value: " + str(sinx))
                    print("Actual Value: " + str(math.sin(user_choice)))
                    difference = abs(math.sin(user_choice) - sinx)
                    print("Difference: " + str(difference))

                    if difference <= COMPARED_ACCURACY:
                        print("It is accurate to 0.000001")
                        PROGRAM_END = True 
                        break
                    else:
                        choice = input("Y/N to continue") 
                    if(choice == 'Y'):
                        continue
                    elif (choice == 'N'):
                        print("program over")
                        PROGRAM_END = True 
                        break

    elif (user_choice != "pi"):
        user_choice = float(user_choice) 
        while not PROGRAM_END: 
            for i in range(1000000): 
                print("iteration", i)
                sinx += (((-1)**i)/math.factorial(2*i + 1)) * (math.pow(user_choice, (2*i+1))) 
                print("Estimated Value: " + str(sinx))
                print("Actual Value: " + str(math.sin(user_choice)))
                difference = abs(math.sin(user_choice) - sinx)
                print("Difference: " + str(difference))

                if difference <= COMPARED_ACCURACY:
                        print("It is accurate to 0.000001")
                        PROGRAM_END = True 
                        break
                else:
                        choice = input("Y/N to continue") 
                if(choice == 'Y'):
                        continue
                elif (choice == 'N'):
                        print("program over")
                        PROGRAM_END = True 
                        break

'''
Results:

Please enter the radian or put 'pi' to use pi: pi
Enter denominator:3
This is iteration:  0
Estimated Value: 1.0471975511965976
Actual Value: 0.8660254037844386
Difference: 0.18117214741215903
Y/N to continueY
This is iteration:  1
Estimated Value: 0.8558007815651174
Actual Value: 0.8660254037844386
Difference: 0.010224622219321189
Y/N to continueY
This is iteration:  2
Estimated Value: 0.8662952837868348
Actual Value: 0.8660254037844386
Difference: 0.00026988000239625
Y/N to continueY
This is iteration:  3
Estimated Value: 0.8660212716563727
Actual Value: 0.8660254037844386
Difference: 4.132128065936769e-06
Y/N to continueY
This is iteration:  4
Estimated Value: 0.8660254450997812
Actual Value: 0.8660254037844386
Difference: 4.131534259155245e-08
It is accurate to 0.000001

Please enter the radian or put 'pi' to use pi: pi
Enter denominator:-6
This is iteration:  0
Estimated Value: -0.5235987755982988
Actual Value: -0.49999999999999994
Difference: 0.02359877559829887
Y/N to continueY
This is iteration:  1
Estimated Value: -0.49967417939436376
Actual Value: -0.49999999999999994
Difference: 0.00032582060563618453
Y/N to continueY
This is iteration:  2
Estimated Value: -0.5000021325887924
Actual Value: -0.49999999999999994
Difference: 2.1325887925027764e-06
Y/N to continueY
This is iteration:  3
Estimated Value: -0.4999999918690232
Actual Value: -0.49999999999999994
Difference: 8.130976725251315e-09
It is accurate to 0.000001

Please enter the radian or put 'pi' to use pi: 0.112
iteration 0
Estimated Value: 0.112
Actual Value: 0.11176599215128519
Difference: 0.00023400784871481506
Y/N to continueY
iteration 1
Estimated Value: 0.11176584533333334
Actual Value: 0.11176599215128519
Difference: 1.4681795185156332e-07
It is accurate to 0.000001

Please enter the radian or put 'pi' to use pi: pi
Enter denominator:1
This is iteration:  0
Estimated Value: 3.141592653589793
Actual Value: 1.2246467991473532e-16
Difference: 3.141592653589793
Y/N to continueY
This is iteration:  1
Estimated Value: -2.0261201264601763
Actual Value: 1.2246467991473532e-16
Difference: 2.0261201264601763
Y/N to continueY
This is iteration:  2
Estimated Value: 0.5240439134171688
Actual Value: 1.2246467991473532e-16
Difference: 0.5240439134171687
Y/N to continueY
This is iteration:  3
Estimated Value: -0.07522061590362306
Actual Value: 1.2246467991473532e-16
Difference: 0.07522061590362318
Y/N to continueY
This is iteration:  4
Estimated Value: 0.006925270707505149
Actual Value: 1.2246467991473532e-16
Difference: 0.006925270707505027
Y/N to continueY
This is iteration:  5
Estimated Value: -0.0004451602382091989
Actual Value: 1.2246467991473532e-16
Difference: 0.00044516023820932135
Y/N to continueY
This is iteration:  6
Estimated Value: 2.114256755841339e-05
Actual Value: 1.2246467991473532e-16
Difference: 2.1142567558290925e-05
Y/N to continueY
This is iteration:  7
Estimated Value: -7.727858894168152e-07
Actual Value: 1.2246467991473532e-16
Difference: 7.727858895392798e-07
It is accurate to 0.000001

Please enter the radian or put 'pi' to use pi: pi
Enter denominator:2
This is iteration:  0
Estimated Value: 1.5707963267948966
Actual Value: 1.0
Difference: 0.5707963267948966
Y/N to continueY
This is iteration:  1
Estimated Value: 0.9248322292886504
Actual Value: 1.0
Difference: 0.07516777071134961
Y/N to continueY
This is iteration:  2
Estimated Value: 1.0045248555348174
Actual Value: 1.0
Difference: 0.004524855534817407
Y/N to continueY
This is iteration:  3
Estimated Value: 0.9998431013994987
Actual Value: 1.0
Difference: 0.00015689860050127624
Y/N to continueY
This is iteration:  4
Estimated Value: 1.0000035425842861
Actual Value: 1.0
Difference: 3.542584286142514e-06
Y/N to continueY
This is iteration:  5
Estimated Value: 0.999999943741051
Actual Value: 1.0
Difference: 5.625894905492146e-08
It is accurate to 0.000001

Please enter the radian or put 'pi' to use pi: pi
Enter denominator:4
This is iteration:  0
Estimated Value: 0.7853981633974483
Actual Value: 0.7071067811865476
Difference: 0.0782913822109007
Y/N to continueY
This is iteration:  1
Estimated Value: 0.7046526512091675
Actual Value: 0.7071067811865476
Difference: 0.0024541299773800374
Y/N to continueY
This is iteration:  2
Estimated Value: 0.7071430457793603
Actual Value: 0.7071067811865476
Difference: 3.6264592812695895e-05
Y/N to continueY
This is iteration:  3
Estimated Value: 0.7071064695751781
Actual Value: 0.7071067811865476
Difference: 3.116113694856537e-07
It is accurate to 0.000001

Please enter the radian or put 'pi' to use pi: pi
Enter denominator:-4
This is iteration:  0
Estimated Value: -0.7853981633974483
Actual Value: -0.7071067811865476
Difference: 0.0782913822109007
Y/N to continueY
This is iteration:  1
Estimated Value: -0.7046526512091675
Actual Value: -0.7071067811865476
Difference: 0.0024541299773800374
Y/N to continueY
This is iteration:  2
Estimated Value: -0.7071430457793603
Actual Value: -0.7071067811865476
Difference: 3.6264592812695895e-05
Y/N to continueY
This is iteration:  3
Estimated Value: -0.7071064695751781
Actual Value: -0.7071067811865476
Difference: 3.116113694856537e-07
It is accurate to 0.000001

'''