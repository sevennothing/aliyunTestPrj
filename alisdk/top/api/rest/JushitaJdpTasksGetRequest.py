'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from top.api.base import RestApi
class JushitaJdpTasksGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fetch_num = None
		self.task_item_num = None
		self.task_items = None
		self.type = None
		self.user_ids = None

	def getapiname(self):
		return 'taobao.jushita.jdp.tasks.get'
