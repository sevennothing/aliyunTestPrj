'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from aliyun.api.base import RestApi
class Ecs20140526ModifyEipAddressAttributeRequest(RestApi):
	def __init__(self,domain='ecs.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.AllocationId = None
		self.Bandwidth = None

	def getapiname(self):
		return 'ecs.aliyuncs.com.ModifyEipAddressAttribute.2014-05-26'