import web
import json
        
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
	def GET(self, name):
		if not name: 
			return json.load(open('db.out'))
		else:
			try:
				return json.load(open('db.out'))[name]
			except Exception as e:
				return "No such machine in the list."
	def POST(self, data):
		dict = json.loads(web.data())
		write_in(dict, 'db.out')
		return "success!"

if __name__ == "__main__":
	app.run()