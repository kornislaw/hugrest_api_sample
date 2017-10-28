""" A simple API for Sleepy Talkie, a cool project at HackYeay 2017
"""
import hug

users = []

@hug.post(examples=['phone_number=601234567&interests=fajki,kopytka',
                    'phone_number=676543210&interests=zona kolegi Karola,fajki',
                    'phone_number=676233211&interests=kopytka,chomiki'])
@hug.cli()
def add(phone_number: hug.types.text, interests: hug.types.comma_separated_list):
    """ Adds a new user """
    if len([u for u in users if u['phone_number']==phone_number]) == 0:
        users.append({'phone_number': phone_number, 'interests': interests})
        return f'Number {phone_number} added'
    else:
        return f'Number {phone_number} already exists!'


@hug.get()
@hug.cli()
def get_users():
    return users


@hug.get(examples='interests=fajki')
@hug.cli()
def get_users_by_interests(interests: hug.types.text):
    return [u for u in users if interests in u['interests']]


@hug.get(examples='phone_number=601234567')
@hug.cli()
def get_users_by_phone(phone_number: hug.types.text):
    return [u for u in users if u['phone_number']==phone_number]

if __name__ == '__main__':
    add.interface.cli()
