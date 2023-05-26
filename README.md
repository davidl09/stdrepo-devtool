# stdrepo-devtool
Run this script in the desired parent directory of your new C/C++ project to create a standard folder structure, complete with pre-written cmake files.

(Linux)
1. Place the script in your home directory's bin/ or .local/bin/ folder.
2. Make sure the bin directory is added to your path. (run >$ echo $(path) to check PATH variables)
3. Open the bin directory in a terminal and run >$ chmod +x stdrepo
4. Call >$ stdrepo from anywhere to create C/CPP project folder structures!

The generic folder structure looks like this: (click 'view raw file' if it does not display properly)

{repo name}
    |
    |build  #miscellaneous cmake/makefiles
    |bin  #compiled binaries are placed here
    |   |{project name} #executable named with project name
    |main
        |include #add your .h / .hpp header files here
        |src
        |   |CMakeLists.txt
        |   |main.c #example hello world program
        |
        |CMakeLists.txt
     
To compile the example, or your own code in main/src/ after running the stdrepo command, run the following:
  >$ cd build
  >$ cmake ..
  >$ cd ..
  >./bin/{projectname}
