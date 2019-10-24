from text import *
from asscii import *
def choice(pg1=0, pg2=0):
    pg1 = str(pg1)
    pg2 = str(pg2)
    while True:
        choice = input("Enter page " + pg1 + " or page " + pg2 + "\n")
        if choice==pg1:
            return pg1
        elif choice == pg2:
            return pg2
        else:
            print("Sorry not an option.")
            continue

pg1a()
#art page 2
pg2Art()
pg2a()

#art page 3
pg3Art()
pg3()
choicex = choice(pg1=6, pg2=5)
if choicex == "6":
    pg6()
elif choicex == "5":
    pg5()
#art page 4
pg4Art()
pg5()
choicex = choice(pg1=8, pg2=9)
if choicex == "8":
    pg8()
elif choicex == "9":
    pg9()
pg6()
choicex = choice(pg1=10, pg2=12)
if choicex == "10":
    pg10()
elif choicex == "12":
    pg12()
pg8()
choicex = choice(pg1=11, pg2=15)
if choicex == "11":
    pg11()
elif choicex == "15":
    pg15()
pg9()
choicex = choice(pg1=16, pg2=14)
if choicex == "16":
    pg16()
elif choicex == "14":
    pg14()
pg10()
choicex = choice(pg1=17, pg2=18)
if choicex == "17":
    pg17()
elif choicex == "18":
    pg18()
pg11()
choicex = choice(pg1=24, pg2=22)
if choicex == "24":
    pg24()
elif choicex == "22":
    pg22()
pg12()
choicex = choice(pg1=21, pg2=19)
if choicex == "21":
    pg21()
elif choicex == "19":
    pg19()
#art page 13
pg13Art()
#art page 14
pg14Art()
pg14()
choicex = choice(pg1=26, pg2=28)
if choicex == "26":
    pg26()
elif choicex == "28":
    pg28()
pg15()
choicex = choice(pg1=23, pg2=27)
if choicex == "23":
    pg23()
elif choicex == "27":
    pg27()
pg16()
choicex = choice(pg1=29, pg2=31)
if choicex == "29":
    pg29()
elif choicex == "31":
    pg31()
pg17()
choicex = choice(pg1=32, pg2=33)
if choicex == "32":
    pg32()
elif choicex == "33":
    pg33()
pg18()
choicex = choice(pg1=34, pg2=37)
if choicex == "34":
    pg34()
elif choicex == "37":
    pg37()
#art page 19
pg19Art()
pg19()#end

#art page 20
pg20Art()
pg21() #end
pg22()
choicex = choice(pg1=38, pg2=35)
if choicex == "38":
    pg38()
elif choicex == "38":
    pg35()
pg23() #end

pg24()
pg6()
#art page 25
pg25Art()
#art page 26
pg26Art()
pg26() #End

pg27()
choicex = choice(pg1=39, pg2=40)
if choicex == "39":
    pg39()
elif choicex == "40":
    pg40()
pg28()
choicex = choice(pg1=41, pg2=42)
if choicex == "41":
    pg41()
elif choicex == "42":
    pg42()
pg29()
choicex = choice(pg1=43, pg2=44)
if choicex == "43":
    pg43()
elif choicex == "44":
    pg44()
#art page 30
pg30Art()
pg31() #end

pg32() #end

pg33()
choicex = choice(pg1=45, pg2=46)
if choicex == "45":
    pg45()
elif choicex == "46":
    pg46()
pg34()
choicex = choice(pg1=48, pg2=47)
if choicex == "48":
    pg48()
elif choicex == "47":
    pg47()
pg35()
choicex = choice(pg1=50, pg2=53)
if choicex == "50":
    pg50()
elif choicex == "53":
    pg53()
#art page 36
pg36Art()
pg37() #end

pg38()
choicex = choice(pg1=55, pg2=51)
if choicex == "55":
    pg55()
elif choicex == "51":
    pg51()
pg3()
choicex = choice(pg1=56, pg2=57)
if choicex == "56":
    pg56()
elif choicex == "57":
    pg57()
pg40()#end

#art page 40
pg40Art()
pg41()
choicex = choice(pg1=58, pg2=59)
if choicex == "58":
    pg58()
elif choicex == "59":
    pg59()
pg42()
pg6()

pg43()
choicex = choice(pg1=60, pg2=61)
if choicex == "60":
    pg60()
elif choicex == "61":
    pg61()
pg44()
choicex = choice(pg1=64, pg2=63)
if choicex == "64":
    pg64()
elif choicex == "63":
    pg63()
#art page 44
pg44Art()
pg45()
choicex = choice(pg1=65, pg2=66)
if choicex == "65":
    pg65()
elif choicex == "66":
    pg66()
pg46()
pg48()
                 
pg47() #ending

