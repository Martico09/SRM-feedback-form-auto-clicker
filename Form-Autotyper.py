import pyautogui
import time

def auto_key_presser(keys):
    for key in keys:
        if key.lower() == "tab":
            pyautogui.press("tab")
        elif key.lower() == "enter":
            pyautogui.press("enter")
            time.sleep(0.3)
        elif key.lower() == "down":
            pyautogui.press("down")
        elif key.lower() == "space":
            pyautogui.press("space")
        else:
            pyautogui.press(key)

if __name__ == "__main__":
    T_subs = int(input("Total number of theory subjects: "))
    T_crit = int(input("Total number of theory remarks: "))
    P_subs = int(input("Total number of practical subjects: "))
    p_crit = int(input("Total number of practical remarks: "))
#     T_subs = 4
#     T_crit = 14
#     P_subs = 2
#     p_crit = 13
    comment = input("Comment: ")
    remark = int(input("Choose option: {0:Average,1:Excellent,2:Good,3:Poor,4:Very Good}"))
    print("The form will start to autofill in 10 seconds switch to the tab")
    
    key_input = "tab tab tab tab tab"
    comment = " ".join([i for i in comment]).replace("   "," space ")
    comment = " " + comment + " "
    
    menu_press = " enter {} enter tab".format("down "*remark)
    for j in range(T_subs):
        for i in range(T_crit):
                key_input += menu_press
        key_input += comment
        key_input += "tab tab tab"
    key_input += " tab "
    for j in range(P_subs):
        for i in range(p_crit):
                key_input += menu_press
        key_input += comment
        key_input += "tab tab tab"

    
    time.sleep(10)
    keys_to_press = key_input.split()
    auto_key_presser(keys_to_press)
