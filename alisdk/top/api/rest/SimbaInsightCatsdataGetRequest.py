'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from top.api.base import RestApi
class SimbaInsightCatsdataGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.category_id_list = None
		self.end_date = None
		self.start_date = None

	def getapiname(self):
		return 'taobao.simba.insight.catsdata.get'
