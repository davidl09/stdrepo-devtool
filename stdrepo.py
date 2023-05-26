#!/usr/bin/python3

import sys
import os

mode = 0o0770

if len(sys.argv) < 2:
    print("Missing repo name, please enter a name:")
    name = input()

else: name = sys.argv[1]

if len(sys.argv) < 3:
    pname = input("Missing project name, please enter a name:\n")
else: pname = sys.argv[2]

if len(sys.argv) < 4:
	lang = input("Missing language, enter C or CPP to choose.").lower()
else: lang = sys.argv[3].lower()

if lang != "c" and lang != "cpp":
	while lang != "c" and lang != "cpp":
		lang = input("Option not available, enter C or CPP").lower()
		if lang == "c" or lang == "cpp":
			break
	

rootpath = os.getcwd() + "/" + name

binpath = rootpath + "/bin"
mainpath = rootpath + "/main"
buildpath = rootpath + "/build"

mainsrc = mainpath + "/src"
maininc = mainpath + "/include"

paths = [rootpath, binpath, mainpath, buildpath, mainsrc, maininc]

for p in paths:
	os.mkdir(p, mode)
	
cmv = os.popen("cmake --version").read()[14:18]
langstand = "C_STANDARD	17" if lang == "c" else "CXX_STANDARD 23"

#create cmake files
rootcmake = open(rootpath + "/CMakeLists.txt", "w") 
maincmake = open(mainpath + "/CMakeLists.txt", "w")
srccmake = open(mainsrc + "/CMakeLists.txt", "w")
mainexpl = open(mainsrc + f"/main.{lang}", "w")

#write to cmake files
rootcmake.write(f"project({pname})\ncmake_minimum_required(VERSION {cmv})\nset({langstand})\nadd_subdirectory(main)")
maincmake.write(f"add_subdirectory(src)")
srccmake.write("include_directories(${" + pname + "_SOURCE_DIR}/main/include)\n")
srccmake.write("set(EXECUTABLE_OUTPUT_PATH ${" + pname + "_SOURCE_DIR}/bin)\n")
srccmake.write(f"add_executable({pname} main.{lang})")

if lang == "c":
	mainexpl.write("#include <stdio.h>\n\nint main(){\n\tprintf(\"Hello, World!\\n\");\n}\n")
else: mainexpl.write("#include <iostream>\n\nint main(){\n\tstd::cout << \"Hello, World!\" << std::endl;\n}\n")

mainexpl.close()
rootcmake.close()
maincmake.close()
srccmake.close()










