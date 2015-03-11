'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from top.api.base import RestApi
class TbkCreativeAuditRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.audit_time = None
		self.comment = None
		self.creative_id = None
		self.result = None
		self.success_url = None

	def getapiname(self):
		return 'taobao.tbk.creative.audit'
