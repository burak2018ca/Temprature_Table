from termcolor import colored


def TableValues():

    TempArr = [ ]
    WindspeedArr = [ ]

    for x in range(60,-50,-5):
        if(x >= 5):
            WindspeedArr.append(x)
        
        if(x <= 40):
            TempArr.append(x)

    return TempArr,WindspeedArr

def WindChillTable (arr):

    Temprature = arr[0]
    Windspeed = arr[1]

    for x in range (len(Windspeed)-1, 0, -1):
        for y in range(0,len(Temprature)):
            
            WindChill = 35.74 + 0.6215*Temprature[y] - 35.75 * (Windspeed[x] ** 0.16) + 0.4275*Temprature[y] * (Windspeed[x] ** 0.16)

            answer = str(round(WindChill))  

            if(Temprature[y] == 40):
                print(colored(f"\n {answer}  ", 'red'), end =' ') 
            else:
                print(f" {answer}   ", end =' ')




def Main():
    
    Arrays = TableValues()
    WindChillTable(Arrays)

Main()