pg48()
pg9()
                 
#art page 49
pg49Art()
pg50()
choicex = choice(pg1=67, pg2=68)
if choicex == "67":
    pg67()
elif choicex == "68":
    pg68()
pg51()
choicex = choice(pg1=72, pg2=74)
if choicex == "72":
    pg72()
elif choicex == "74":
    pg74()
#art page 52
pg52Art()
pg53()
choicex = choice(pg1=69, pg2=70)
if choicex == "69":
    pg69()
elif choicex == "70":
    pg70()
#art page 54
pg54Art()
pg55()
choicex = choice(pg1=71, pg2=73)
if choicex == "71":
    pg71()
elif choicex == "73":
    pg73()
pg56()
choicex = choice(pg1=75, pg2=76)
if choicex == "75":
    pg75()
elif choicex == "76":
    pg76()
pg57()
choicex = choice(pg1=77, pg2=79)
if choicex == "77":
    pg77()
elif choicex == "79":
    pg79()
pg58()#end

pg59()#end

#art page 59
pg59Art()
pg60()
choicex = choice(pg1=80, pg2=82)
if choicex == "80":
    pg80()
elif choicex == "82":
    pg82()
pg61()
choicex = choice(pg1=81, pg2=86)
if choicex == "81":
    pg81()
elif choicex == "86":
    pg86()
#art page 63
pg63Art()
pg63()#end

pg64()
choicey = option(pg1=63, pg2=85, pg3=87)
if choicey == "63":
    pg63()
elif choicey == "85":
    pg85()
elif choicey == "87":
    pg87()
pg65()
choicex = choice(pg1=88, pg2=89)
if choicex == "88":
    pg88()
elif choicex == "89":
    pg89()
#art page 66
pg66Art()
pg66()
pg32()
                 
pg67()
pg6()
                 
pg68()#end

pg69()
choicex = choice(pg1=97, pg2=98)
if choicex == "97":
    pg97()
elif choicex == "98":
    pg98()
pg70()
choicex = choice(pg1=99, pg2=100)
if choicex == "99":
	pg99()
elif choicex == "100":
	pg100()
pg71()
choicex = choice(pg1=90, pg2=91)
if choicex == "90":
    pg90()
elif choicex == "91":
    pg91()
pg72()
choicex = choice(pg1=93, pg2=94)
if choicex == "93":
    pg93()
elif choicex == "94":
    pg94()
pg73()#end

#art page 73
pg73Art()
pg74()#end
chch=input("If you don't like this ending turn to page 107\nTurn to page 107\nyes or no?")
chch=chch.title
if chch=="No":
    print("END")
elif chch=="Yes":
    pg107()
pg75()#end

pg76()#end
chch=input("If you don't like this ending turn to page 108\nTurn to page 108\nyes or no?")
chch=chch.title
if chch=="No":
    print("END")
elif chch=="Yes":
    pg108()
pg77()#end

#art page 78
pg78Art()
pg79()
pg50()
                 
pg80()#end

pg81()
choicex = choice(pg1=116, pg2=117)
if choicex == "116":
    pg116()
elif choicex == "117":
    pg117()
pg82()
choicex = choice(pg1=112, pg2=114)
if choicex == "112":
    pg112()
elif choicex == "114":
    pg114()
#art page 83
pg83Art()
#art page 84
pg84Art()
pg85()#end

pg86()#end

pg87()#end

#art page 87
pg87Art()
pg88()
choicex = choice(pg1=95, pg2=96)
if choicex == "95":
    pg95()
elif choicex == "96":
    pg96()
pg89()#end

pg90()
choicex = choice(pg1=101, pg2=102)
if choicex == "101":
    pg101()
elif choicex == "102":
    pg102()
pg91()
choicex = choice(pg1=103, pg2=104)
if choicex == "103":
    pg103()
elif choicex == "104":
    pg104()             
#art page 92()
pg92Art()
pg93()#end

pg94()
choicex = choice(pg1=105, pg2=106)
if choicex == "105":
    pg105()
elif choicex == "106":
    pg106()
pg95()#end

pg96()
chch=input("If you decide to drop out of throught travel and return to earth life, turn to page 110\nTurn to page 110\nyes or no?")
chch=chch.title
if chch=="No":
    print("END")
elif chch=="Yes":
    pg110()
pg97()#end

#page 97 art
pg97Art()
pg98()#end

pg99()#end

pg100()
pg55()

pg101()#end

#art page 102
pg102Art()
pg102()#end

pg103()#end

pg104()#end

pg105()#end

#art page 105
pg105Art()
pg106()#end

#art page 106
pg106Art()
pg107()#end

pg108()
#art page 108
pg108Art()
pg109()#end

#art page 109
pg109Art()
pg110()#end
