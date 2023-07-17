import subprocess
compile_cmd = ["g++", r"C:\Users\User\Documents\GitHub\AUTOvalorant\others\selectagent.cpp", "-o", "selectagent"]
subprocess.run(compile_cmd, shell=True, check=True)
# Run the compiled executable with the x and y coordinates as arguments
run_cmd = [r"C:\Users\User\Documents\GitHub\AUTOvalorant\others\selectagent.exe",'999','999','999','999']
subprocess.run(run_cmd, shell=True, check=True)