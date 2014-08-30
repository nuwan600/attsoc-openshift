import random
import math
import pre_process
import json
import collections

class classify_knn:
	"""
		Initialize the classify class.
		* n                       - number of neighbours
		* using_weighted_distance - if the "weighted distance" is used - True, else False
		* weight                  - weight factor for a distance
		* p                       - power of a distance.
	"""
	def __init__(self, n, using_weighted_distance, weight, p):
		self.n = n
		self.words = {}
		self.points = list()
		self.pre_processor = pre_process.pre_process()
		self.weighted_distance = using_weighted_distance
		self.weight = weight
		self.p = p
		
	"""
		Reading a file.
		* name                    - file name
	"""
	def file_read(self, name):
		try:
			f = open(name, 'r')
		except IOError:
			print "ERROR : '", name, "' is missing"
			exit(0)
		en = f.read().splitlines()
		return en
		
	"""
		Get the word lest of a given set of strings
		* questions               - set of strings
	"""
	def get_all_words(self, questions):
		for question in questions:
			wd_list = self.pre_processor.preprocess(question)
			for wd in wd_list:
				self.words[wd] = 1
		
	"""
		Remove duplicates in a point list.
		* list                    - the point list                
	"""
	def remove_duplicates(self, list):
		d = {}
		for l in list:
			d[str(l)] = l
			
		return [d[key] for key in d.keys()]
	
	"""
		update point list for a question list in given category.
		* list                    - the point list                
	"""
	def train(self, cat, questions):
		for question in questions:
			wd_list = self.pre_processor.preprocess(question)
			point = list()
			sq_sum = 0.0
			for wd in self.words.keys():
				num = wd_list.get(wd, 0)
				point.append(num);
				sq_sum = sq_sum + num * num
				
			sq_sum = math.sqrt(sq_sum)
			
			for i in range(0, len(point)):
				point[i] = point[i] / sq_sum
				
			self.points.append((point, cat))
	
		self.points = self.remove_duplicates(self.points)
		
	"""
		find the similarity of a given two vectors.
		* point1                  - vector 1  
		* point2                  - vector 2
	"""
	def match(self, point1, point2):
		score = 0.0
		for i in range(0, len(point1)):
			score = score + point1[i] * point2[i]
			
		return score
	
	"""
		find the category of a given question.
		* question                - uncategorised question
	"""
	def get_category(self, question):
		wd_list = self.pre_processor.preprocess(question)
		queary_point = list()
		sq_sum = 0.0
		for wd in self.words.keys():
			num = wd_list.get(wd, 0)
			queary_point.append(num);
			sq_sum = sq_sum + num * num

		sq_sum = math.sqrt(sq_sum)
		
		if not sq_sum == 0:	
			for i in range(0, len(queary_point)):
				queary_point[i] = queary_point[i] / sq_sum

		top = list()
		
		for point in self.points:
			score = self. match(point[0], queary_point)
			top.append((score, point[1]))
			
		top = sorted(top)
		
		d = {}
		if self.weighted_distance:
			for i in range(len(top) - self.n, len(top)):
				d[top[i][1]] = d.get(top[i][1], 0) + self.weight * math.pow(top[i][0], self.p)
		else:
			for i in range(len(top) - self.n, len(top)):
				d[top[i][1]] = d.get(top[i][1], 0) + 1
			
		lst = sorted([(d[key], key) for key in d.keys()])
		return lst[len(lst) - 1][1]
		
	"""
		save the current word list and point list
		* dimention_file          - file to save word list
		* points_file             - file to save point list
	"""
	def save(self, dimention_file, points_file):
		try:
			f = open(dimention_file, 'w')
		except IOError:
			print "ERROR : '", dimention_file, "' is missing"
			exit(0)
			
		f.write(json.dumps(self.words))
		f.close()
		
		try:
			f = open(points_file, 'w')
		except IOError:
			print "ERROR : '", points_file, "' is missing"
			exit(0)
	
		f.write(json.dumps(self.points))
		f.close()
		
	"""
		load the current word list and point list from saved files
		* dimention_file          - file to load word list from
		* points_file             - file to load point list from
	"""
	def load(self, dimention_file, points_file):
		try:
			f = open(dimention_file, 'r')
		except IOError:
			print "ERROR : '", dimention_file, "' is missing"
			exit(0)
			
		self.words = json.loads(f.read())
		f.close()
		
		try:
			f = open(points_file, 'r')
		except IOError:
			print "ERROR : '", points_file, "' is missing"
			exit(0)
			
		self.points = json.loads(f.read())
		f.close()
	
	"""
		return the word list
	"""
	def get_dimensions(self):
		return self.words
	
	"""
		set the word list in to a given list
		*d                        - dictionary containing the new word list
	"""
	def set_dimensions(self, d):
		self.words = d

# 	
# classifier = classify_knn(3, True, 1.0, 2.0)
# 
# 
# q = list()
# 
# names = [
# 	"AC",
# 	"children",
# 	"communication",
# 	"cultural",
# 	"educational",
# 	"employers",
# 	"english",
# 	"environment",
# 	"facilities",
# 	"family",
# 	"health",
# 	"holidays",
# 	"ill",
# 	"interaction",
# 	"language",
# 	"leadership",
# 	"machines",
# 	"management",
# 	"manager",
# 	"members",
# 	"resources",
# 	"room",
# 	"stress",
# 	"studies",
# 	"supervisor",
# 	"supervisors",
# 	"tools",
# 	"transport",
# 	"transportation"
# 	]
# 
# for name in names:
# 	q.append(classifier.file_read('data/' + name + '.txt'))
# 	
# for i in range(0, len(q)):
# 	classifier.get_all_words(q[i])
# 	
# for i in range(0, len(q)):
# 	classifier.train(names[i], q[i])
# 
# classifier.save("word_list.json", "points.json")
# 
# print "done"