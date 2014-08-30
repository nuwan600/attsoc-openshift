import os.path

ls = [
	"AC",
	"transportation",
	"facilities",
	"equipment",
	"tools",
	"machines",
	"room",
	"transport",
	"condition",
	"environment",
	"workplace",
	"stress",
	"stressed",
	"resources",
	"relationship",
	"employees",
	"managers",
	"employer",
	"employers",
	"member",
	"members",
	"supervisor",
	"supervisors",
	"cultural",
	"unavoidable",
	"health",
	"studies",
	"educational",
	"manager",
	"employee",
	"interaction",
	"leadership",
	"management",
	"family",
	"children",
	"holidays",
	"communication",
	"speak",
	"language",
	"english",
	"ill",
	"education"
	]

for l in ls:
	if not os.path.isfile('data/' + l + '.txt'):
		try:
			f = open('data/' + l + '.txt', 'w')
			print 'data/' + l + '.txt : file created'
		except IOError:
			print "ERROR : "
			exit(0)
	else:
		print 'data/' + l + '.txt : file exists'