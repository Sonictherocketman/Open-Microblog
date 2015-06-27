""" A simple model of a standard-compliant Microblog Feed.
This module contains wrappers for all 3 Microblog feed files
(feed, follows, blocks) and adhered to the Open Microblog
Standard. For more information see:
http://openmicroblog.com

author: Brian Schrader
since: 2015-06-01
standard-version: 0.5
"""
from __future__ import print_function

import sys
from xml.dom import minidom

try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen


class MalformedFeedError(Exception):
    pass


# Feed Model

MICROBLOG_NAMESPACE = 'microblog'


class Feed(object):
    """ The base object that represents an XML feed. """

    def __init__(self, raw_text=''):
        """ Using the raw text provided, pull out the
        relevant information.
        """
        self._tree = minidom.parseString(
            raw_text).getElementsByTagName('channel')[0]


class MainFeed(Feed):
    """ Models a user's feed.xml feed.
    This feed contains a list of status messages which
    the given user has posted.
    """
    REQUIRED_RSS_ELEMENTS = set(['link', 'lastBuildDate', 'language'])
    OPTIONAL_RSS_ELEMENTS = set(['docs', 'description'])
    REQUIRED_MICROBLOG_ELEMENTS = set(['username', 'user_id', 'profile'])
    OPTIONAL_MICROBLOG_ELEMENTS = set(['blocks', 'follows', 'message',
                                       'user_full_name', 'next_node'])

    def __init__(self, raw_text=''):
        super(MainFeed, self).__init__(raw_text)
        tree = self._tree
        self.items = []

        for attr in self.REQUIRED_RSS_ELEMENTS:
            try:
                value = self._tree.getElementsByTagName(
                    '{attr}'.format(attr=attr))[0].firstChild
                if value:
                    value = value.nodeValue
                else:
                    value = ''
            except IndexError:
                raise MalformedFeedError(
                    'Feed must contain all required elements: '
                    '{0} is missing.'.format(attr))
            setattr(self, attr, value)

        for attr in self.OPTIONAL_RSS_ELEMENTS:
            try:
                value = self._tree.getElementsByTagName(
                    '{attr}'.format(attr=attr))[0].firstChild.nodeValue
            except IndexError:
                continue
            setattr(self, attr, value)

        for attr in self.REQUIRED_MICROBLOG_ELEMENTS:
            try:
                value = self._tree.getElementsByTagName(
                    '{ns}:{attr}'.format(ns=MICROBLOG_NAMESPACE, attr=attr)
                )[0].firstChild.nodeValue
            except IndexError:
                raise MalformedFeedError(
                    'Feed must contain all required elements: '
                    '{0} is missing.'.format(attr))
            setattr(self, attr, value)

        for attr in self.OPTIONAL_MICROBLOG_ELEMENTS:
            try:
                value = self._tree.getElementsByTagName(
                    '{ns}:{attr}'.format(ns=MICROBLOG_NAMESPACE, attr=attr)
                )[0].firstChild.nodeValue
            except IndexError:
                pass
            else:
                setattr(self, attr, value)

        for element in tree.getElementsByTagName('item'):
            self.items.append(MainFeedItem(element.toxml('utf-8')))


class UserFeed(Feed):
    """ Models a user's follows.xml or blocks.xml feed.
    This feed contains a list of users which the given
    user either follows or blocks.
    """

    def __init__(self, raw_text=''):
        super(UserFeed, self).__init__(raw_text)
        tree = self._tree
        self.items = []
        for element in tree.getElementsByTagName('item'):
            self.items.append(UserFeedItem(element.firstChild.nodeValue))


# Item Model


class Item(object):
    """ The base object that represents a generic item in a feed. """

    def __init__(self, raw_text=''):
        self._tree = minidom.parseString(raw_text)

