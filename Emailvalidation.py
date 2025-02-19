# Python Project on Email Validation:

a = " Dear User, Please Enter Your Email ID Below: "
print(a)

b = " Please follow the given conditions before entering the Email ID: "
print(b)

c = " 1. The Length of your email should be greater or equal to 6 characters. "
print(c)

d = " 2. The 1st character of your email should be Alphabet. "
print(d)

e = " 3. The '@' character should be atleast once in your email and should not be more than one time. "
print(e)

f = " 4. The '.' position should be used properly for e.g: use like this - .com or .in "
print(f)

g = " 5. There should not be any space character nor any upper case characters nor any extra special characters like '#' in your Email. "
print(g)

email = input(" Enter your Email ID: ") # g@g.in, muskan@gmail.com

k = 0
j = 0
s = 0

if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        s = 1
                if k == 1 or j == 1 or s == 1:
                    print('Invalid Email Please Try Again, Your 5th Condition is not satisfied.')
                else:
                    print('Your Email is Valid.')
            else:
                print('Invalid Email Please Try Again, Your 4th Condition is not satisfied.')
        else:
            print('Invalid Email Please Try Again, Your 3rd Condition is not satisfied.')
    else:
        print('Invalid Email Please Try Again, Your 2nd Condition is not satisfied.')
else:
    print('Invalid Email Please Try Again, Your 1st Condition is not satisfied.')