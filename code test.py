#message_text = input(str('type something'))
#print('your message text is:' + message_text)

def is_word(word):
     if len(word) >= 1:
          return True
     else:
          return False

def __init__(self, text):
       
        self.message_text = input(str('please type a message'))
        #let the user input a message
        if is_word(self.message_text):
            print("valid word" + self.message_text)
            return self.message_text  #check are there any spelling mistakes in message
        
        else:#there are mistakes in message, so the user have to input again
            print("there's an error, type it again")
            return __init__(self, text)
__init__()