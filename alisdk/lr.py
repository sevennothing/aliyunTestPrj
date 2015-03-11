# -*- coding: utf-8 -*-
'''
Created on 2014-6-17

@author: lijie.ma
'''
import aliyun.api


'''
这边可以设置一个默认的accessKeyId和accessKeySecret，当然也可以不设置
注意：默认的只需要设置一次就可以了

'''
aliyun.setDefaultAppInfo("ICfKMQhyhyotR07W", "cObYq5CD1ppf1zzzhw0iyEaszEMaG9")

'''
使用自定义的域名和端口（测试沙箱环境使用）
a = aliyun.api.Rds20130528DescribeDBInstancesRequest("rds.aliyuncs.com",80)

使用自定义的域名（测试沙箱环境使用）
a = aliyun.api.Rds20130528DescribeDBInstancesRequest("rds.aliyuncs.com")

使用默认的配置（调用线上环境）
a = aliyun.api.Rds20130528DescribeDBInstancesRequest()

'''

#a = aliyun.api.Rds20140815DescribeDBInstancesRequest()
#a = aliyun.api.Slb20140515DescribeLoadBalancersRequest();
#a = aliyun.api.Slb20140515DescribeRegionsRequest();
#a = aliyun.api.Ecs20140526DescribeInstanceAttributeRequest()
#a.InstanceId = "i-28metkvhf"
#a = aliyun.api.
#a = aliyun.api.
#a = aliyun.api.

#查询实例信息
a = aliyun.api.Slb20140515DescribeLoadBalancerAttributeRequest()
a.LoadBalancerId = "14ab315db23-cn-qingdao-cm5-a01"
try:
	f = a.getResponse()
	if("Code" in f):
		print("失败")
		print(f["Code"])
		print(f["Message"])
	else:
		print("成功")
		print(f)      
except Exception,e:
	print(e)
'''
#delete loadBalancer  listener [30443]

print "delete loadBalancer  listener"
a = aliyun.api.Slb20140515DeleteLoadBalancerListenerRequest();
a.LoadBalancerId = "14ab315db23-cn-qingdao-cm5-a01"
a.ListenerPort = 30443
try:
	f = a.getResponse()
	if("Code" in f):
		print("失败")
		print(f["Code"])
		print(f["Message"])
	else:
		print("成功")
		print(f)      
except Exception,e:
	print(e)
#create TCP 30443 port listen
print "create loadBalancer  HTTP listener with port is 30443"
a = aliyun.api.Slb20140515CreateLoadBalancerHTTPListenerRequest()
a.LoadBalancerId = "14ab315db23-cn-qingdao-cm5-a01"
a.ListenerPort = 30443
a.BackendServerPort = 30444
a.HealthCheckConnectPort = 30444
a.Bandwidth = -1
a.StickySession = 'off'
a.StickySessionType = 'server'
#a.Cookie = 
a.HealthCheck = 'on'
a.HealthCheckDomain = '$_ip'
a.HealthCheckURI = '/alicheck'
a.HealthCheckConnectPort = 30444
a.HealthyThreshold=4
a.UnhealthyThreshold=4
a.HealthCheckTimeout=3
a.HealthCheckInterval=5

try:
	f = a.getResponse()
	if("Code" in f):
		print("失败")
		print(f["Code"])
		print(f["Message"])
	else:
		print("成功")
		print(f)      
except Exception,e:
	print(e)

a = aliyun.api.Slb20140515StartLoadBalancerListenerRequest()
a.LoadBalancerId = "14ab315db23-cn-qingdao-cm5-a01"
a.ListenerPort = 30443
try:
	f = a.getResponse()
	if("Code" in f):
		print("失败")
		print(f["Code"])
		print(f["Message"])
	else:
		print("成功")
		print(f)      
except Exception,e:
	print(e)
'''
'''
#delete loadBalancer  listener [3000]

print "delete loadBalancer  listener 3000"
a = aliyun.api.Slb20140515DeleteLoadBalancerListenerRequest();
a.LoadBalancerId = "14ab315db23-cn-qingdao-cm5-a01"
a.ListenerPort = 3000
try:
	f = a.getResponse()
	if("Code" in f):
		print("失败")
		print(f["Code"])
		print(f["Message"])
	else:
		print("成功")
		print(f)      
except Exception,e:
	print(e)
#create HTTP 3000 port listen
print "create loadBalancer  HTTP listener with port is 3000"
a = aliyun.api.Slb20140515CreateLoadBalancerHTTPListenerRequest()
a.LoadBalancerId = "14ab315db23-cn-qingdao-cm5-a01"
a.ListenerPort = 3000
a.BackendServerPort = 3000
a.HealthCheckConnectPort = 3000
a.Bandwidth = -1
a.StickySession = 'off'
a.StickySessionType = 'server'
#a.Cookie = 
a.HealthCheck = 'on'
a.HealthCheckDomain = '$_ip'
a.HealthCheckURI = '/alicheck'
a.HealthCheckConnectPort = 3000
a.HealthyThreshold=4
a.UnhealthyThreshold=4
a.HealthCheckTimeout=3
a.HealthCheckInterval=5

try:
	f = a.getResponse()
	if("Code" in f):
		print("失败")
		print(f["Code"])
		print(f["Message"])
	else:
		print("成功")
		print(f)      
except Exception,e:
	print(e)

a = aliyun.api.Slb20140515StartLoadBalancerListenerRequest()
a.LoadBalancerId = "14ab315db23-cn-qingdao-cm5-a01"
a.ListenerPort = 3000
try:
	f = a.getResponse()
	if("Code" in f):
		print("失败")
		print(f["Code"])
		print(f["Message"])
	else:
		print("成功")
		print(f)      
except Exception,e:
	print(e)

'''

