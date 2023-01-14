# this module check whether username is valid or not

def userId_validition(username):
    message = ""
    status=True
    for single_character in username:
        if ord(single_character) in range (48,58) or ord(single_character) in range (65,91) or ord(single_character) in range (97,123) or ord(single_character)==32:
            continue
        else:
            status=False
            message = "'user id can only contain character or digit'"
            break
    return message, status