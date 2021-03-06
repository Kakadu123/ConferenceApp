#Conference Central App Engine application

## Task 1: Add Sessions to a Conference

Sessions are child objects of Conference. There are default values for duration: 30 and TypeOfSession: NOT_SPECIFIED. TypeOfSession is an enum field. Speaker is a string field within the Session entity. There is additional field websafeSessionKey as urlsafe Session key is required in multiple methods. I followed the suggestion from Jeff suggested on forum: https://discussions.udacity.com/t/how-to-find-entity-keys-in-developers-console/28207/4 

**Methods**:

* createSession - Create Session object.
* getConferenceSessions - Return requested sessions (by websafeConferenceKey).
* getSessionsBySpeaker - Return requested sessions (by speaker).
* getConferenceSessionsByType - Return requested sessions (by conference and SessionType). Date field is in "%Y-%m-%d" format.


## Task 2: Sessions in User Wishlist 
Sessions in wishlist are handled as string values of session keys. Repeated values are allowed in Profile model.

**Methods**:

* addSessionToWishlist(SessionKey) - Add sessions to user wishlist via private method: _updateSessionToWishlist
* delSessionFromWishlist - Add sessions to user wishlist via private method: _updateSessionToWishlist
* getSessionsInWishlist - Get a list of sessions that user has added to wishlist.


## Task 3: Work on indexes and queries
**2 new queries**:

* getLongestSession - Get the session with the longest duration.
* getListOfUniqueSpeakers - Get a comma separated list of unique speakers.

**Indexes**

To fix indexing issue, I used automatical update of indexes whenever the dev_appserver detects that a new type of query is run.

**All non-workshop sessions before 7 pm**

There are query restrictions in GAE due to the fact that performance of queries does not depend on the amount of data stored but the actual size of the result set. This involves restriction on inequality filters. Inequality filter can be applied to at most one property and the requirement for Task 3 requires inequality filter for 2 different properties. Due to this limitation I itirated over the filtered result set (non-workshop entities) to retrieve only those entities that start before 7pm.


## Task 4: Featured speaker
getFeaturedSpeaker method returns Featured Speaker from memcache. 
Featured Speaker Announcement & assignment to memcache is done by private method _cacheSpeaker that assigns speaker to memcache if there is more than 1 session by the most recently added speaker for a given conference. Otherwise, the previous featured speaker or blank value is left.


# Setup Instructions
1. Change `application` value in `app.yaml` to your app ID from the App Engine admin console.
2. Change IDs in `settings.py` to your IDs from the admin console.
3. Change CLIENT_ID in `static/js/app.js` to your Web client ID.
4. Run and Deploy your application in Google App Engine Launcher.
