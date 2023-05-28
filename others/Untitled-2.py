import subprocess
# Compile the C++ file
compile_cmd = ["g++", "selectagent.cpp", "-o", "selectagent"]
subprocess.run(compile_cmd, check=True)