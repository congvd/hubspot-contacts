# coding: utf-8

from hubspot.connection.testing import MockPortalConnection
from nose.tools import eq_

from hubspot.contacts import save_contact
from hubspot.contacts.testing import SaveContact

from tests._utils import make_contact
from tests.test_properties import STUB_STRING_PROPERTY


class TestSavingContact(object):

    def test_save_single_contact(self):
        contact = make_contact(None)
        connection = self._make_connection_for_contact(1, contact)

        vid = save_contact(contact, connection)

        eq_(1, vid)

    @staticmethod
    def _make_connection_for_contact(vid, contact, available_property=None):
        available_property = available_property or STUB_STRING_PROPERTY
        simulator = SaveContact(vid, contact, [available_property])
        connection = MockPortalConnection(simulator)
        return connection

