def timeConversion(s):
    co_s=int(s[:2])
    if s[-2:]=='PM' and co_s==12:
        return s[:-2]
    if s[-2:]=='PM' and  co_s<=11 :
        new_str = co_s + 12
        return str(new_str)+s[2:len(s)-2]
    if s[-2:]=='AM' and co_s==12:
        return '00'+s[2:len(s)-2]
    else:
        return s[:-2]


if __name__=='__main__':
    print(timeConversion('01:13:45PM'))