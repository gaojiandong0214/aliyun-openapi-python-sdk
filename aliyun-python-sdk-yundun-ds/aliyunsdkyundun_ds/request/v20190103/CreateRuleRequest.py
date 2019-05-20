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
class CreateRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Yundun-ds', '2019-01-03', 'CreateRule','sddp')

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_FeatureType(self):
		return self.get_query_params().get('FeatureType')

	def set_FeatureType(self,FeatureType):
		self.add_query_param('FeatureType',FeatureType)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_RiskLevelId(self):
		return self.get_query_params().get('RiskLevelId')

	def set_RiskLevelId(self,RiskLevelId):
		self.add_query_param('RiskLevelId',RiskLevelId)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_CustomType(self):
		return self.get_query_params().get('CustomType')

	def set_CustomType(self,CustomType):
		self.add_query_param('CustomType',CustomType)

	def get_Category(self):
		return self.get_query_params().get('Category')

	def set_Category(self,Category):
		self.add_query_param('Category',Category)

	def get_Content(self):
		return self.get_query_params().get('Content')

	def set_Content(self,Content):
		self.add_query_param('Content',Content)