'''
Created by auto_sdk on 2014-11-20 12:53:43
'''
from aliyun.api.base import RestApi
class Rds20140815DescribeSlowLogsRequest(RestApi):
	def __init__(self,domain='rds.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.OwnerId = None
		self.OwnerAccount = None
		self.ResourceOwnerAccount = None
		self.DBInstanceId = None
		self.DBName = None
		self.EndTime = None
		self.PageNumber = None
		self.PageSize = None
		self.SortKey = None
		self.StartTime = None

	def getapiname(self):
		return 'rds.aliyuncs.com.DescribeSlowLogs.2014-08-15'
