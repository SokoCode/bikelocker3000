
def sample_response(input_text):
    user_message = str(input_text).lower()
    
    if user_message in ("lock", "lock bike"):
        return "The bike is locked!"
    
    if user_message in ('unlock', "unlock bike"):
        return 'The bike is unlocked!'
    
    return "Please only use the known commands!"