import pickle
import numpy as np
import cv2

list_of_instructions = [
	'Climb down the ladder',			#0
	'Climb up the ladder',				#1
	'Get the key',						#2
	'Get the sword',					#3
	'Get the torch',					#4
	'Go between the lasers',			#5
	'Go to the bottom of the room',		#6
	'Go to the bottom room',			#7
	'Go to the center of the room',		#8
	'Go to the left room',				#9
	'Go to the left side of the room',	#10
	'Go to the right room',				#11
	'Go to the right side of the room',	#12
	'Go to the top of the room',		#13
	'Go to the top room',				#14
	'Jump to the rope',					#15
	'Use the key',						#16
]

dataset = []

def label_images():

	global dataset

	for i in range(400,600):

		f1 = open('saved/sprite_' + str(i) + '.pickle','rb')
		f2 = open('saved/sprite_' + str(i+1) + '.pickle','rb')

		image1 = pickle.load(f1)
		image2 = pickle.load(f2)

		image1 = image1[:,:,::-1]
		image2 = image2[:,:,::-1]

		both = np.hstack((image1, image2))

		cv2.imshow('image' + str(i),both)
		cv2.waitKey(1000)

		inp = input()

		if inp == 'q':
			
			with open('dataset3.pickle','wb') as f:
				pickle.dump(dataset,f)
			
			break
		elif inp == 'n':
			continue
		else:
			try:
				x = int(inp)
				dataset.append(((image1,image2),list_of_instructions[x]))
			except ValueError:
				print("skipped")

	with open('dataset3.pickle','wb') as f:
		pickle.dump(dataset,f)

#label_images()

def combine():

	f1 = open('dataset1.pickle','rb')
	f2 = open('dataset2.pickle','rb')
	f3 = open('dataset3.pickle','rb')
	f5 = open('dataset7.pickle','rb')
	f6 = open('dataset8.pickle','rb')
	f7 = open('dataset9.pickle','rb')

	l1 = pickle.load(f1)
	l2 = pickle.load(f2)
	l3 = pickle.load(f3)
	l5 = pickle.load(f5)
	l6 = pickle.load(f6)
	l7 = pickle.load(f7)

	print (len(l1))
	print (len(l2))
	print (len(l3))
	print (len(l5))
	print (len(l6))
	print (len(l7))

	l = l1 + l2 + l3 + l5 + l6 + l7

	with open('dataset_true.pickle','wb') as f:
		pickle.dump(l,f)

#combine()
with open('dataset_false.pickle','rb') as f:
	l = pickle.load(f)

for i in range(0,200,20):

	(f1,f2), sent = l[i]

	both = np.hstack((f1, f2))

	print (sent)

	cv2.imshow('image' + str(i),both)
	cv2.waitKey()








