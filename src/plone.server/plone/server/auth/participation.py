# -*- coding: utf-8 -*-
from zope.security.interfaces import IParticipation
from zope.interface import implementer
from zope.component import adapter
from plone.server.interfaces import IRequest
from collections import OrderedDict
from plone.server.registry import ACTIVE_AUTH_EXTRACTION_KEY, ACTIVE_AUTH_USER_KEY
from plone.server.utils import import_class
from plone.registry.interfaces import IRegistry


class PloneUser(object):

    def __init__(self, request):
        self.id = "plone"
        self.request = request
        self._groups = {}
        self._roles = []
        self._roles = []
        self._properties = {}


class AnonymousUser(PloneUser):

    def __init__(self, request):
        self.id = 'Anonymous User'
        self.request = request


@adapter(IRequest)
@implementer(IParticipation)
class PloneParticipation(object):

    def __init__(self, request):
        self.request = request
        # Cached user
        if not hasattr(self.request, '__cache_user'):
            plone_registry = request.registry.getUtility(IRegistry)
            # Plugin to extract the credentials to request._cache_credentials
            plugins = plone_registry.get(ACTIVE_AUTH_EXTRACTION_KEY, [])
            for plugin in plugins:
                plugin_object = import_class(plugin)
                plugin_object(self.request)

            # Plugin to get the user to request._cache_user
            plugins = plone_registry.get(ACTIVE_AUTH_USER_KEY, [])
            for plugin in plugins:
                plugin_object = import_class(plugin)
                plugin_object(self.request)

        self.principal = self.request._cache_user
        self.interaction = None


