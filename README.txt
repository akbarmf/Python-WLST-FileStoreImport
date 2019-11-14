CSV File Input Format and Explanation

JMS Module:
module,moduleName,serverTarget:type

Subdeployment:
subdeployemnt,moduleName,subdeploymentName,serverTarget:type(JMSServer)

Foreign Server:
foreign,moduleName,foreignName,jndiInitContextFactory,jndiConnUrl

Queue:
queue,moduleName,queueName,jndiQueue,subdeploymentName(insert "default" to set default target and leave it blank if not assign)

Distributed Queue: Uniform
distqueueuniform,moduleName,distributedQueueName,jndiDistributedQueue,subdeploymentName(insert "default" to set default target and leave it blank if not assign)

Distributed Queue: Weighted
distqueueweighted,moduleName,distributedQueueName,jndiDistributedQueue,queueNameMember1|queueNameMember2|queueNameMember3

Topic:
topic,moduleName,topicName,jndiTopic,subdepName,subdeploymentName(leave it blank if not assign)

Distributed Topic: Uniform
disttopicuniform,modulename,distTopicName,jndidistTopic,subdeploymentName(insert "default" to set default target and leave it blank if not assign)

Distributed Topic: Weighted
disttopicweighted,modulename,distTopicName,jndiDistTopic,queueNameMember1|queueNameMember2|queueNameMember3

Connection Factory:
factory,moduleName,connFactoryName,jndiconnFactory,attachJMSXUserId,clientIdPolicy,subscriptionSharingPolicy,messagesMaximum,XAConnectionFactoryEnabled,subdeploymentName(insert "default" to set default target and leave it blank if not assign)

- attachJMSXUserId : '1'(true) or '0'(false)
- clientIdPolicy : 'Unrestricted' or 'Restricted'
- subscriptionSharingPolicy : 'Sharable' or 'Exclusive'
- messagesMaximum : number int
- XAConnectionFactoryEnabled : '1'(true) or '0'(false) 

Foreign Destination:
dest,moduleName,foreignName,foreignDestName,localJNDIName,remoteJNDIName

Foreign Connection Factory Name:
conn,moduleName,foreignName,foreignConnFactName,localJNDIName,remoteJNDIName

Quota:
quota,moduleName,quotaName,bytesMaximum,messagesMaximum,policy,shared

- bytesMaximum : int, default values '9223372036854775807'
- messagesMaximum : int, default values '9223372036854775807'
- policy : 'FIFO' or 'Preemptive'
- shared : '1'(true) of '0'(false)


JMS Module
- module		: tag that use to create JMS Module (dont change)
- moduleName	: name of JMS Module you want (change)
- serverTarget	: targetName:Server  => for server target
				  targetName:Cluster => for cluster target
				  targetName:Server|targetName:Cluster => for target more than one

Foreign Server:
- foreign		: tag that use to create Foreign Server (dont change)
- moduleName	: name of JMS Module that has been created before (change)
- foreignName	: name of Foreign Server in JMS Module (change)
- jndiInitContextFactory	: JNDI Initial Context Factory
- jndiConnUrl	: JNDI Connection URL

Foreign Destination:
- dest			: tag that use to create Foreign Destination inside Foreign Server (dont change)
- moduleName	: name of JMS Module that has been created before (change)
- foreignName	: name of Foreign Server in JMS Module that has been created before (change)
- foreignDestName	: name of Foreign Destination that created inside Foreign Server (change)
- localJNDIName	: Local JNDI Name
- remoteJNDIName: Remote JNDI Name

Foreign Connection Factory Name:
- conn			: tag that use to create Connection Factory inside Foreign Server (dont change)
- moduleName	: name of JMS Module that has been created before (change)
- foreignName	: name of Foreign Server in JMS Module that has been created before (change)
- foreignConnFactName	: name of Foreign Connection Factory that created inside Foreign Server (change)
- localJNDIName	: Local JNDI Name
- remoteJNDIName: Remote JNDI Name