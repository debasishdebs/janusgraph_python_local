"""
Copyright 2018 Debasish Kanhar

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

__author__ = "Debasish Kanhar (https://github.com/debasishdebs)"
__credits__ = ["Florian Hockman", "Jason Plurad", "Dave Brown", "Marko Rodriguez"]
__license__ = "Apache-2.0"
__version__ = "0.0.1"
__email__ = ["d.kanhar@gmail.com", "dekanhar@in.ibm.com"]


from gremlin_python.structure.io.graphsonV3d0 import GraphSONUtil
from ..core.datatypes.RelationIdentifier import RelationIdentifier


class RelationIdentifierSerializer(object):
    GRAPHSON_PREFIX = "janusgraph"
    GRAPHSON_BASE_TYPE = "RelationIdentifier"

    @classmethod
    def dictify(cls, relationID, writer):
        """

        Args:
            relationID (RelationIdentifier):
            writer:

        Returns:

        """

        relationJSON = cls.__relationID_to_json(relationID)

        serializedJSON = GraphSONUtil.typedValue(cls.GRAPHSON_BASE_TYPE, relationJSON, cls.GRAPHSON_PREFIX)

        return serializedJSON

    @classmethod
    def __relationID_to_json(cls, relationID):
        """

        Args:
            relationID (RelationIdentifier):

        Returns:

        """

        relationIdDict = dict()

        relationIdDict["relationId"] = relationID.toString()

        return relationIdDict
