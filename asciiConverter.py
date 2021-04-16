import math

from PIL import Image

table_point = [
	"⠀", "⠁", "⠂", "⠃", "⠄", "⠅", "⠆", "⠇", "⠈", "⠉", "⠊", "⠋", "⠌", "⠍", "⠎", "⠏",
	"⠐", "⠑", "⠒", "⠓", "⠔", "⠕", "⠖", "⠗", "⠘", "⠙", "⠚", "⠛", "⠜", "⠝", "⠞", "⠟",
	"⠠", "⠡", "⠢", "⠣", "⠤", "⠥", "⠦", "⠧", "⠨", "⠩", "⠪", "⠫", "⠬", "⠭", "⠮", "⠯",
	"⠰", "⠱", "⠲", "⠳", "⠴", "⠵", "⠶", "⠷", "⠸", "⠹", "⠺", "⠻", "⠼", "⠽", "⠾", "⠿",
	"⡀", "⡁", "⡂", "⡃", "⡄", "⡅", "⡆", "⡇", "⡈", "⡉", "⡊", "⡋", "⡌", "⡍", "⡎", "⡏",
	"⡐", "⡑", "⡒", "⡓", "⡔", "⡕", "⡖", "⡗", "⡘", "⡙", "⡚", "⡛", "⡜", "⡝", "⡞", "⡟",
	"⡠", "⡡", "⡢", "⡣", "⡤", "⡥", "⡦", "⡧", "⡨", "⡩", "⡪", "⡫", "⡬", "⡭", "⡮", "⡯",
	"⡰", "⡱", "⡲", "⡳", "⡴", "⡵", "⡶", "⡷", "⡸", "⡹", "⡺", "⡻", "⡼", "⡽", "⡾", "⡿",
	"⢀", "⢁", "⢂", "⢃", "⢄", "⢅", "⢆", "⢇", "⢈", "⢉", "⢊", "⢋", "⢌", "⢍", "⢎", "⢏",
	"⢐", "⢑", "⢒", "⢓", "⢔", "⢕", "⢖", "⢗", "⢘", "⢙", "⢚", "⢛", "⢜", "⢝", "⢞", "⢟",
	"⢠", "⢡", "⢢", "⢣", "⢤", "⢥", "⢦", "⢧", "⢨", "⢩", "⢪", "⢫", "⢬", "⢭", "⢮", "⢯",
	"⢰", "⢱", "⢲", "⢳", "⢴", "⢵", "⢶", "⢷", "⢸", "⢹", "⢺", "⢻", "⢼", "⢽", "⢾", "⢿",
	"⣀", "⣁", "⣂", "⣃", "⣄", "⣅", "⣆", "⣇", "⣈", "⣉", "⣊", "⣋", "⣌", "⣍", "⣎", "⣏",
	"⣐", "⣑", "⣒", "⣓", "⣔", "⣕", "⣖", "⣗", "⣘", "⣙", "⣚", "⣛", "⣜", "⣝", "⣞", "⣟",
	"⣠", "⣡", "⣢", "⣣", "⣤", "⣥", "⣦", "⣧", "⣨", "⣩", "⣪", "⣫", "⣬", "⣭", "⣮", "⣯",
	"⣰", "⣱", "⣲", "⣳", "⣴", "⣵", "⣶", "⣷", "⣸", "⣹", "⣺", "⣻", "⣼", "⣽", "⣾", "⣿"
]

char_travel = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (0, 3), (1, 3)]

# char_range = " ░▒▓█"
char_range = " .,:;/*O0@"

emojis = [
	["⬜", (255, 255, 255)],
	["⬛", (0, 0, 0)],
#	["📰", (122, 122, 122)],
	["🔴", (122, 0, 0)],
	["👛", (122, 0, 122)],
	["🔵", (0, 0, 122)],
	["⛎", (0, 122, 122)],
	["✅", (0, 122, 0)],
	["🌕", (122, 122, 0)],
]


def ascii_convert_point(size, img: Image, split=256/2):
	result = ""
	img = img.resize((size[0] * 2, size[1] * 4))

	for y in range(size[1]):
		for x in range(size[0]):
			char = 0
			for charIndex in range(len(char_travel)):
				pixel = img.getpixel((x * 2 + char_travel[charIndex][0], y * 4 + char_travel[charIndex][1]))
				if pixel >= split:
					char += 2 ** charIndex
			result += table_point[char]
		result += "\n"

	print(result)


def ascci_convert(size, img: Image):
	result = ""
	img = img.resize(size)

	for y in range(size[1]):
		for x in range(size[0]):
			pixel = img.getpixel((x, y))
			char = int(round(pixel * (len(char_range) - 1) / 255, 0))
			result += char_range[char]
		result += "\n"

	print(result)


def ascii_convert_color(size, img: Image):
	result = ""
	img = img.resize(size)

	for y in range(size[1]):
		for x in range(size[0]):
			pixel = img.getpixel((x, y))
			char = -1
			char_diff = 0
			for cur_emoji in emojis:
				diff = 0
				for i in range(3):
					diff += abs(pixel[i] - cur_emoji[1][i])
				diff /= 3
				if diff < char_diff or char == -1:
					char = cur_emoji[0]
					char_diff = diff
			result += char
		result += "\n"

	print(result)

