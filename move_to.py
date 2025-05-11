import getopt, sys, shutil, os, time

def do_stuff():
    source = r"C:\Users\lnia2\projects\moodle_local\server\moodle\blocks\openai_chat"
    target = r"C:\Users\lnia2\projects\poodle-moodle-chatbot\moodle\plugin"

    print("Trying to remove target")
    shutil.rmtree(target)
    time.sleep(1)
    print("Target removed, trying to recreate directory")
    #os.mkdir(target)
    #print("Directory created, trying to copy tree")
    shutil.copytree(source, target)

print("hehe")
do_stuff()