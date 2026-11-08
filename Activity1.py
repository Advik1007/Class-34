total_chores =4
orignal_count =total_chores
print(f"You have {orignal_count} chores to finish today!\n")
completed_count =0
chore_num = 1
while chore_num <= total_chores:
    if chore_num   ==1: next_chore ="Make Your Bed"
    elif chore_num ==2: next_chore ="Feed The Pet"
    elif chore_num ==3: next_chore="Take Out The Trash"
    else: next_chore="Wash The Dishes"
    answer=input(f"Have You Finished{next_chore}? (Yes/No)")  
    if answer=="yes":
        completed_count +=1
        chore_num += 1
        print("Great Job? Chore Completed.")
    else:
        print("Okay,finish it and check again!")
    print("Chores Remaining:",total_chores - completed_count )
    print()

print("========= ALL CHORES COMPLETE============")
print("Great work finishing your entire checklist today!\n")
print("Now lets safely [eek at an infinite loop ........")
test_value =0
safety_counter =0
while test_value <=0:
    print("This Condition Never changes ,so this would run forever!")
    safety_counter+=1
    if safety_counter ==3:
        print("(Stoping here on purpose  - a real infinite loop never stops on its own!)")
        break
    print("\n======CHORE CHECKLIST SUMMARY==========")
    print("Chores Assigned Today:" ,orignal_count)
    print("Chores Completed:", completed_count)
    print("Chores Remaining:",total_chores-completed_count)
    print("================================================================")
