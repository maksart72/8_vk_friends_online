import getpass
import vk


APP_ID = 6122676


def get_user_login():
    your_username = input('Enter username:')
    return your_username


def get_user_password():
    your_password = getpass.getpass('Enter password:')
    return your_password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope="friends"
    )
    api = vk.API(session)
    online_friends_ids = api.friends.getOnline()
    friends_online = api.users.get(user_ids=online_friends_ids,
                                   fields=['last_name', 'first_name'])
    return friends_online


def output_friends_to_console(friends_online):
    print('Online:', len(friends_online))
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password)
    except vk.exceptions.VkAuthError as error:
        print(error)
    else:
        output_friends_to_console(friends_online)
