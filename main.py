
import secrets
import string

def generatePassword(style="general"):

    # define the alphabet
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    if style=='general':
        alphabet = letters + digits + '-_$#'

        # fix password length
        pwd_length = 16

        # generate password meeting constraints
        while True:
          pwd = ''
          for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))

          if (any(char in special_chars for char in pwd) and
              sum(char in digits for char in pwd)>=2):
                  break
        print(pwd)
    elif style=='mac':
        alphabet = letters+digits
        breakLength = 5
        totalBreaks = 4
        pwd = ''
        for j in range(totalBreaks):
            for i in range(breakLength):
                pwd += ''.join(secrets.choice(alphabet))
            if j<totalBreaks-1:
                pwd += '-'
        print(pwd)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in range(10):
        generatePassword('mac')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
