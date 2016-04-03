import web
import json
import re
        
urls = (
	'/(.*)', 'hello'
)
app = web.application(urls, globals())

def write_in(dict, file_name):
	try:
		f = open(file_name, 'r')
		old_dict = json.load(f)
		f.close()
	except Exception as e:
		old_dict = {}
	old_dict.update(dict)
	f = open(file_name, 'w')
	json.dump(old_dict, f)
	f.close()

class hello:        
	def GET(self, route):
		data = web.input()
		db = json.load(open("db.out"))
		if not route: 
			return db
		else:
			parsed = re.split('/', route)
			name = parsed[0]
			if len(parsed) == 1:
				return db[name]
			else:
				attr = parsed[2]
				return db[name][attr]
	def POST(self, data):
		dict = json.loads(web.data())
		write_in(dict, 'db.out')
		return "success!"

if __name__ == "__main__":
	app.run()