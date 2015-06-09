# Proposed New Repost/Reply Nodes for Item elements

This is a preliminary document proposing a new syntax for replies and reposting.

## Old:

```
<item>
	<!— Status Update —>
	<guid isPermalink="false"></guid>
	<pubdate></pubdate>
	<description><![CDATA[]]></description>
	<!— Reply and Mention URL —>
	<microblog:reply></microblog:reply>
	<!— Replying —>
	<microblog:in_reply_to_status_id></microblog:in_reply_to_status_id>
	<microblog:in_reply_to_user_id></microblog:in_reply_to_user_id>
	<microblog:in_reply_to_user_link></microblog:in_reply_to_user_link>
	<!— Reposting —>
	<microblog:reposted_status_id></microblog:reposted_status_id>
	<microblog:reposted_status_pubdate></microblog:reposted_status_pubdate>
	<microblog:reposted_status_user_id></microblog:reposted_status_user_id>
	<microblog:reposted_status_user_link></microblog:reposted_status_user_link>
	<!— Misc. —>
	<language>en</language>
</item>
```

## New:

```
<item>
	<!— Status Update —>
	<guid isPermalink="false"></guid>
	<pubdate></pubdate>
	<description><![CDATA[]]></description>
	<!— Reply and Mention URL —>
	<microblog:reply></microblog:reply>
	<!— Replying —>
	<microblog:to userId="a guid goes here">[a link goes here]</microblog:to>
	<!— Reposting —>
	<microblog:from userId="a guid goes here">[a link goes here]</microblog:from>
	<!— Either replies or reposts —>
	<microblog:regarding>[the id being replied to]</microblog:regarding>
	<!— Misc. —>
	<language>en</language>
</item>
```
