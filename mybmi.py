#Jimmy Vo
#Jimmyvo866@gmail.com
#CPSC 223P
#Assignment 1


def calc_Bmi(weight, height):
    height = (height/100) # converts cms to meters (1m=100cm)
    bmi = (weight/(height**2))  #(kg/meters**2)
    return bmi

def calcMale_Bmr(weight, height, age): 
    bmrM = ((13.397*weight) + (4.799*height) - (5.677*age) + (88.362)) # weight(kg), height(cm), age(year), (kcal/day)
    return bmrM

def calcFemale_Bmr(weight, height, age):
    bmrF = ((9.247*weight) + (3.098*height) - (4.330*age) + (447.593))
    return bmrF

def bmi_Category(bmiNum, height, weight, measurements):
    height = (height/100) # converts cms to meters (1m=100cm)
    weeklyCal = 0
    extraCal = 0
    additionalWeight = 0
    minusWeight = 0

    if bmiNum < 16:
        bmiClass = 'Severe Thinness'
        print(' ')
        print('Based upon your BMI numbers, you are currently in the Severe Thinness category.')

        #move above a category
        extraCal = 0
        neededBmi =  (16.01 - bmiNum) #needed additional bmi numbers
        neededWeight = (neededBmi * (height**2)) #weight needed to move next category(kgs)
        additionalWeight = neededWeight
        while neededWeight > 0: #needed calories to gain weight
            extraCal = extraCal + 3500  #based on a week 500/day
            neededWeight = neededWeight - .45
        weeklyCal = (extraCal/52) # number of calories needed each week for a year 
        print('If you wanted to move up a BMI category, you would need to consume about', round(weeklyCal),
              'more calories a week over the course of 52 weeks.')
        if measurements == 'c': # prints based on unit scale user wanted  (c = U.S. customary)
            print('By doing so, you would have gained',round((additionalWeight*.4536)),'more lbs.')
        else:
            print('By doing so, you would have gained',round((additionalWeight)),'more kgs.')

        
    elif 15.99 < bmiNum < 17:
        bmiClass = 'Moderate Thinness'
        print(' ')
        print('Based upon your BMI numbers, you are currently in the Moderate Thinness category.')

        #move above a category
        extraCal = 0
        neededBmi =  (17 - bmiNum)
        neededWeight = (neededBmi * (height**2)) #weight needed to move next category(kgs)
        additionalWeight = neededWeight
        while neededWeight > 0:
            extraCal = extraCal + 3500
            neededWeight = neededWeight - .45
        weeklyCal = (extraCal/52)
        print('If you wanted to move up a BMI category, you would need to consume', round(weeklyCal),
              ' more calories a week over the course of 52 weeks.')
        if measurements == 'c':
            print('By doing so, you would have gained',round((additionalWeight*.4536)),'more lbs.')
        else:
            print('By doing so, you would have gained',round((additionalWeight)),'more kgs.')
        print(' ')

        #move below a category, same as moving above but you deal with losing calories in losing weight.
        loseCal = 0
        decreaseBmi = (bmiNum - 15.99)
        decNeedWeight = (decreaseBmi * (height**2)) #weight needed to move below category
        minusWeight = decNeedWeight
        while decNeedWeight > 0:
            loseCal = loseCal + 3500
            decNeedWeight = decNeedWeight - .45
        loseWeeklyCal = (loseCal/52)
        print('If you wanted to move down a BMI category, you would need to consume', round(loseWeeklyCal),
              'less calories a week over the course of 52 weeks.')
        if measurements == 'c':
            print('By doing so, you would have lost', round((minusWeight*.4536)), 'lbs.')
        else:
            print('By doing so, you would have lost',round(minusWeight),'kgs.')
    elif 16.99 < bmiNum < 18.5:
        bmiClass = 'Mild Thinness'
        print(' ')
        print('Based upon your BMI numbers, you are currently in the Mild Thinness category.')

        #move above a category
        extraCal = 0
        neededBmi =  (18.5 - bmiNum)
        neededWeight = (neededBmi * (height**2)) #weight needed to move next category(kgs)
        additionalWeight = neededWeight
        while neededWeight > 0:
            extraCal = extraCal + 3500
            neededWeight = neededWeight - .45
        weeklyCal = (extraCal/52)
        print('If you wanted to move up a BMI category, you would need to consume', round(weeklyCal), 
              'more calories a week over the course of 52 weeks.')
        if measurements == 'c':
            print('By doing so, you would have gained',round((additionalWeight*.4536)),'more lbs.')
        else:
            print('By doing so, you would have gained',round((additionalWeight)),'more kgs.')
        print(' ')

        #move below a category
        loseCal = 0
        decreaseBmi = (bmiNum - 16.99)
        decNeedWeight = (decreaseBmi * (height**2)) #weight needed to move below category
        minusWeight = decNeedWeight
        while decNeedWeight > 0:
            loseCal = loseCal + 3500
            decNeedWeight = decNeedWeight - .45
        loseWeeklyCal = (loseCal/52)
        print('If you wanted to move down a BMI category, you would need to consume about', round(loseWeeklyCal),
              'less calories a week over the course of 52 weeks.')
        if measurements == 'c':
            print('By doing so, you would have lost', round((minusWeight*.4536)), 'lbs.')
        else: 
            print('By doing so, you would have lost',round(minusWeight),'kgs.')

    elif 18.49 < bmiNum < 25:
        bmiClass = 'Normal Range'
        print(' ')
        print('Based upon your BMI numbers, you are currently in the Normal Range category.')

        #move above a category
        Extracal = 0
        neededBmi =  (25 - bmiNum)
        neededWeight = (neededBmi * (height**2)) #weight needed to move next category(kgs)
        additionalWeight = neededWeight
        while neededWeight > 0:
            extraCal = extraCal + 3500
            neededWeight = neededWeight - .45
        weeklyCal = (extraCal/52)
        print('If you wanted to move up a BMI category, you would need to consume about', round(weeklyCal),
              'more calories a week over the course of 52 weeks.')
        if measurements == 'c':
            print('By doing so, you would have gained',round((additionalWeight*.4536)),'more lbs.')
        else:
            print('By doing so, you would have gained',round((additionalWeight)),'more kgs.')
        print(' ')

        #move below a category
        loseCal = 0
        decreaseBmi = (bmiNum - 18.49)
        decNeedWeight = (decreaseBmi * (height**2)) #weight needed to move below category
        minusWeight = decNeedWeight
        while decNeedWeight > 0:
            loseCal = loseCal + 3500
            decNeedWeight = decNeedWeight - .45
        loseWeeklyCal = (loseCal/52)
        print('If you wanted to move down a BMI category, you would need to consume about', round(loseWeeklyCal),
              'less calories a week over the course of 52 weeks.')
        if measurements == 'c':
            print('By doing so, you would have lost', round((minusWeight*.4536)), 'lbs.')
        else:
            print('By doing so, you would have lost',round(minusWeight),'kgs.')

    elif 24.99 < bmiNum < 30:
        bmiClass = 'Overweight'
        print(' ')
        print('Based upon your BMI numbers, you are currently in the Over Weight category.')

        #move above a category
        extraCal = 0
        neededBmi =  (30 - bmiNum)
        neededWeight = (neededBmi * (height**2)) #weight needed to move next category(kgs)
        additionalWeight = neededWeight
        while neededWeight > 0:
            extraCal = extraCal + 3500
            neededWeight = neededWeight - .45
        weeklyCal = (extraCal/52)
        print('If you wanted to move up a BMI category, you would need to consume', round(weeklyCal),
              'more calories a week over the course of 52 weeks.')
        if measurements == 'c':
            print('By doing so, you would have gained',round((additionalWeight*.4536)),'more lbs.')
        else:
            print('By doing so, you would have gained',round((additionalWeight)),'more kgs.')
        print(' ')

        #move below a category
        loseCal = 0
        decreaseBmi = (bmiNum - 24.99)
        decNeedWeight = (decreaseBmi * (height**2)) #weight needed to move below category
        minusWeight = decNeedWeight
        while decNeedWeight > 0:
            loseCal = loseCal + 3500
            decNeedWeight = decNeedWeight - .45
        loseWeeklyCal = (loseCal/52)
        print('If you wanted to move down a BMI category, you would need to consume', round(loseWeeklyCal),
              'less calories a week over the course of 52 weeks.')
        if measurements == 'c':
            print('By doing so, you would have lost', round((minusWeight*.4536)), 'lbs.')
        else:
            print('By doing so, you would have lost',round(minusWeight),'kgs.')

    elif 29.99 < bmiNum < 35:
        bmiClass = 'Obese Class I (Moderate)'
        print(' ')
        print('Based upon your BMI numbers, you are currently in the Obese Class I (Moderate) category.')

        #move above a category
        extraCal = 0
        neededBmi =  (35 - bmiNum)
        neededWeight = (neededBmi * (height**2)) #weight needed to move next category(kgs)
        additionalWeight = neededWeight
        while neededWeight > 0:
            extraCal = extraCal + 3500
            neededWeight = neededWeight - .45
        weeklyCal = (extraCal/52)
        print('If you wanted to move up a BMI category, you would need to consume', round(weeklyCal),
              'more calories a week over the course of 52 weeks.')
        if measurements == 'c':
            print('By doing so, you would have gained',round((additionalWeight*.4536)),'more lbs.')
        else:
            print('By doing so, you would have gained',round((additionalWeight)),'more kgs.')
        print(' ')

        #move below a category
        loseCal = 0
        decreaseBmi = (bmiNum - 29.99)
        decNeedWeight = (decreaseBmi * (height**2)) #weight needed to move below category
        minusWeight = decNeedWeight
        while decNeedWeight > 0:
            loseCal = loseCal + 3500
            decNeedWeight = decNeedWeight - .45
        loseWeeklyCal = (loseCal/52)
        print('If you wanted to move down a BMI category, you would need to consume', round(loseWeeklyCal),
              'less calories a week over the course of 52 weeks.')  
        if measurements == 'c':
            print('By doing so, you would have lost', round((minusWeight*.4536)), 'lbs.')
        else:
            print('By doing so, you would have lost',round(minusWeight),'kgs.')
        
    elif 34.99 < bmiNum < 40:
        bmiClass = 'Obese Class II (Severe)'
        print(' ')
        print('Based upon your BMI numbers, you are currently in the Obese Class II (Severe) category.')
        
        #move above a category
        extraCal = 0
        neededBmi =  (40 - bmiNum)
        neededWeight = (neededBmi * (height**2)) #weight needed to move next category(kgs)
        additionalWeight = neededWeight
        while neededWeight > 0:
            extraCal = extraCal + 3500
            neededWeight = neededWeight - .45
        weeklyCal = (extraCal/52)
        print('If you wanted to move up a BMI category, you would need to consume', round(weeklyCal), 
              'more calories a week over the course of 52 weeks.')
        if measurements == 'c':
            print('By doing so, you would have gained',round((additionalWeight*.4536)),'more lbs.')
        else:
            print('By doing so, you would have gained',round(additionalWeight),'more kgs.')
        print(' ')

        #move below a category
        loseCal = 0
        decreaseBmi = (bmiNum - 34.99)
        decNeedWeight = (decreaseBmi * (height**2)) #weight needed to move below category
        minusWeight = decNeedWeight
        while decNeedWeight > 0:
            loseCal = loseCal + 3500
            decNeedWeight = decNeedWeight - .45
        loseWeeklyCal = (loseCal/52)
        print('If you wanted to move down a BMI category, you would need to consume', round(loseWeeklyCal),
              'less calories a week over the course of 52 weeks.')
        if measurements == 'c':
            print('By doing so, you would have lost', round((minusWeight*.4536)), 'lbs.')
        else:
            print('By doing so, you would have lost',round(minusWeight),'kgs.')
        
    else:
        bmiClass = 'Obese Class III (Very Severe)'
        print('Based upon your BMI numbers, you are currently in the Obese Class III (Very Severe) category.')
        print(' ')

        #move below a category
        loseCal = 0
        decreaseBmi = (bmiNum - 39.99)
        decNeedWeight = (decreaseBmi * (height**2)) #weight needed to move below category
        minusWeight = decNeedWeight
        while decNeedWeight > 0:
            loseCal = loseCal + 3500
            decNeedWeight = decNeedWeight - .45
        loseWeeklyCal = (loseCal/52)
        
        print('If you wanted to move down a BMI category, you would need to consume', round(loseWeeklyCal), 
              'less calories a week over the course of 52 weeks.')
        if measurements == 'c':
            print('By doing so, you would have lost',round((minusWeight*.4536)),'lbs.')
        else:
            print('By doing so, you would have lost',round(minusWeight),'kgs.')

