def solution(s):
    ltstring = s
    Camel = []
    for i in range(len(s)):
        j = i + 1
        if (j) < len(s):
            if s[j].isupper():
                Camel.append(j)
            else:
                pass
        new_list = []
        if Camel == []:
            pass
        else:
            for i in range((len(Camel)+1)):
                last_one = len(Camel) - 1
                if i == 0:
                    new_list += [s[0:Camel[0]]]
                elif i == len(Camel):                     
                    new_list += [s[Camel[last_one]:]]       
                else:                                       
                    new_list += [s[Camel[i-1]:Camel[i]]]       
        ltstring = " ".join(new_list)
    return ltstring