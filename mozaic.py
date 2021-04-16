import math
import os
import random
from PIL import Image
from os import listdir
from os.path import isfile, join
import csv
import time

def dataset_sort(dataset):
	files = listdir(join("./dataset", dataset))
	result_table = []
	i = 0
	start_time = time.time()
	file_count = len(files)
	for cur_file in files:
		img = Image.open("dataset/" + dataset + "/" + cur_file)
		img = img.resize((200, 200))
		mean = get_mean(img)
		result_table.append([mean, cur_file])
		i += 1
		if i % 50 == 0:
			print(str(i) + "/" + str(file_count), ((time.time() - start_time) * (file_count - i) / i) / 60, "m")

	to_csv(result_table, dataset)


def get_mean(img: Image):
	mean = [0, 0, 0]
	pixel_count = 0
	for y in range(img.size[1]):
		for x in range(img.size[0]):
			pixel = img.getpixel((x, y))
			mean = [mean[0] + pixel[0], mean[1] + pixel[1], mean[2] + pixel[2]]
			pixel_count += 1
	mean = (math.floor(mean[0] / pixel_count), math.floor(mean[1] / pixel_count), math.floor(mean[2] / pixel_count))
	#mean2 = img.resize((1, 1)).getpixel((0, 0))
	#print((abs(mean[0]-mean2[0]) + abs(mean[2]-mean2[1]) + abs(mean[2]-mean2[2])) / 3)
	return mean


def to_csv(table, name):
	with open("datasetResult/" + name + ".csv", "w+", newline="") as csv_file:
		writer = csv.writer(csv_file, delimiter=";", quotechar="|", quoting=csv.QUOTE_MINIMAL)
		for row in table:
			writer.writerow([row[0][0], row[0][1], row[0][2], row[1]])


def get_csv(name):
	with open("datasetResult/" + name + ".csv", newline="") as csv_file:
		reader = csv.reader(csv_file, delimiter=";", quotechar="|")
		data = []
		for row in reader:
			data.append([(int(row[0]), int(row[1]), int(row[2])), row[3]])
		return data


def to_mozaic(size, img: Image, dataset_name, result_name, img_size=(30, 30),):
	img = img.resize(size)
	dataset = get_csv(dataset_name)

	result = Image.new("RGB", (size[0] * img_size[0], size[1] * img_size[1]))

	for y in range(size[1]):
		for x in range(size[0]):
			pixel = img.getpixel((x, y))
			img_name = []
			img_diff = 0
			for cur_img in dataset:
				diff = 0
				for i in range(3):
					diff += abs(pixel[i] - cur_img[0][i])
				diff /= 3
				if diff < img_diff or img_name == []:
					img_name.clear()
					img_name.append(cur_img[1])
					img_diff = diff
				elif diff == img_diff:
					img_name.append(cur_img[1])

			cur_img = Image.open("dataset/" + dataset_name + "/" + random.choice(img_name))
			cur_img = cur_img.resize(img_size)
			result.paste(cur_img, (x * img_size[0], y * img_size[1]))

	result.show()
	result.save("result/" + result_name + ".jpeg", "JPEG")

