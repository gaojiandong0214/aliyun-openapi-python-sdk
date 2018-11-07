# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class DescribeFlowNodeInstanceContainerLogRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'DescribeFlowNodeInstanceContainerLog')

	def get_Offset(self):
		return self.get_query_params().get('Offset')

	def set_Offset(self,Offset):
		self.add_query_param('Offset',Offset)

	def get_LogName(self):
		return self.get_query_params().get('LogName')

	def set_LogName(self,LogName):
		self.add_query_param('LogName',LogName)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_Length(self):
		return self.get_query_params().get('Length')

	def set_Length(self,Length):
		self.add_query_param('Length',Length)

	def get_ContainerId(self):
		return self.get_query_params().get('ContainerId')

	def set_ContainerId(self,ContainerId):
		self.add_query_param('ContainerId',ContainerId)

	def get_NodeInstanceId(self):
		return self.get_query_params().get('NodeInstanceId')

	def set_NodeInstanceId(self,NodeInstanceId):
		self.add_query_param('NodeInstanceId',NodeInstanceId)

	def get_ProjectId(self):
		return self.get_query_params().get('ProjectId')

	def set_ProjectId(self,ProjectId):
		self.add_query_param('ProjectId',ProjectId)