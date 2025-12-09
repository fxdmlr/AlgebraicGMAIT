import os
import gamerunner as gr
import gamehandler as gh

def static(prechoice=None):
    
    if prechoice is not None:
        choice = prechoice
    print("\n")
    if prechoice is None:
        choice = input("Enter the desired mode :\n0-Quit\n1-CalcGame\n2-IntegralSet\n3-Shuffle\n")
        if not isinstance(choice, int):
            if choice == 'q':
                inpt_dict = {'moe' : 0.1}
                stats = gr.general_runner(gh.calc_game, (0, 10), inpt_dict, 1)#multgame.regMulGameDig(number_of_rounds=rounds, digits=a)
                print("Score : ", round(stats[0]))
                print("Total time spent : ", round(stats[1]))
                print("Time spent per item : ", round(stats[2]))
            elif choice == 'a':
                inpt_dict = {'moe' : 0.1}
                stats = gr.general_runner(gh.integral_set_game, (0, 10), inpt_dict, 1)#multgame.regMulGameDig(number_of_rounds=rounds, digits=a)
                print("Score : ", round(stats[0]))
                print("Total time spent : ", round(stats[1]))
                print("Time spent per item : ", round(stats[2]))
            
            elif choice == 'z':
                inpt_dict = {'moe' : 0.1}
                stats = gr.general_runner(gh.shuffle, (0, 10), inpt_dict, 1)#multgame.regMulGameDig(number_of_rounds=rounds, digits=a)
                print("Score : ", round(stats[0]))
                print("Total time spent : ", round(stats[1]))
                print("Time spent per item : ", round(stats[2]))
        choice = int(choice)
    
    if choice == 1:
        md = int(input("Mode :\n 1-Static\n 2-Dynamic\n"))
        roundd = int(input("Number of rounds : ")) 
        t = 0
        if md == 2:
            t = int(input("Duration : "))
        rounds = (t, roundd)
        moe = float(input('Margin of error : '))
        inpt_dict = {'moe' : moe}
        stats = gr.general_runner(gh.calc_game, rounds, inpt_dict, md)#multgame.regMulGameDig(number_of_rounds=rounds, digits=a)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
        
    if choice == 2:
        md = int(input("Mode :\n 1-Static\n 2-Dynamic\n"))
        roundd = int(input("Number of rounds : ")) 
        t = 0
        if md == 2:
            t = int(input("Duration : "))
        rounds = (t, roundd)
        moe = float(input('Margin of error : '))
        inpt_dict = {'moe' : moe}
        stats = gr.general_runner(gh.integral_set_game, rounds, inpt_dict, md)#multgame.regMulGameDig(number_of_rounds=rounds, digits=a)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
    
    if choice == 3:
        md = int(input("Mode :\n 1-Static\n 2-Dynamic\n"))
        roundd = int(input("Number of rounds : ")) 
        t = 0
        if md == 2:
            t = int(input("Duration : "))
        rounds = (t, roundd)
        moe = float(input('Margin of error : '))
        inpt_dict = {'moe' : moe}
        stats = gr.general_runner(gh.shuffle, rounds, inpt_dict, md)#multgame.regMulGameDig(number_of_rounds=rounds, digits=a)
        print("Score : ", round(stats[0]))
        print("Total time spent : ", round(stats[1]))
        print("Time spent per item : ", round(stats[2]))
   

def run():        
    while True:
        static()
        z = input("Press Enter to continue ...")

if __name__ == '__main__':
    run()