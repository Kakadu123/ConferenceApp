#!/usr/bin/env python

"""
main.py -- Udacity conference server-side Python App Engine
    HTTP controller handlers for memcache & task queue access

$Id$

created by wesc on 2014 may 24

"""

__author__ = 'wesc+api@google.com (Wesley Chun)'

import webapp2
from google.appengine.api import app_identity
from google.appengine.api import mail
from conference import ConferenceApi

import logging

class SetAnnouncementHandler(webapp2.RequestHandler):
    def get(self):
        """Set Announcement in Memcache."""
        ConferenceApi._cacheAnnouncement()
        self.response.set_status(204)

#############     Task 4:  Memcache Featured Speaker in a Task      #############

# When a new session is added to a conference, check the speaker.
# If there is more than one session by this speaker 
# at this conference, also add a new Memcache entry that 
# features the speaker and session names.

class VerifyFeaturedSpeakerHandler(webapp2.RequestHandler):
    def post(self):
        """Assign to memcache entry if a speaker has more than one session"""
        # logging.info('VerifyFeaturedSpeakerHandler entered')
        ConferenceApi._cacheSpeaker(self)
        self.response.set_status(204)


class SendConfirmationEmailHandler(webapp2.RequestHandler):
    def post(self):
        """Send email confirming Conference creation."""
        mail.send_mail(
            'noreply@%s.appspotmail.com' % (
                app_identity.get_application_id()),     # from
            self.request.get('email'),                  # to
            'You created a new Conference!',            # subj
            'Hi, you have created a following '         # body
            'conference:\r\n\r\n%s' % self.request.get(
                'conferenceInfo')
        )


app = webapp2.WSGIApplication([
    ('/crons/set_announcement', SetAnnouncementHandler),
    ('/tasks/send_confirmation_email', SendConfirmationEmailHandler),
    ('/tasks/verify_featuredSpeaker', VerifyFeaturedSpeakerHandler),
], debug=True)
