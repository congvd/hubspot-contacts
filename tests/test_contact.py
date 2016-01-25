# coding: utf-8

from hubspot.connection.testing import MockPortalConnection
from nose.tools import eq_
from nose.tools import assert_raises

from hubspot.contacts import save_contact
from hubspot.contacts.testing import SaveContact, SaveContactClientError

from tests._utils import make_contact
from tests.test_properties import STUB_STRING_PROPERTY

from hubspot.connection.exc import HubspotClientError


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

    def test_invalid_property_raises_hubspot_client_error(self):
        contact = make_contact(None, properties={'is_polite': 'notavalidinput'})
        connection = self._make_connection_for_contact_with_exception(contact, HubspotClientError("Property notavalidinput is invalid", "request-id", None))

        with assert_raises(HubspotClientError) as context:
            with connection:
                save_contact(contact, connection)
        eq_(context.exception.message, "Property notavalidinput is invalid")

    @staticmethod
    def _make_connection_for_contact_with_exception(contact, exception, available_property=None):
        available_property = available_property or STUB_STRING_PROPERTY
        simulator = SaveContactClientError(contact, exception, [available_property])
        connection = MockPortalConnection(simulator)
        return connection
