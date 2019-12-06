MaxNumber = 100
MinNumber = 0
for i in range(0, 100):
    Average = int((MaxNumber + MinNumber)/2)
    Answer = input('is it {}:\n'.format(Average))
    if Answer == 'h':
        MinNumber = Average
    elif Answer == 'l':
        MaxNumber = Average
    elif Answer == 'y':
        print('wow . well played;)\n')
        break
    else:
        print('please enter the correct character X( :\n')