'''
#delete loadBalancer  listener [443]

print "delete loadBalancer  listener"
a = aliyun.api.Slb20140515DeleteLoadBalancerListenerRequest();
a.LoadBalancerId = "14ab315db23-cn-qingdao-cm5-a01"
a.ListenerPort = 443
try:
	f = a.getResponse()
	if("Code" in f):
		print("失败")
		print(f["Code"])
		print(f["Message"])
	else:
		print("成功")
		print(f)      
except Exception,e:
	print(e)


#create TCP 443 port listen
a = aliyun.api.Slb20140515CreateLoadBalancerTCPListenerRequest();
print "create loadBalancer  TCP listener with port is 443"
a.LoadBalancerId = "14ab315db23-cn-qingdao-cm5-a01"
a.ListenerPort = 443
a.BackendServerPort = 30443
a.HealthCheckConnectPort = 30443
a.Bandwidth = -1
try:
	f = a.getResponse()
	if("Code" in f):
		print("失败")
		print(f["Code"])
		print(f["Message"])
	else:
		print("成功")
		print(f)      
except Exception,e:
	print(e)

a = aliyun.api.Slb20140515StartLoadBalancerListenerRequest()
a.LoadBalancerId = "14ab315db23-cn-qingdao-cm5-a01"
a.ListenerPort = 443
try:
	f = a.getResponse()
	if("Code" in f):
		print("失败")
		print(f["Code"])
		print(f["Message"])
	else:
		print("成功")
		print(f)      
except Exception,e:
	print(e)
'''
'''
#delete loadBalancer  listener [80]

print "delete loadBalancer  listener 80"
a = aliyun.api.Slb20140515DeleteLoadBalancerListenerRequest();
a.LoadBalancerId = "14ab315db23-cn-qingdao-cm5-a01"
a.ListenerPort = 80
try:
	f = a.getResponse()
	if("Code" in f):
		print("失败")
		print(f["Code"])
		print(f["Message"])
	else:
		print("成功")
		print(f)      
except Exception,e:
	print(e)
#create HTTP 80 port listen
print "create loadBalancer  HTTP listener with port is 80"
a = aliyun.api.Slb20140515CreateLoadBalancerHTTPListenerRequest()
a.LoadBalancerId = "14ab315db23-cn-qingdao-cm5-a01"
a.ListenerPort = 80
a.BackendServerPort = 30080
a.HealthCheckConnectPort = 30080
a.Bandwidth = -1
a.StickySession = 'off'
a.StickySessionType = 'server'
#a.Cookie = 
a.HealthCheck = 'on'
a.HealthCheckDomain = '$_ip'
a.HealthCheckURI = '/alicheck'
a.HealthCheckConnectPort = 30080
a.HealthyThreshold=4
a.UnhealthyThreshold=4
a.HealthCheckTimeout=3
a.HealthCheckInterval=5

try:
	f = a.getResponse()
	if("Code" in f):
		print("失败")
		print(f["Code"])
		print(f["Message"])
	else:
		print("成功")
		print(f)      
except Exception,e:
	print(e)

a = aliyun.api.Slb20140515StartLoadBalancerListenerRequest()
a.LoadBalancerId = "14ab315db23-cn-qingdao-cm5-a01"
a.ListenerPort = 80
try:
	f = a.getResponse()
	if("Code" in f):
		print("失败")
		print(f["Code"])
		print(f["Message"])
	else:
		print("成功")
		print(f)      
except Exception,e:
	print(e)
'''