def main( ):
    firstName = input('Hello, what is your name? ')
    askSex = input('1. Are you a male or female? ')
    userAge = input('2. Please enter your age: ')
    userAge = float(userAge)
    userHeight = input('3. Please enter your height(inches): ')
    userHeight = float(userHeight)
    userWeight = input('4. Please enter your weight(lbs): ')
    userWeight = float(userWeight)
    userMeasurements = input('5. Would you like to receive your report in metric units(m) or U.S. customary units(c)? ')
    print(" ")
    userHeight = (userHeight * 2.54) # converts userHeight(inches) to cms (1 inch = 2.54cm)
    userWeight = (userWeight * 0.4536) # converts userWeight(lbs) to kgs (1 lb = 0.4536kg)
    
    #different calculations for gender for bmi and bmr
    if askSex == 'male':
        totalBmi = calc_Bmi(userWeight, userHeight)
        totalBmr = calcMale_Bmr(userWeight, userHeight, userAge)
    else:
        totalBmi =  calc_Bmi(userWeight, userHeight)
        totalBmr = calcFemale_Bmr(userWeight, userHeight, userAge)
        
    
    totalBmi = float(totalBmi) #BMI number
    totalBmr = float(totalBmr)

    bmi_Category(totalBmi, userHeight, userWeight, userMeasurements)   
    

if __name__ == '__main__':
    main( )
