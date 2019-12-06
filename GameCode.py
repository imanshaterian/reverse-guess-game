# make a max and min for making the possible area smaler by every step
MaxNumber = 100
MinNumber = 0
print('Hi .This is a guess game. You choose a number between 1 and 100 and i should try to find it.\n
if your number is SMALLER than my guess press "l".\n
if your number is BIGGER than my guess press "h".\n
if i guessed the number right press "y".\n')
for i in range(0, 100):
    # average is the answer that will be printed in every step
    Average = int((MaxNumber + MinNumber)/2)
    Answer = input('is it {}:\n'.format(Average))
    # the higer part
    if Answer == 'h':
        MinNumber = Average
    # the lower part
    elif Answer == 'l':
        MaxNumber = Average
    # the right asnwer part
    elif Answer == 'y':
        print('wow . well played;)\n')
        break
    else:
        print('please enter the correct character X( :\n')
