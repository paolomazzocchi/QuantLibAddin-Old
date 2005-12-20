
"""
 Copyright (C) 2005 Eric Ehlers

 This file is part of QuantLib, a free-software/open-source library
 for financial quantitative analysts and developers - http://quantlib.org/

 QuantLib is free software: you can redistribute it and/or modify it under the
 terms of the QuantLib license.  You should have received a copy of the
 license along with this program; if not, please email quantlib-dev@lists.sf.net
 The license is also available online at http://quantlib.org/html/license.html

 This program is distributed in the hope that it will be useful, but WITHOUT
 ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 FOR A PARTICULAR PURPOSE.  See the license for more details.
"""

'enumeration'

import Serializable
import common

class EnumerationDefinition(Serializable.Serializable):
    'encapsulate a string/value mapping for a QuantLib enumeration'

    groupName = 'EnumerationDefinitions'

    def serialize(self, serializer):
        'load/unload class state to/from serializer object'
        serializer.serializeProperty(self.__dict__, common.STRING)
        serializer.serializeProperty(self.__dict__, common.VALUE)

    def key(self):
        'return unique identifier for this object'
        return self.string

class Enumeration(Serializable.Serializable):
    'encapsulate enumerations for a QuantLib datatype'

    groupName = 'Enumerations'

    def serialize(self, serializer):
        'load/unload class state to/from serializer object'
        serializer.serializeAttributeBoolean(self.__dict__, common.DOCUMENTATION_ONLY)
        serializer.serializeProperty(self.__dict__, common.TYPE)
        serializer.serializeBoolean(self.__dict__, common.CONSTRUCTOR)
        serializer.serializeObjectDict(self.__dict__, EnumerationDefinition)

    def key(self):
        'return unique identifier for this object'
        return self.type

    def getEnumerationDefinitions(self):
        'serve up enumeration definition objects alphabetically by name'
        for enumDefKey in self.EnumerationDefinitionKeys:
            yield self.EnumerationDefinitions[enumDefKey]

