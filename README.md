# hms_udn #

# What's this repo for? #
This repo is a sample test app to create a website from Django and Python.
* It contains a simple list view of "participants"
* A form for creating new participants
* Reused from (from create) to update participants
* And an AJAX call from the list view to update a status field not found in the create/update forms.

# How do I get set up? #

## Dependencies ##
The dependencies for this application are:
* Python 3.6.2
* Django 1.9.13
  * Pease note, this version of Django is no longer supported. Version 1.11 or higher should be used.

## Setup ##
Clone the repo:
  `git clone https://github.com/mczabaj/hms_udn.git`

Starting the app:
  `python manage.py runserver`

# Enhancements #

## Security ##
What can/could be done to secure this site in the future to restrict access?
* If this site is for internal use at the company, and not meant for general public use,
  * you could hook up to some internal authorization mechanism like AD or LDAP to grant access to specific users within the organization.
* If this site is for public use, it would great to be able let people register (username/email/password, etc) to create a participant.
  * that way, if/when they come back they can see the status of just their record.
  * additionally, the general list view could have just participant ids and the status (pending review or reviewed)
  * I would suggest using Open ID Connect for the authentication/authorization. I've built my own before, and unless you want to be in the business of managing accounts, rotating keys, etc. let someone else manage it and just an open source oidc library.

## UI/UX ##
What could be done to change the existing flow to make it more dynamic from a UI/UX perspective?
* Default landing page could be the list view, if that's what most people are coming to see. Rather than the landing page being a blank form.
  * From there, new participant records could be added
* If registration is going to be part of the flow, you could totally "hide" the gathering of personal info as part of registration so the app isn't asking for duplicate data it should already have.
* Verify the users' registered email so it can be used for
  1) resetting forgot passwords,
  2) notifications to the participant, for example, if the status changes from "pending review" to one of the "reviewed" statuses.
