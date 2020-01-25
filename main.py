
##############################
#Computer Project #3
#
#  Algorithm
#   Ask user if they are a resident, if not, ask if they are international
#   Ask user what grade level they are
#   if the user enters an invalid input, make them enter a correct input
#   Ask what college the user is in
#   Ask the user how many credits they are taking
#   Create logical statements for tuition based on residency
#   Create logical statements for tuition based on grade level
#   Create logical statements for tuition calculation based on college
#   Create logical statements for tuition based on number of credits
#   Print the user's tuition calculation
#   Ask the user if they would like another calculation
#   if user answers yes, then re-ask the same questions
#   if user answers no, break the code
###############################





print("2019 MSU Undergraduate Tuition Calculator.")
print()

while True:
    user_residency= input("Resident (yes/no): ") #ask if user is a resident
    user_residency_lowercase= user_residency.lower()
    if user_residency_lowercase!="yes": #if reponse isn't yes, then it's no
        user_residency_lowercase=="no"
    if user_residency_lowercase=="no": # if no, then check if international
        international= input("International (yes/no): ")
        international_lowercase= international.lower()
    
    #Ask for user's grade level
    user_level= input("Level—freshman, sophomore, junior, senior: ")
    user_level_lowercase= user_level.lower()
    #If reponse isn't adequate, print error message
    while user_level_lowercase!="freshman" \
    and user_level_lowercase!="sophomore" and user_level_lowercase!="junior"\
    and user_level_lowercase!="senior":
        print("Invalid input. Try again.")
        #Ask question again, if reponse is adequate break this loop
        user_level= input("Level—freshman, sophomore, junior, senior: ")
        user_level_lowercase= user_level.lower()
        if user_level_lowercase=="freshman" \
        or user_level_lowercase=="sophomore" or user_level_lowercase=="junior"\
        or user_level_lowercase=="senior":
            break
            
     #Logic if the user is a freshman or a sophomore   
    if user_level_lowercase=="freshman" or user_level_lowercase=="sophomore":
        #Check if user is in college of engineering
        engineer= \
        input("Are you admitted to the College of Engineering (yes/no): ")
        engineer_lowercase= engineer.lower()
        #if reponse isn't yes, then it is automatically no.
        if engineer_lowercase!="yes":
            engineer_lowercase="no"
        #If user isn't in engineering, ask if in james madison
        if engineer_lowercase=="no":
            james_madison= \
            input("Are you in the James Madison College (yes/no): ")
            james_madison_lowercase= james_madison.lower()
    
    #Logic if user is a junior or a senior
    if user_level_lowercase=="junior" or user_level_lowercase=="senior":
        #Ask for the user's college
        user_college= \
        input("Enter college as business, engineering, health, sciences, or none: ")
        user_college_lowercase= user_college.lower()
        #Ask if user's major is CMSE
        cmse= \
        input("Is your major CMSE " + \
              '(“Computational Mathematics and Engineering”) ' + \
              "(yes/no): ")
        cmse_lowercase= cmse.lower()
        #if response isn't yes, it is automatically no
        if cmse_lowercase!="yes":
            cmse_lowercase="no"
        #If user are in none of the previous colleges, ask if in james madison
        if user_college_lowercase!="business" and \
        user_college_lowercase!="health"\
        and user_college_lowercase!="engineering" and user_college_lowercase!=\
        "health" and user_college_lowercase!= "sciences":
            james_madison= \
            input("Are you in the James Madison College (yes/no): ")
            james_madison_lowercase= james_madison.lower()
            user_college=None
  
    #Ask user how many credits do they have
    credits_=input("Credits: ")
    user_credits_digits= credits_.isdigit()
    type_credits= type(credits_)
    user_credits= int(credits_)
    
    #Check if response is a number, if not, print error message
    while user_credits_digits==False:
        print("Invalid input. Try again.")
        credits_= input("Credits: ")
        user_credits_digits= credits_.isdigit()
        #If reponse is digit, convert response to integer and break loop
        if user_credits_digits==True:
            user_credits=int(credits_)
            break
    
    
    while user_credits<0 or user_credits==0: #Check if credits is 0 or less
        print("Invalid input. Try again.") #Print error message
        credits_=input("Credits: ") #Ask question again
        user_credits_digits= credits_.isdigit()
        if user_credits_digits==True:
          user_credits= int(credits_)
        if user_credits>0 or type_credits=="int": #If more than 0 break loop
            break
    
    
    if user_level_lowercase=="freshman": #logic if user is freshman
        asmsu_tax= 21.00
        fm_radio_tax= 3.00
        state_news_tax= 5.00
        james_madison_tax= 7.50
        #Check if credits are in between 1 and 11 for tuition calculation
        if (user_credits==1 or user_credits>1) and (user_credits==11 or \
           user_credits<11) and user_residency_lowercase=="yes":
            tuition= (482.00 * user_credits) + asmsu_tax+ fm_radio_tax
            #Check if engineer and credits are 4 or less for fee charge
            if engineer_lowercase=="yes" and (user_credits<4 or user_credits==4):
              engineer_fee= 402.00
              james_madison_lowercase=None
              tuition= tuition + engineer_fee
            #If credits are 6 or more, charge state new's tax
            if user_credits==6 or user_credits>6:
              tuition= tuition + state_news_tax
            #If user is in james madison, charge james madison tax
            if james_madison_lowercase=="yes":
              tuition= tuition + james_madison_tax
        #Check if credits are between 12 and 18 for tuition calculation
        elif (user_credits==12 or user_credits>12) and (user_credits==18 or \
             user_credits<18) and user_residency_lowercase=="yes":
            tuition= 7230.00 + asmsu_tax + fm_radio_tax + state_news_tax
            #if engineer, charge engineering fee
            if engineer_lowercase=="yes":
              engineer_fee= 670.00
              james_madison_lowercase=None
              tuition= tuition + engineer_fee
            #if james madison, charge james madison tax
            if james_madison_lowercase=="yes":
              tuition= tuition + james_madison_tax
            #Check is credits are more than 18
        elif user_credits>18 and user_residency_lowercase=="yes":
            tuition= 7230.00 + (482.00*(user_credits-18)) \
            + asmsu_tax + fm_radio_tax + state_news_tax
            # If engineer, charge engineering fee
            if engineer_lowercase=="yes":
              engineer_fee= 670.00
              james_madison_lowercase=None
              tuition= tuition + engineer_fee
            #if james madison, charge james madison tax
            if james_madison_lowercase=="yes":
              tuition= tuition + james_madison_tax
              
        # Repeat same logic but now for non-residents so only the rates change
        while user_residency_lowercase=="no":
            if (user_credits==1 or user_credits>1) and \
        (user_credits==11 or user_credits<11) and user_residency_lowercase=="no":
                tuition= (1325.00 * user_credits) + asmsu_tax + fm_radio_tax
                #Because non-resident, ask if international and charge fee 
                if international_lowercase=="yes":
                  international_fee= 375.00
                  tuition= tuition + international_fee
                if engineer_lowercase=="yes" \
                and (user_credits<4 or user_credits==4):
                  engineer_fee= 402.00
                  james_madison_lowercase=None
                  tuition= tuition + engineer_fee
                if user_credits==6 or user_credits>6:
                  tuition= tuition + state_news_tax
                if james_madison_lowercase=="yes":
                  tuition= tuition + james_madison_tax
            elif (user_credits==12 or user_credits>12) and \
        (user_credits==18 or user_credits<18) \
        and user_residency_lowercase=="no":
                tuition= 19883.00 + asmsu_tax + fm_radio_tax+ state_news_tax
                if international_lowercase=="yes":
                  international_fee= 750.00
                  tuition= tuition + international_fee
                if engineer_lowercase=="yes":
                  engineer_fee= 670.00
                  james_madison_lowercase=None
                  tuition= tuition + engineer_fee
                if james_madison_lowercase=="yes":
                  tuition= tuition + james_madison_tax
            elif user_credits>18 and user_residency_lowercase=="no":
                tuition= 19883.00 + (1325.00 * (user_credits-18)) \
                + asmsu_tax+ fm_radio_tax+ state_news_tax
                if international_lowercase=="yes":
                  international_fee= 670.00
                  tuition= tuition + international_fee
                if engineer_lowercase=="yes":
                  engineer_fee=670.00
                  james_madison_lowercase=None
                  tuition= tuition + engineer_fee
                if james_madison_lowercase=="yes":
                  tuition= tuition + james_madison_tax
            else:
                None
            #After calculating tuition, break the loop
            break
    
    #Repeat same logic for sophomore but some rates are different 
    if user_level_lowercase=="sophomore":
        asmsu_tax= 21.00
        fm_radio_tax= 3.00
        state_news_tax= 5.00
        james_madison_tax= 7.50
        if (user_credits==1 or user_credits>1) and (user_credits==11 or \
           user_credits<11) and user_residency_lowercase=="yes":
            tuition= (494.00 * user_credits) + asmsu_tax+ fm_radio_tax
            if engineer_lowercase=="yes" \
            and (user_credits<4 or user_credits==4):
              engineer_fee= 402.00
              james_madison_lowercase=None
              tuition= tuition + engineer_fee
            if user_credits==6 or user_credits>6:
              tuition= tuition + state_news_tax
            if james_madison_lowercase=="yes":
              tuition= tuition + james_madison_tax
        elif (user_credits==12 or user_credits>12) and (user_credits==18 or \
             user_credits<18) and user_residency_lowercase=="yes":
            tuition= 7410.00 + asmsu_tax + fm_radio_tax + state_news_tax
            if engineer_lowercase=="yes":
              engineer_fee= 670.00
              james_madison_lowercase=None
              tuition= tuition + engineer_fee
            if james_madison_lowercase=="yes":
              tuition= tuition + james_madison_tax
        elif user_credits>18 and user_residency_lowercase=="yes":
            tuition= 7410.00 + (494.00*(user_credits-18)) \
            + asmsu_tax + fm_radio_tax + state_news_tax
            if engineer_lowercase=="yes":
              engineer_fee= 670.00
              james_madison_lowercase=None
              tuition= tuition + engineer_fee
            if james_madison_lowercase=="yes":
              tuition= tuition + james_madison_tax
        while user_residency_lowercase=="no":
            if (user_credits==1 or user_credits>1) and \
        (user_credits==11 or user_credits<11) \
        and user_residency_lowercase=="no":
                tuition= (1325.50 * user_credits) + asmsu_tax + fm_radio_tax
                if international_lowercase=="yes":
                  international_fee= 375.00
                  tuition= tuition + international_fee
                if engineer_lowercase=="yes" \
                and (user_credits<4 or user_credits==4):
                  engineer_fee= 402.00
                  james_madison_lowercase=None
                  tuition= tuition + engineer_fee
                if user_credits==6 or user_credits>6:
                  tuition= tuition + state_news_tax
                if james_madison_lowercase=="yes":
                  tuition= tuition + james_madison_tax
            elif (user_credits==12 or user_credits>12) and \
        (user_credits==18 or user_credits<18) \
        and user_residency_lowercase=="no":
                tuition= 19883.00 + asmsu_tax + fm_radio_tax+ state_news_tax
                if international_lowercase=="yes":
                  international_fee= 750.00
                  tuition= tuition + international_fee
                if engineer_lowercase=="yes":
                  engineer_fee= 670.00
                  james_madison_lowercase=None
                  tuition= tuition + engineer_fee
                if james_madison_lowercase=="yes":
                  tuition= tuition + james_madison_tax
            elif user_credits>18 and user_residency_lowercase=="no":
                tuition= 19883.00 + (1325.50 * (user_credits-18)) \
                + asmsu_tax+ fm_radio_tax+ state_news_tax
                if international_lowercase=="yes":
                  international_fee= 750.00
                  tuition= tuition + international_fee
                if engineer_lowercase=="yes":
                  engineer_fee=670.00
                  james_madison_lowercase=None
                  tuition= tuition + engineer_fee
                if james_madison_lowercase=="yes":
                  tuition= tuition + james_madison_tax
            else:
                None
            break
    
    #Logic for if user is a junior or senior
    #Same steps for calculation like freshman and sophomore
    #But there are more colleges for juniors and seniors
    #And there are different rates
    if user_level_lowercase=="junior" or user_level_lowercase=="senior":
        asmsu_tax= 21.00
        fm_radio_tax= 3.00
        state_news_tax= 5.00
        james_madison_tax= 7.50
        if (user_credits==1 or user_credits>1) and (user_credits==11 or \
           user_credits<11) and user_residency_lowercase=="yes":
            tuition= (555.00 * user_credits) + asmsu_tax+ fm_radio_tax
            #If user's college is sciences, check credits for fee
            if user_college_lowercase=="sciences":
                james_madison_lowercase=None
            #Check fee charge if credits are 4 or less
                if user_credits<4 or user_credits==4:
                    sciences_fee= 50.00
                    tuition= tuition + sciences_fee
                #If credits are more than 4, give higher fee charge
                else:
                    sciences_fee= 100.00
                    tuition= tuition + sciences_fee
            #Check if user college is health, check for credits fee
            if user_college_lowercase=="health":
                james_madison_lowercase=None
                #If credits are 4 or less, give health fee
                if user_credits<4 or user_credits==4:
                    health_fee= 50.00
                    tuition= tuition + health_fee
                #If credits are more than 4, give higher fee charge
                else:
                    health_fee= 100.00
                    tuition= tuition + health_fee
            #Check if user college is business
            if user_college_lowercase=="business":
                #Caluclate new tuition charge for business students
                tuition = (573.00 * user_credits) + asmsu_tax + fm_radio_tax
                james_madison_lowercase= None
                #If credits are 4 or less, give business fee charge
                if user_credits<4 or user_credits==4:
                    business_fee=113.00
                    tuition= tuition + business_fee
                #If credits are more than 4, give higher fee charge
                else:
                    business_fee=226.00
                    tuition= tuition + business_fee
            #Check is user is in engineering
            if user_college_lowercase=="engineering":
                #Calculate new tuition for engineering students
                tuition= (573.00 * user_credits) + asmsu_tax + fm_radio_tax
                james_madison_lowercase=None
                #If credis are 4 or less, give engineering fee charge
                if user_credits<4 or user_credits==4:
                    engineer_fee= 402.00
                    tuition= tuition + engineer_fee
                #If credits are more than 4, give higher fee charge
                else:
                    engineer_fee=670.00
                    tuition= tuition + engineer_fee
            #If credits are more than 6, give state news tax
            if user_credits==6 or user_credits>6:
              tuition= tuition + state_news_tax
            #If user is in james madison, give james madison tax
            if james_madison_lowercase=="yes":
              tuition= tuition + james_madison_tax
            #If user's major is CMSE, check for fee charge
            if cmse_lowercase=="yes":
                #If credits are 4 or less, give cmse fee charge
                if user_credits<4 or user_credits==4:
                    cmse_fee= 402.00
                    tuition= tuition + cmse
                #if credits are more than 4, give higher fee charge
                else:
                    cmse_fee=670.00
                    tuition= tuition + cmse_fee
        #Check if user credits are between 12 and 18.
        #Repeat same calculation steps and ensure the right fee charges
        elif (user_credits==12 or user_credits>12) and (user_credits==18 or \
             user_credits<18) and user_residency_lowercase=="yes":
            tuition= 8325.00 + asmsu_tax + fm_radio_tax + state_news_tax
            if user_college_lowercase=="sciences":
                sciences_fee= 100.00
                tuition= tuition + sciences_fee
                james_madison_lowercase= None
            if user_college_lowercase=="health":
                health_fee= 100.00
                tuition= tuition + health_fee
                james_madison_lowercase=None
            if user_college_lowercase=="business":
              business_fee= 226.00
              james_madison_lowercase= None
              tuition= 8595.00 + business_fee + asmsu_tax + fm_radio_tax \
              + state_news_tax
            if user_college_lowercase=="engineering":
              engineer_fee= 670.00
              james_madison_lowercase=None
              tuition= 8595.00 + engineer_fee + asmsu_tax + fm_radio_tax \
              + state_news_tax
            if james_madison_lowercase=="yes":
              tuition= tuition + james_madison_tax
            if cmse_lowercase=="yes":
                cmse_fee= 670.00
                tuition= tuition + cmse_fee
        #Check if user credits are more than 18
        #Repeat same calculation steps and ensure the right fee charges
        elif user_credits>18 and user_residency_lowercase=="yes":
            #new tuition cost for users with more than 18 credits
            tuition= 8325.00 + (555.00*(user_credits-18)) + asmsu_tax + \
            fm_radio_tax + state_news_tax
            if user_college_lowercase=="sciences":
                sciences_fee= 100.00
                tuition= tuition + sciences_fee
                james_madison_lowercase= None
            if user_college_lowercase=="health":
                health_fee= 100.00
                tuition= tuition + health_fee
                james_madison_lowercase=None
            if user_college_lowercase=="business":
              business_fee= 226.00
              james_madison_lowercase=None
              tuition= 8595.00 + (573.00*(user_credits-18)) + asmsu_tax+ \
              fm_radio_tax+ state_news_tax+ business_fee
            if user_college_lowercase=="engineering":
              engineer_fee= 670.00
              james_madison_lowercase=None
              tuition= 8595.00 + (573.00*(user_credits-18))+asmsu_tax+ \
              + fm_radio_tax+ state_news_tax+ engineer_fee
            if james_madison_lowercase=="yes":
              tuition= tuition + james_madison_tax
            if cmse_lowercase=="yes":
                cmse_fee= 670.00
                tuition= tuition + cmse_fee
        #Tuition cost for non-residents
        #Repeat same calculation steps but the tuition charge will change
        while user_residency_lowercase=="no":
            if (user_credits==1 or user_credits>1) and \
        (user_credits==11 or user_credits<11) \
        and user_residency_lowercase=="no":
                tuition= (1366.75 * user_credits) + asmsu_tax + fm_radio_tax
                if user_college_lowercase=="sciences":
                    james_madison_lowercase=None
                    if user_credits<4 or user_credits==4:
                        sciences_fee= 50.00
                        tuition= tuition + sciences_fee
                    else:
                        sciences_fee= 100.00
                        tuition= tuition + sciences_fee
                if user_college_lowercase=="health":
                    james_madison_lowercase=None
                    if user_credits<4 or user_credits==4:
                        health_fee= 50.00
                        tuition= tuition + 50.00
                    else:
                        health_fee= 100.00
                        tuition= tuition + health_fee
                if user_college_lowercase=="business":
                    tuition= (1385.75 * user_credits) + asmsu_tax + fm_radio_tax
                    james_madison_lowercase=None
                    if user_credits<4 or user_credits==4:
                        business_fee= 113.00
                        tuition= tuition + business_fee
                    else:
                        business_fee= 226.00
                        tuition= tuition + business_fee
                if user_college_lowercase=="engineering":
                    tuition= (1385.75 * user_credits) + asmsu_tax + fm_radio_tax
                    james_madison_lowercase=None
                    if user_credits<4 or user_credits==4:
                        engineer_fee= 402.00
                        tuition= tuition + engineer_fee
                    else:
                        engineer_fee= 670.00
                        tuition= tuition + engineer_fee
                if user_credits==6 or user_credits>6:
                  tuition= tuition + state_news_tax
                if james_madison_lowercase=="yes":
                  tuition= tuition + james_madison_tax
                if international_lowercase=="yes":
                  international_fee= 375.00
                  tuition= tuition + international_fee
                if cmse_lowercase=="yes":
                    if user_credits<4 or user_credits==4:
                        cmse_fee= 402.00
                        tuition= tuition + cmse_fee
                    else:
                        cmse_fee= 670.00
                        tuition= tuition + cmse_fee
            elif (user_credits==12 or user_credits>12) and \
        (user_credits==18 or user_credits<18) and user_residency_lowercase=="no":
                tuition= 20501.00 + asmsu_tax + fm_radio_tax+ state_news_tax
                if user_college_lowercase=="sciences":
                    sciences_fee= 100.00
                    tuition= tuition + sciences_fee
                    james_madison_lowercase= None
                if user_college_lowercase=="health":
                    health_fee= 100.00
                    tuition= tuition + health_fee
                    james_madison_lowercase=None
                if user_college_lowercase=="business":
                  business_fee=226.00
                  james_madison_lowercase=None
                  tuition= 20786.00 + asmsu_tax+ fm_radio_tax + \
                  state_news_tax+ business_fee
                if user_college_lowercase=="engineering":
                  engineer_fee= 670.00
                  james_madison_lowercase=None
                  tuition= 20786.00 + asmsu_tax+ fm_radio_tax+ \
                  state_news_tax+ engineer_fee
                if james_madison_lowercase=="yes":
                  tuition= tuition + james_madison_tax
                if international_lowercase=="yes":
                  international_fee= 750.00
                  tuition= tuition + international_fee
                if cmse_lowercase=="yes":
                    cmse_fee= 670.00
                    tuition= tuition + cmse_fee
            elif user_credits>18 and user_residency_lowercase=="no":
                tuition= 20501.00 + (1366.75 * (user_credits-18)) + asmsu_tax+\
                fm_radio_tax+ state_news_tax
                if user_college_lowercase=="sciences":
                    sciences_fee= 100.00
                    tuition= tuition + sciences_fee
                    james_madison_lowercase= None
                if user_college_lowercase=="health":
                    health_fee= 100.00
                    tuition= tuition + health_fee
                    james_madison_lowercase=None
                if user_college_lowercase=="business":
                  business_fee=226.00
                  james_madison_lowercase=None
                  tuition= 20786.00 + (1385.75*(user_credits-18))+ asmsu_tax+ \
                  fm_radio_tax+ state_news_tax+ business_fee
                if user_college_lowercase=="engineering":
                  engineer_fee=670.00
                  james_madison_lowercase=None
                  tuition= 20786.00+ (1385.75*(user_credits-18))+ asmsu_tax +\
                  fm_radio_tax+ state_news_tax + engineer_fee
                if james_madison_lowercase=="yes":
                  tuition= tuition + james_madison_tax
                if international_lowercase=="yes":
                  international_fee= 750.00
                  tuition= tuition + international_fee
                if cmse_lowercase=="yes":
                    cmse_fee= 670.00
                    tuition= tuition + cmse_fee
                else:
                    None
                break
    
    #Print the user's tuition cost
    print("Tuition is $"+format(tuition,",.2f") + ".")
    
    #Ask if the user would like another calculation
    calculation= input("Do you want to do another calculation (yes/no): ")
    calculation_lowercase= calculation.lower()
    #if user says no, break the loop and the code ends
    if calculation_lowercase=="no":
        break