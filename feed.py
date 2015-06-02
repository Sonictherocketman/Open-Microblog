""" A simple model of a standard-compliant Microblog Feed.
This module contains wrappers for all 3 Microblog feed files
(feed, follows, blocks) and adhered to the Open Microblog
Standard. For more information see:
http://openmicroblog.com

author: Brian Schrader
since: 2015-06-01
standard-version: 0.5
"""

from lxml import etree
from defusedxml import lxml


class MalformedFeedError(Exception):
    pass


# Feed Model

MICROBLOG_NAMESPACE = 'microblog'
NSMAP = {
        MICROBLOG_NAMESPACE: 'http://openmicroblog.com/',
    }

class Feed(object):
    """ The base object that represents an XML feed. """

    def __init__(self, raw_text=''):
        """ Using the raw text provided, pull out the
        relevant information.
        """
        self._tree = lxml.fromstring(raw_text).find('channel')


class MainFeed(Feed):
    """ Models a user's feed.xml feed.
    This feed contains a list of status messages which
    the given user has posted.
    """
    REQUIRED_RSS_ELEMENTS = {'link', 'lastBuildDate', 'language'}
    OPTIONAL_RSS_ELEMENTS = {'docs', 'description'}
    REQUIRED_MICROBLOG_ELEMENTS = {'username', 'user_id', 'profile', }
    OPTIONAL_MICROBLOG_ELEMENTS = {'blocks', 'follows', 'message', 'user_full_name',
            'next_node'}

    def __init__(self, raw_text=''):
        super(self.__class__, self).__init__(raw_text)
        tree = self._tree
        self.items = []

        for attr in self.REQUIRED_RSS_ELEMENTS:
            try:
                value = self._tree.find('{attr}'.format(ns=MICROBLOG_NAMESPACE,
                        attr=attr),
                    namespaces=NSMAP).text
            except AttributeError:
                raise MalformedFeedError(
                        'Feed must contain all required elements: {} is missing.'\
                                .format(attr))
            setattr(self, attr, value)

        for attr in self.OPTIONAL_RSS_ELEMENTS:
            value = self._tree.find('{attr}'.format(ns=MICROBLOG_NAMESPACE,
                    attr=attr),
                namespaces=NSMAP)
            if value is not None:
                setattr(self, attr, value)

        for attr in self.REQUIRED_MICROBLOG_ELEMENTS:
            try:
                value = self._tree.find('{ns}:{attr}'.format(ns=MICROBLOG_NAMESPACE,
                        attr=attr),
                    namespaces=NSMAP).text
            except AttributeError:
                raise MalformedFeedError(
                        'Feed must contain all required elements: {} is missing.'\
                                .format(attr))
            setattr(self, attr, value)

        for attr in self.OPTIONAL_MICROBLOG_ELEMENTS:
            value = self._tree.find('{ns}:{attr}'.format(ns=MICROBLOG_NAMESPACE,
                    attr=attr),
                namespaces=NSMAP)
            if value is not None:
                setattr(self, attr, value)

        for element in tree.xpath('//item'):
            self.items.append(MainFeedItem(etree.tostring(element)))


class UserFeed(Feed):
    """ Models a user's follows.xml or blocks.xml feed.
    This feed contains a list of users which the given
    user either follows or blocks.
    """

    def __init__(self, raw_text=''):
        super(self.__class__, self).__init__(raw_text)
        tree = self._tree
        self.items = []
        for element in tree.find('item'):
            self.items.append(UserFeedItem(element.text))


# Item Model


class Item(object):
    """ The base object that represents a generic item in a feed. """

    def __init__(self, raw_text=''):
        self._tree = lxml.fromstring(raw_text)

