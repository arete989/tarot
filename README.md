Why I chose this project: # TODO fill out

1) very constrained set of tasks (vs the health tracker app that I was considering building) - so I can focus on technical decisions and frontend implementation details, adding extra polish - rather than conceptualizing the functionality of the app. function is super clear and constrained.
2) interesting topic to keep me engaged. I had fun working on this! also a niche topic so I didn't feel like I was building the same set of restaurant review / blogging and notes app / daily tracker app that's been done a bunch of times before. -- tackle a new type of problem which is fun for me to do! -- also show diversity of what can be done with code - a traditionally feminine topic. maybe kind of a litmus test for culture fit? -- want to work somewhere that celebrates this kind of quirkiness and individuality.

Explanation of this log: # TODO fill out
- Show that I can chunk work appropriately / break down into tickets / stage the appropriate order to do things in / start small and build
- Comments in the code will explain my technical decisions - similar to discussion that would be on pull requests. / show my thought process and how I learn
- Example of design decision: [link to constants.py] for storing as constants and in [views.py] regarding how to structure endpoints so not sending lots of data over the wire

NOTES TO SELF (this is for interview prep)
- weaknesses: (1) culture around PRs and giving feedback. tone is hard to read over written text. hierarchy. (2) senior? yes in terms of thinking about maintainability and structure, technical planning, looking at overall architecture. no in terms of repeated experience with industry-wide coding patterns and frameworks - depth/breadth of experience. simply need more data points, ie. once you work with 5-6 different frameworks, you can pick up on the commonalities between them all.
(for resume) -- link to github. readme documents my thought process, development process, and technical decision making.

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
* CHECKPOINT: Test suite passes locally for 3 API endpoints.

DAY 5 (2 hours)

* Add model for ReadingCross and skeleton of views for CRUD ReadingCross
* Details of how to store a reading are more complicated than I expected and causing me to refactor how I store tarot cards - makes more sense to store tarot cards as a constant rather than model as it will never be updated. Also avoids unnecessary database queries.
* CHECKPOINT: Test suite passes locally for skeleton of 1 new API endpoint.

DAY 6 (2 hours)

* Rip out a bunch of code. I actually have LESS code than I started with. T_T
* But makes more sense. Store tarot deck as display constants on the frontend rather than Django models. Took a lot of thinking and refactoring to get here.
* Less code is not a bad thing - cleaner, more maintainable. It's actually harder to write less + good/thoughtful code versus more code.
* A lot of thinking for such a little bit of code - but it pays off bc when I look at code I wrote 2 years ago and forgot about - it still makes sense and effortless to pick up - bc it was well organized from the start. Like an intuitive UX like the iPhone.
* CHECKPOINT: Test suite still passes after refactor.

DAY 7 (2 hours)
* Add validation to CrossReadingCreate API
* More tests for CrossReadingCreate API to cover more behavior
* Downside of using DRF serializers instead of explicit Django ORM - need to read documentation to learn the specifics of DRF serializers versus using already existing knowledge of Django ORM. Serializers are slightly less verbose and more reusable but is it worth the extra activation energy for a new specific framework and added layer? Also: magic behavior and less explicit equals harder to debug - you're debugging by reading docs instead of stepping through code. I'm still very skeptical of using too many abstractions that are specific to frameworks.
* Another downside of DRF serializers - their API error return schema really sucks. This is showing up when I write unit tests - grabbing the error is not intuitive and requires pdb to figure out the exact schema. And hard to customize the error schema because it's all wrapped up in the serializer abstraction.
* CHECKPOINT: Test suite now includes validation and still passes.

DAY 8 (2 hours)
* Build out all the views in CrossReadingById. This is where the serializer shortens some code.
* Write test coverage for CrossReadingById. The part that took the longest was getting freeze_time and datetime formats to work correctly for test purposes. Was important to get this right from the start bc IME when tests fail randomly, this is often a cause.
* CHECKPOINT: Test suite includes CrossReadingById and passes.

NEXT
* NEXT: Build out the CrossReadingById class with test coverage
* NEXT: Wire up the URLs and write test coverage
* TODO: Add User model to ReadingCross views
* TODO: Figure out how to handle card images
* Goal: Get all of the API endpoints working locally
* Goal: Deploy and able to call API endpoints from non-local server



