'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from aliyun.api.base import RestApi
class Rds20140815DescribeOptimizeAdviceOnMissIndexRequest(RestApi):
	def __init__(self,domain='rds.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.DBInstanceId = None
		self.PageNumber = None
		self.PageSize = None

	def getapiname(self):
		return 'rds.aliyuncs.com.DescribeOptimizeAdviceOnMissIndex.2014-08-15'
