Why I chose this project: # TODO fill out
1) interesting topic to keep me engaged
2) very constrained set of tasks - so I can focus on technical decisions and visual UX design - rather than conceptualizing the functionality of the app. function is super clear and constrained.

Explanation of this log: # TODO fill out
- Show that I can chunk work appropriately / break down into tickets / stage the appropriate order to do things in / start small and build
- Comments in the code will explain my technical decisions - similar to discussion that would be on pull requests. TODO: record for interview prep - what I struggle with is culture around PRs and tone being hard to interpret when written, hierarchy.

DAY 1 (2 hours)

* Sketch out design and functionality of app
* Rough outline of project technical components

DAY 2 (2 hours)

* Set up github repo
* Set up toolchain
* Django boilerplate
* CHECKPOINT: First commit to github

DAY 3 (1 hour)

* Get the first schema and view working from Django REST Framework
* Achieved! Only took an hour :)
* And also solved some minor bugs
* CHECKPOINT: Can call first API endpoint locally through browser

DAY 4 (2 hours)

* Refactor to class-based views per the Django REST Framework tutorial (why didn't they just say that from the beginning...)
* Manually retest in the browser and everything works - same place as I was on Day 3, just refactored.
* Annoyed with manual testing - seems like a good time to write a unit test suite. So I did.
* CHECKPOINT: Test suite passes locally for 3 API endpoints

DAY 5 (2 hours)

* Add model for ReadingCross and skeleton of views for CRUD ReadingCross
* Details of how to store a reading are more complicated than I expected and causing me to refactor how I store tarot cards - makes more sense to store tarot cards as a constant rather than model as it will never be updated. Also avoids unnecessary database queries.
* CHECKPOINT: Test suite passes locally for skeleton of 1 new API endpoint

NEXT
* NEXT: Add constants file for use in ReadingCross but don't delete the old Card code yet
* NEXT: Build out test suite and additional views for ReadingCross until complete
* NEXT: Add validation for ReadingCross views.
* TODO: Figure out how to handle card images
* TODO: Rip out the Card model as not needed
* TODO: Add User model and validation to ReadingCross views
* Goal: Get all of the API endpoints working locally
* Goal: Write test suite to cover all the API endpoints
* Goal: Deploy and able to call API endpoints from non-local server



