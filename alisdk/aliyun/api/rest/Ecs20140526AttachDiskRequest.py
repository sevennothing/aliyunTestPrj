'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from aliyun.api.base import RestApi
class Ecs20140526AttachDiskRequest(RestApi):
	def __init__(self,domain='ecs.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.DeleteWithInstance = None
		self.Device = None
		self.DiskId = None
		self.InstanceId = None

	def getapiname(self):
		return 'ecs.aliyuncs.com.AttachDisk.2014-05-26'
