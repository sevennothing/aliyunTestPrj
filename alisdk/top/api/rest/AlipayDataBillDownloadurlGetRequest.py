'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from top.api.base import RestApi
class AlipayDataBillDownloadurlGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.auth_token = None
		self.bill_date = None
		self.bill_type = None

	def getapiname(self):
		return 'alipay.data.bill.downloadurl.get'
