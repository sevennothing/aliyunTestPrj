'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from top.api.base import RestApi
class CrmGroupUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.group_id = None
		self.new_group_name = None

	def getapiname(self):
		return 'taobao.crm.group.update'
