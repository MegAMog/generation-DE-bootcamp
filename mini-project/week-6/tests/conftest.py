import sys, os

#Find absolute path for current py-file
abs_path_current_file=os.path.abspath(__file__)

#Get the project directory
project_dir=os.path.dirname(os.path.dirname(abs_path_current_file))

#Get source directory
source_dir=os.path.join(project_dir, "source")

# Add source folder to sys.path
if source_dir not in sys.path:
    sys.path.insert(0, source_dir)


