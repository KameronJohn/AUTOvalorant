import subprocess
import time
time.sleep(2)
others_path = r'C:\Users\kamka\Documents\AUTOvalorant\others'+'\\'
while True:
    # Compile the C++ filwe
    compile_cmd = ["g++", f"{others_path}afk.cpp", "-o", "afk"]
    subprocess.run(compile_cmd, check=True)
    # Run the compiled executable with the x and y coordinates as arguments
    """ drop,shield,abilities """
    run_cmd = [f"{others_path}afk", '0', '0', '0']
    """ drop,shield,abilities """
    subprocess.run(run_cmd, check=True)