class MainFeedItem(Item):
    """ Models an item found in the main feed representing
    a status message.
    """

    REQUIRED_RSS_ELEMENTS = {'guid', 'pubDate', 'description'}
    OPTIONAL_RSS_ELEMENTS = {}
    REQUIRED_MICROBLOG_ELEMENTS = {}
    OPTIONAL_MICROBLOG_ELEMENTS = {'reply', 'in_reply_to_user_id', 'in_reply_to_user_link',
            'in_reply_to_status_id', 'reposted_status_user_id', 'reposted_user_link',
            'reposted_status_id', 'reposted_status_pubdate', 'language'}

    def __init__(self, raw_text=''):
        super(self.__class__, self).__init__(raw_text)
        self.items = []

        for attr in self.REQUIRED_RSS_ELEMENTS:
            try:
                value = self._tree.find('{attr}'.format(ns=MICROBLOG_NAMESPACE,
                        attr=attr),
                    namespaces=NSMAP).text
            except AttributeError:
                raise MalformedFeedError(
                        'Feed must contain all required elements: {} is missing.'\
                                .format(attr))
            setattr(self, attr, value)

        for attr in self.OPTIONAL_RSS_ELEMENTS:
            value = self._tree.find('{attr}'.format(ns=MICROBLOG_NAMESPACE,
                    attr=attr),
                namespaces=NSMAP)
            if value is not None:
                setattr(self, attr, value)

        for attr in self.REQUIRED_MICROBLOG_ELEMENTS:
            try:
                value = self._tree.find('{ns}:{attr}'.format(ns=MICROBLOG_NAMESPACE,
                        attr=attr),
                    namespaces=NSMAP).text
            except AttributeError:
                raise MalformedFeedError(
                        'Feed must contain all required elements: {} is missing.'\
                                .format(attr))
            setattr(self, attr, value)

        for attr in self.OPTIONAL_MICROBLOG_ELEMENTS:
            value = self._tree.find('{ns}:{attr}'.format(ns=MICROBLOG_NAMESPACE,
                    attr=attr),
                namespaces=NSMAP)
            if value is not None:
                setattr(self, attr, value)


class UserFeedItem(Item):
    """ Models an item found in the blocks or follows feed
    representing a user.
    """

    REQUIRED_RSS_ELEMENTS = {}
    OPTIONAL_RSS_ELEMENTS = {}
    REQUIRED_MICROBLOG_ELEMENTS = {}
    OPTIONAL_MICROBLOG_ELEMENTS = {'user_id', 'username', 'user_link'}

    def __init__(self, raw_text=''):
        super(self.__class__, self).__init__(raw_text)
        self.items = []

        for attr in self.REQUIRED_RSS_ELEMENTS:
            try:
                value = self._tree.find('{attr}'.format(ns=MICROBLOG_NAMESPACE,
                        attr=attr),
                    namespaces=NSMAP).text
            except AttributeError:
                raise MalformedFeedError(
                        'Feed must contain all required elements: {} is missing.'\
                                .format(attr))
            setattr(self, attr, value)

        for attr in self.OPTIONAL_RSS_ELEMENTS:
            value = self._tree.find('{attr}'.format(ns=MICROBLOG_NAMESPACE,
                    attr=attr),
                namespaces=NSMAP)
            if value is not None:
                setattr(self, attr, value)

        for attr in self.REQUIRED_MICROBLOG_ELEMENTS:
            try:
                value = self._tree.find('{ns}:{attr}'.format(ns=MICROBLOG_NAMESPACE,
                        attr=attr),
                    namespaces=NSMAP).text
            except AttributeError:
                raise MalformedFeedError(
                        'Feed must contain all required elements: {} is missing.'\
                                .format(attr))
            setattr(self, attr, value)

        for attr in self.OPTIONAL_MICROBLOG_ELEMENTS:
            value = self._tree.find('{ns}:{attr}'.format(ns=MICROBLOG_NAMESPACE,
                    attr=attr),
                namespaces=NSMAP)
            if value is not None:
                setattr(self, attr, value)


if __name__ == '__main__':
    import sys, requests
    try:
        url = sys.argv[1]
    except IndexError:
        print 'You must include a url to validate.'; sys.exit(0)

    feed = MainFeed(raw_text=str(requests.get(url).text))
    if len(feed.items) > 0:
        description = feed.items[-1].description
        print '\n{} says, "{}"'.format(feed.username, description)
    else:
        print '\n{} hasn\'t said anything yet.'.format(feed.username)
