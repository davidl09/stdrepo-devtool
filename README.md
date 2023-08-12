# stdrepo-devtool
Run this script in the desired parent directory of your new C/C++ project to create a standard folder structure, complete with pre-written cmake files.

(Linux)
1. run the install script
2. done

The generic folder structure looks like this: (click 'view raw file' if it does not display properly) 

{repo name}                                                                                                                                                     
|    |     
|    |build  #miscellaneous cmake/makefiles                                                                                                                  
|    |bin  #compiled binaries are placed here                                                                                                                   
|    |    |{project name} #executable named with project name                                                                                                  
|    |main
|        |include #add your .h / .hpp header files here                                                                                                      
|        |src                                                                                                                                                
|        |   |CMakeLists.txt                                                                                                                             
|        |   |main.c #example hello world program                                                                                                               
|        |                                                                                                                                                   
|        |CMakeLists.txt                                                                                                                                     



To compile the example, or your own code in main/src/ after running the stdrepo command, run the following:                                                     
  $ cd build                                                                                                                                                   
  $ cmake ..                                                                                                                                                   
  $ cd ..                                                                                                                                                       
  $ ./bin/{projectname}
