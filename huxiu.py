#coning:utf-8

from spider.spider import route, Handler, spider
import _env
from os.path import abspath, dirname, join
from operator import itemgetter

PREFIX = join(dirname(abspath(__file__)))
HTTP = "http://www.huxiu.com/tags/%s"

@route("/tags/(\d+)")
class _(Handler):
	def get(self,tag):  ## make it match with m.groups() from route.match
		## find tag
		tag = self.extract("<h1>", "</h1>")
		if tag == None:
			print "Tag not found..."
			return
		## prune tag
		tag = tag[tag.find("</span>")+7:]
		print tag

		## find tittles under this tag
		tittles = self.extract_all("<h3><a", "</a>")
		## prune tittle
		for i in xrange(len(tittles)):
			tittles[i] = tittles[i][tittles[i].find('k">')+3:]
			print "	  " + str(i + 1) + '.' + tittles[i]
		return




if __name__ == '__main__':
	for i in xrange(3500, 4000):
		spider.put(HTTP%i)
	# 10 threads run in parallel, each timeout in 30 sec
	# WARNING! new version of grevent doesn't support gevent.shutdown()!!!
	spider.run(10,30)

