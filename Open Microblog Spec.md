
# Open Microblog
================================================================

**Version:** 0.3 InDev 

**Last Updated:** Sept 14, 2014

**Known Bugs/Issues:**
- In the sample feed, the root element is 'rss'. As of v0.2 it is a straight port of the RSS root element, this will be fixed..

================================================================
**Overview**
- What is this
- What is it used for?
- Why not just use RSS? It's already there...
- How does it work?
- Why doesn't it have a cool name?
- Terminology

**Feed Features and Layout**
- The Feed
- Reposts
- Replies/Mentions
- Blocking
- Following
- Followers	
- Favorites

**Main Feed Layout and Elements**
- Required Channel Elements
- Optional Channel Elements
- Required Item Elements
- Optional Channel Elements
- Notes
- Sample Feed

**Alternate Feed Layout and Elements**
- Required Channel Elements
- Optional Channel Elements
- Required Item Elements
- Sample Feed

================================================================

# Overview

## What is this?

In recent years our internet communication has been increasingly controlled by single private companies. Facebook and Twitter account for an enormous percentage of online communication. This isn't good. Private companies (that aren't treated as utilities) have a number of factors that prevent them from being pure communications networks. Private companies need to make money, then need to constantly make *more* money, and they need to serve changing needs. They need to upgrade their service and add "features". This means that their goals will never align entirely with the goal of open, untampered internet communication. There's one more problem: Private companies can die. They go away. Twitter and Facebook sit high now, but in 10 years? 5 years even? Will they still be around? Hard to say. Communications that are tied to services and companies like this will die with the companies that built them. This is the problem that the Open Microblog tries to solve.

The Open Microblog is a proposed standard for an open and easy to implement internet communication mechanism. It is based on the success of RSS and is platform independent. It allows for most of the features that services like Twitter and Facebook provide but in an open way.

## What is it used for?

Open Microblogger is an open standard for a distributed, real-time, internet based communications service. Using a model based on RSS, Open Microblogger allows any developer, or savvy user to build and host their own microblogging service modeled after Twitter. The biggest upside to Open Microblogger is that it isn't controlled by a central corporation or body thus it remains, like RSS, outside the realm of corporate reach.

Social Networks are the cornerstone of the modern internet world. People all over the world use them to communicate with each other. The importance of this information being tamper-free and delivered in real-time is one thing that services like Twitter have excelled at recently. However services like Twitter and Facebook are controlled by a single entity, the fate's of all the information they carry is dictated by the needs of that particular company needing to make money. This means that our communication, the things we use to share events and news around the world is controlled by a single company and it's pockets.

Information regarding world events, social injustice, and social upheaval is just too much to allow a single corporation to handle. Not for any act of malevolence by that company but rather because companies need to make money, and if they don't they could disappear. If Twitter disappeared tomorrow, the world would almost certainly cease to hear about events all over the world and would have to go backward to other means. The idea of Twitter, of instant access to the information you want from the source is too good to let die or be corrupted. That is the mission of Open Microblogger, to create a standard by which anyone can develop a system, free of corporate overlords, that users can use to plug into the web of information that is microblogging.

## Why not just use RSS? It's already there...

True, but the Open Microblogger Standard allows for more social interaction and functionality than the broadcast-only medium that is RSS. Open Microblogger is meant to supplement RSS as another means of communicating. You'll see further down, there is a lot that Open Microblogger can do that RSS just can't.

## How does it work?

Open Microblog is an XML format that models a user's interactions and status updates. A user's public data, on any given service, is laid out in 3 XML files: the user's Feed, their block list, and their following list.

### The Feed

The feed is the main file that contains the connections to and information about a given user. The Feed XML file contains a list of the user's most recent posts as well as their profile information such as their username, user id, and bio information as well as a link to the public URL of the feed. At this point the Feed may sound like a typical RSS feed, and that is intended. In addition, the Feed contains a couple of important links to other pieces of the user's information; these elements are the next\_node, blocks, and follows elements. 

The first one, the next\_node element contains a link to the previous set of user posts. For fast and responsive feeds, the main Feed XML file is paginated in a standard way. For more information see Feed Paging.

#### Special Notes about the Feed

A given user wanting to subscribe to, or "Follow" another user needs only the Feed URL of the user in question. From this one URL it is possible to garner all other public information about a given user. The URL of the user's feed is the head node to which all other files link back to and branch off from.

### Blocks

