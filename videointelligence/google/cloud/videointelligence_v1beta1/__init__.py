# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import

from google.cloud.videointelligence_v1beta1 import types
from google.cloud.videointelligence_v1beta1.gapic import enums
from google.cloud.videointelligence_v1beta1.gapic import video_intelligence_service_client


class VideoIntelligenceServiceClient(
        video_intelligence_service_client.VideoIntelligenceServiceClient):
    __doc__ = video_intelligence_service_client.VideoIntelligenceServiceClient.__doc__
    enums = enums


__all__ = (
    'enums',
    'types',
    'VideoIntelligenceServiceClient',
)
