import os
import shutil
import math


def clean_dataset(dataset_name):
	utility_file = check_files("./dataset/" + dataset_name)
	file_need_remove = os.listdir("./dataset/" + dataset_name)
	i = 0
	for file in utility_file:
		future_name = f"{'0' * (8 - (len(str(i))))}{i}{os.path.splitext(file)[1]}"
		shutil.move(file, "./dataset/" + dataset_name + "/" + future_name)
		i += 1
		print("copy:", file, future_name)
	print("copy finish")
	for file in file_need_remove:
		shutil.rmtree("./dataset/" + dataset_name + "/" + file)
		print("remove:", file)
	print("clean finish")


def check_files(path, extensions=None):
	if extensions is None:
		extensions = [".png", ".jpeg", ".jpg"]
	files = os.listdir(path)
	utility_file = []
	for file in files:
		if os.path.isfile(os.path.join(path, file)):
			name, extension = os.path.splitext(os.path.join(path, file))
			keep = False
			for cur_extension in extensions:
				if extension == cur_extension:
					keep = True
					break
			if keep:
				utility_file.append(os.path.join(path, file))
		else:
			utility_file += check_files(os.path.join(path, file), extensions)

	return utility_file
