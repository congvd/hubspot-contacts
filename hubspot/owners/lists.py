##############################################################################
#
# Copyright (c) 2014, 2degrees Limited.
# All Rights Reserved.
#
# This file is part of hubspot-contacts
# <https://github.com/2degrees/hubspot-contacts>, which is subject to the
# provisions of the BSD at
# <http://dev.2degreesnetwork.com/p/2degrees-license.html>. A copy of the
# license should accompany this distribution. THIS SOFTWARE IS PROVIDED "AS IS"
# AND ANY AND ALL EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT
# NOT LIMITED TO, THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST
# INFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE.
#
##############################################################################

from hubspot.connection import APIKey, PortalConnection

OWNERS_API_SCRIPT_NAME = '/owners/v2'

_OWNERS_LIST_COLLECTION_URL_PATH = OWNERS_API_SCRIPT_NAME + '/owners'
def get_all_owners(connection, is_include_inactive):
    owners_data = connection.send_get_request(_OWNERS_LIST_COLLECTION_URL_PATH, {
        'includeInactive': is_include_inactive
    })

    return owners_data