The blocks XML file](#block) is linked to from the main Feed URL and contains an itemized list of the users (including user ids, usernames, and user link URLs) that the user has chosen to block. If this list becomes longer than 500 kB or 500 items, then it should be paginated as noted in the [Feed Paging section.

### Follows

The follows XML file](#following) is linked to from the main Feed URL and contains an itemized list of the users (including user ids, usernames, and user link URLs) that the user has chosen to follow. If this list becomes longer than 500 kB or 500 items, then it should be paginated as noted in the [Feed Paging section.

## Why doesn't it have a cool name?

I know, the name is terrible. I haven't thought of a good one yet.

## Terminology

_User_: A person/company who has an account. This may also mean the account that belongs to a given person/company.

_Client_: An application used for viewing, posting, or sharing content on this service (web site, mobile app, etc).

_Service_: An application (usually a web based service) that provides data aggregation and collection capabilities (i.e. the feed crawling servers, etc).

_Standard's Level_: Any functionality or feature-set provided by the standard with no additional work required by the service or client.

_Service's Level_: Any functionality or feature-set provided by a given service. Service Level tasks can be anything from post favoriting functionality, user search functionality, etc. In some cases (see Replies/Mentions) the Standard has formalized a set of guidelines for Service Level features/functionality.

================================================================

# Feed Layout and Features
## The Feed

Each user has a feed. This feed should follow the format listed in section 3. The feed represents the user's post history (what they've posted, reposted, and replies they've sent). This feed also contains certain metadata about the user including their username, user\_id, reply\_to information, and their most recent statuses.

Its important to remember that the feed holds the truth. There is not central database for user data, and all of a user's posts should be able to be found by traversing the feed and following public URLs found in it.

### Feed Paging

Due to the high volume of posts common to microblogs, the feed if left unchecked, could grow to be unwieldy in a short time. To combat this it is recommended that a user's feed be paginated to include no more that the user's 500 most recent posts or the most recent posts for a feed file size of up to 500 KB, whichever comes first. This should keep the file size small enough to be easily transmitted over the web. 

Once a given XML file has surpassed the recommended limits provided, it should be moved, as is (do not remove the header information, simply copy it) to a new public location. A new, empty XML file should be inserted at the user's root URL (the header information should be added at the top of this new page) and a next\_node tag should be inserted with a link to the new location of the old page. This will allow the files to remain as static as possible and the archive of all the user's posts is preserved. In practice, the user would have a multitude of these XML files all linking to each other like a singly-linked-list, each with a URL to the next node and the head node.

### Relocation, What happens if the user changes services?

The crucial feature of Open Microblog is that it is designed to be platform and service independent. Users have the ultimate choice to stop, start, relocate, and remove their data from a service at will. In order to migrate services easily, and without losing followers, services should provide a mechanism for users to input a redirect URL in their feed. This item is denoted with the relocate tag. This tag should _only_ be present if the user is relocating; it should never be empty. The value in that tag is the URL of the user's new feed. This tag should give the followers of said user adequate time to migrate over to the new feed URL before the old service deletes the user's feed.

The relocate tag should only be present in the most recently updated page of the user's main feed. It is not necessary to add the relocate tag to previous pages.

#### Obligation of the old Service

If a user is choosing to leave your service, you have an obligation to keep their old feed public for at least 24 hours to allow the user's new choice of service to import the data.

#### Obligation of the new Service

Conversely, services that the user is migrating to, should prompt the user for a link to their old feed and copy it over to  their system. The old service is not obligated to keep that old feed around for long, so make sure to get it quickly.

#### Obligation of the Client

Clients who come across a \<relocate\> tag should immediately redirect their crawlers at this new feed URL. The old URL can be discarded and is considered dead.

## Reposts

Reposting (similar to Twitter's retweeting) is the posting of someone else's post to your own timeline. The information from the original post is preserved in the reposted tags, and includes data link original user\_id, status\_id, and a link to that user's feed.

## Replies/Mentions

Since a user will receive posts from all people/accounts that they follow, Replies/Mentions from those people are delivered automatically via the normal feed. It is up to the service to determine whether or not to show users all mentions or just the ones to people the user also follows (though the latter is recommended).

The question remains, what of Replies/Mentions from those that a user doesn't follow? Due to the broadcast-only nature of the standard this feature must be delegated to the Service Level, though the standard does provide a simple and standardized way for services to provide this feature to users easily.

### Mentions URLs

In the channel declaration an optional element can be declared called reply\_to. If a given service chooses to implement this feature, the reply\_to element contains a simple set of elements that allow the client to form a URL string with the required data to the service of the user being replied to. Services opting-in to Mentions should be able to receive URL request messages from this URL and pass them on to the user they belong to.

## Blocking

Due to the distributed and therefore uncurated nature of this communication network some users may wish to ban others from following/messaging them. This is a service level feature. Services must implement this feature independently, however a preferred format is provided for listing accounts the user wished blocked from contacting them. This will help the user retain these blocking options if they chose to migrate to another service. An optional tag may be inserted into the user's feed which links to the file that describes the user's blocking preferences. See Additional Feeds.

Services should give the user's the option of making this feature publicly visible or not.

## Following 

Just like with RSS, users are given a list of statuses in their timeline of the posts of people/accounts they follow. Similarly to blocking, the implementation of Following a user is up to the service, however a preferred format is provided. An optional tag may be included in the user's main feed which links to the user's followers list. See Additional Feeds.

Services should give the user's the option of making this feature publicly visible or not.

## Followers

Followers (just like with Twitter) are people that will receive posts from a given user. A user will often have multiple followers. 

Because of the distributed nature of the system, gauging exact follower counts becomes challenging and as of version 0.1 there is no way to determine exactly the number of followers a given user has.


Coming soon. Finalizing details.

================================================================

# Main Feed Layout and Elements

## Required Channel Elements

- username: A Twitter-like username. Must no greater than 25 characters. 
- user\_id: A universally unique (or as close as possible) id. This identifies the user.
- link: URL to the feed. If the feed is paginated, then the link to the most recent page. 
- language: The main language for the feed. 
- lastBuildDate: The date and time that the last item was added to the feed.

## Optional Channel Elements

- docs: URL to documentation of the feed (if available).
- next\_node: A URL to the next previous set of items.
- description: A brief bio of the user. Like Twitter bios (surrounded with <\!\[CDATA\[\]\]> tags).
- user\_full\_name: The user's first and last name. Used for display purposes.
- blocks: A public URL to the XML feed of the user's block list.
	- count: An attribute of the blocks tag that lists the total number of items in the blocked users in the list.
- follows: A public URL to the XML feed of the users that a given user follows.
	- count: An attribute of the follows tag that lists the total number of users that a given user follows.

## Required Item Elements

- status\_id: A unique, incrementing integer starting from 0 representing the item.
- pubdate: The datetime when the status was posted.
- description: The HTML text of the post (surrounded with <\!\[CDATA\[\]\]> tags).

## Optional Item Elements
 	
### Replies
 
- in\_reply\_to\_user\_id: The user\_id of the user being replied to.
- in\_reply\_to\_status\_id: The status\_id of the post that is being replied to.
- in\_reply\_to\_user\_link: A link to the feed of the user that is being replied to.

### Reposts
 
- reposted\_status\_user\_id: The user\_id of the user who originally posted the status.
- reposted\_user\_link: A link to the original user's feed.
- reposted\_status\_id: The status\_id of the original user's post.
- reposted\_status\_pubdate: The pubdate of the original user's post.

### Miscellaneous

- language: The language of the status. Recommended if the language is different than the feed language.

## Notes

- Feed should be UTF-8 Encoded.

## Sample Feed

The feed below contains _all_ the possible elements in a single feed. Keep in mind that not all of these elements will be present at one time.
``` xml
<rss xmlns:content="http://purl.org/rss/1.0/modules/content/" version="2.0">
	<channel>
		<!-- User Info -->
		<username></username>
		<user_id></user_id>
		<user_full_name></user_full_name>
		<description><![CDATA[]]></description>
		<!-- Feed Metadata -->
		<link></link>
		<next_node></next_node>
		<relocate></relocate>
		<blocks count=""></blocks>
		<follows count=""></follows>
		<!-- Reply and Mention URL -->
		<reply_to>
			<url></url>
			<reply_to_user></reply_to_user>
			<reply_to_status></reply_to_status>
			<reply_from_user_id />
			<reply_status_id />
			<user_link />
		</reply_to>
		<!-- Misc. -->
		<docs></docs>
		<language></language>
		<lastBuildDate></lastBuildDate>
		<item>
			<!-- Status Update -->
			<status_id></status_id>
			<pubdate></pubdate>
			<description><![CDATA[]]></description>
			<!-- Replying -->
			<in_reply_to_status_id></in_reply_to_status_id>
			<in_reply_to_user_id></in_reply_to_user_id>
			<in_reply_to_user_link></in_reply_to_user_link>
			<!-- Reposting -->
			<reposted_status_id></reposted_status_id>
			<reposted_status_pubdate></reposted_status_pubdate>
			<reposted_status_user_id></reposted_status_user_id>
			<reposted_status_user_link></reposted_status_user_link>
			<!-- Misc. -->
			<language>en</language>
		</item>
	</channel>
</rss>
```
================================================================

# Alternate Feed Layout and Elements

## Required Channel Elements

- username: A Twitter-like username. Must no greater than 25 characters. 
- user\_id: A universally unique (or as close as possible) id. This identifies the user.
- link: URL to the blocks or follows feed. If the feed is paginated, then the link to the most recent page. 
- lastBuildDate: The date and time that the last item was added to the feed.

## Optional Channel Elements

- next\_node: A URL to the next previous set of items.

## Required Item Elements

- user\_id: The id of the user being blocked or followed.
- user\_name: The username of the user being blocked or followed.
- user\_link: A link to the feed of the user being blocked or followed.

## Notes

- Feed should be UTF-8 Encoded.

## Sample Feed

The feed below contains _all_ the possible elements in a single feed. Keep in mind that not all of these elements will be present at one time.
``` xml
<rss xmlns:content="http://purl.org/rss/1.0/modules/content/" version="2.0">
	<channel count="">
		<username></username>
		<user_id></user_id>
		<link></link>
		<next_node></next_node>
		<lastBuildDate></lastBuildDate>
		<item>
			<user_id></user_id>
			<user_link></user_link>
			<user_name></user_name>
		</item>
	</channel>
</rss>
```
