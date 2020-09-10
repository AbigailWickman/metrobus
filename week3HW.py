def check_users(current_users, new_users):
    pass
    lowerC_us = [l.lower() for l in current_users]
    for new_users in new_users:
        if new_users in lowerC_us:
            print(f"Unfortunately, {new_users} has already been taken. Please choose another username.")
        else:
            print(f"Congratulations, {new_users} is available.")
if __name__ == "__main__":
    current_us = ['chris', 'haritha', 'sally', 'darnell', 'superman']
    new_us = ['george', 'ringo', 'superman', 'hannibal']
    check_users(current_us, new_us)