def one_Away(str1,str2):
    def check(short,long):
        change_rate = 0
        for i in range(len(long)):
            if long[i] != short[i]:
                change_rate +=1
        return change_rate



    if len(str1) > len(str2):
        return check(str2,str1)
    else:
        return check(str1,str2)


str1 = "akin"
str2 = "akiN"
print(one_Away(str1,str2))