'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from aliyun.api.base import RestApi
class Ecs20140526DescribeDisksRequest(RestApi):
	def __init__(self,domain='ecs.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.Category = None
		self.DeleteAutoSnapshot = None
		self.DeleteWithInstance = None
		self.DiskIds = None
		self.DiskType = None
		self.InstanceId = None
		self.PageNumber = None
		self.PageSize = None
		self.Portable = None
		self.RegionId = None
		self.SnapshotId = None
		self.Status = None
		self.ZoneId = None

	def getapiname(self):
		return 'ecs.aliyuncs.com.DescribeDisks.2014-05-26'
