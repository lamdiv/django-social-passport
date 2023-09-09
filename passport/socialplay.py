SOCIAL_PLATFORMS = [
    'Facebook',
    'Google',
    'Twitter'
]

def socialhi():
    print()
    name = input("What Shoul I Call You? ")
    available_platforms = ', '.join(SOCIAL_PLATFORMS[:-1]) + ' or ' + SOCIAL_PLATFORMS[-1]

    print()
    print(f'Ok {name}, Nice meeting you! \nAre you available on {available_platforms}?')
    user_response = input('y/n: ')

    print()
    if user_response[0].upper() == 'Y':
        return "Cool! We will allow authentication from them for sure."
    else:
        return "Oops! You have to use email authentication then."

