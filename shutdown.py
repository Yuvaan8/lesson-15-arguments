def shutdown(user_input):
    if user_input == 'Yes':
        print('Shutting down...')
    elif user_input == 'No':
        print('stopping shutdown')
    else:
        print('Sorry')
choice = input('Shutdown? Yes or No:')
shutdown(choice)
    


    

