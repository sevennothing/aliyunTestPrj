'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from top.api.base import RestApi
class TmallPromotagTagApplyRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.start_time = None
		self.tag_desc = None
		self.tag_name = None

	def getapiname(self):
		return 'tmall.promotag.tag.apply'
