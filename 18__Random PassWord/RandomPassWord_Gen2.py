# owner2plusai 
# thanks for watching
# Rand_password_gen_2
import math
import random

alphas = "abcdefghijklmnopqrstuvwxyz"
nums = "0123456789"
char_ = "@#$%&*"

# get length of password
pass_len = int(input("Enter PassWord Length : "))

alphas_len = pass_len // 2
nums_len   = math.ceil(pass_len * 30/100 )
char_len   = pass_len - (alphas_len+nums_len)

pass_word = []


def generate_pass(lenght, array, is_alpha=False):
    for i in range(lenght):
        index = random.randint(0, len(array)-1)
        character = array[index]
        if is_alpha :
            case = random.randint(0,1)
            if case == 1:
                character = character.upper()
        pass_word.append(character)

#alpha pass
generate_pass(alphas_len ,alphas ,True)
# numeric pass
generate_pass(nums_len ,nums )
# char pass
generate_pass(char_len ,char_ )

random.shuffle(pass_word)
gen_password = ""

for i in pass_word:
    gen_password = gen_password + str(i)
    
# show pass_word
print("Your Pass :" , gen_password)