class MainFeedItem(Item):
    """ Models an item found in the main feed representing
    a status message.
    """

    REQUIRED_RSS_ELEMENTS = set(['guid', 'pubDate', 'description'])
    OPTIONAL_RSS_ELEMENTS = set()
    REQUIRED_MICROBLOG_ELEMENTS = set()
    OPTIONAL_MICROBLOG_ELEMENTS = set([
        'reply', 'in_reply_to_user_id', 'in_reply_to_user_link',
        'in_reply_to_status_id', 'reposted_status_user_id',
        'reposted_user_link', 'reposted_status_id', 'reposted_status_pubdate',
        'language'])

    def __init__(self, raw_text=''):
        super(MainFeedItem, self).__init__(raw_text)
        self.items = []

        for attr in self.REQUIRED_RSS_ELEMENTS:
            try:
                value = self._tree.getElementsByTagName('{attr}'.format(
                    ns=MICROBLOG_NAMESPACE, attr=attr))[0].firstChild.nodeValue
            except IndexError:
                raise MalformedFeedError(
                    'Feed must contain all required elements: '
                    '{0} is missing.'.format(attr))
            setattr(self, attr, value)

        for attr in self.OPTIONAL_RSS_ELEMENTS:
            try:
                value = self._tree.getElementsByTagName(
                    '{attr}'.format(ns=MICROBLOG_NAMESPACE, attr=attr)
                )[0].firstChild.nodeValue
            except IndexError:
                continue
            setattr(self, attr, value)

        for attr in self.REQUIRED_MICROBLOG_ELEMENTS:
            try:
                value = self._tree.getElementsByTagName(
                    '{ns}:{attr}'.format(ns=MICROBLOG_NAMESPACE, attr=attr)
                )[0].firstChild.nodeValue
            except IndexError:
                raise MalformedFeedError(
                    'Feed must contain all required elements: '
                    '{0} is missing.'.format(attr))
            setattr(self, attr, value)

        for attr in self.OPTIONAL_MICROBLOG_ELEMENTS:
            try:
                value = self._tree.getElementsByTagName(
                    '{ns}:{attr}'.format(ns=MICROBLOG_NAMESPACE, attr=attr)
                )[0].firstChild.nodeValue
            except IndexError:
                continue
            setattr(self, attr, value)


class UserFeedItem(Item):
    """ Models an item found in the blocks or follows feed
    representing a user.
    """

    REQUIRED_RSS_ELEMENTS = set()
    OPTIONAL_RSS_ELEMENTS = set()
    REQUIRED_MICROBLOG_ELEMENTS = set()
    OPTIONAL_MICROBLOG_ELEMENTS = set(['user_id', 'username', 'user_link'])

    def __init__(self, raw_text=''):
        super(UserFeedItem, self).__init__(raw_text)
        self.items = []

        for attr in self.REQUIRED_RSS_ELEMENTS:
            try:
                value = self._tree.getElementsByTagName(
                    '{attr}'.format(attr=attr))[0].firstChild.nodeValue
            except IndexError:
                raise MalformedFeedError(
                    'Feed must contain all required elements: '
                    '{0} is missing.'.format(attr))
            setattr(self, attr, value)

        for attr in self.OPTIONAL_RSS_ELEMENTS:
            try:
                value = self._tree.getElementsByTagName(
                    '{attr}'.format(attr=attr))[0].firstChild.nodeValue
            except IndexError:
                continue
            setattr(self, attr, value)

        for attr in self.REQUIRED_MICROBLOG_ELEMENTS:
            try:
                value = self._tree.getElementsByTagName(
                    '{ns}:{attr}'.format(ns=MICROBLOG_NAMESPACE, attr=attr)
                )[0].firstChild.nodeValue
            except IndexError:
                raise MalformedFeedError(
                    'Feed must contain all required elements: '
                    '{0} is missing.'.format(attr))
            setattr(self, attr, value)

        for attr in self.OPTIONAL_MICROBLOG_ELEMENTS:
            try:
                value = self._tree.getElementsByTagName(
                    '{ns}:{attr}'.format(ns=MICROBLOG_NAMESPACE, attr=attr)
                )[0].firstChild.nodeValue
            except IndexError:
                continue
            setattr(self, attr, value)


if __name__ == '__main__':
    try:
        url = sys.argv[1]
    except IndexError:
        print('You must include a url to validate.')
        sys.exit(1)

    feed = MainFeed(raw_text=urlopen(url).read())
    if len(feed.items) > 0:
        description = feed.items[-1].description
        print('\n{0} says, "{1}"'.format(feed.username, description))
    else:
        print('\n{0} hasn\'t said anything yet.'.format(feed.username))
