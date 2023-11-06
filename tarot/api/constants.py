

"""

-------------------------------------------------------------------

WHY STORE THE TAROT DECK AS CONSTANTS?

Originally I had stored each Card as a Django model. This was
an OOP instinct because each Reading contains Card objects.
However, after writing some of the API endpoints, I realized
that the tarot deck will never be modified by the end user,
and therefore it makes more sense to store as constants.

ADVANTAGES: (1) Code should never be more complex than it has
to be. Storing tarot cards as constants is much more lightweight
than storing as Django models - eg. no serializer needed. After
I refactored the code, it was much simpler and lighter. (2) Avoids
unnecessary database queries which is important for speed. For
example, if Card is a foreign key on Reading, then every time
you access a Reading, you'll have to join the Card table to get
the explanation of a card. Storing cards as constants avoids
this issue. In a production environment with large tables, this
makes a huge difference.

DISADVANTAGES: The primary disadvantage of storing as a constant
is that if you ever need to make changes, it would require a code
change and redeploy which could be cumbersome in a production
environment - whereas if stored as a database model, a quick change
could be made from the Django admin panel. That said, the data in
a tarot deck is stable enough that this should rarely be an issue.

-------------------------------------------------------------------

WHY STORE THE TAROT DECK ON THE FRONTEND?

Following the thought process above, I then stored the tarot deck
as constants on the backend. Then after writing more code - realized
that there is an even better solution.

ALTERNATIVE: If the tarot deck is truly a *display* constant and the
data in it will not be used by the backend logic - could store this
as a constant on the *frontend* instead. This would even avoid extra
API calls. Consider this as I develop the app further.

^^ Now I am leaning toward this because as I write the API views to
get the tarot deck, I realize that (a) it does not map to the model
which is the whole point of DRF (b) sending a lot of unnecessary
data over the wire if so.

After doing this - it's clear that this is the right decision - because
the API endpoints for getting the tarot deck never made sense under
the DRF philosophy. If I look at the code that I ripped out - this
makes total sense - because the code that I ripped out had a lot of
caveats and todos bc it simply didn't make sense to do this as an
endpoint.

Disadvantage - no conceptual source of truth. If this were a
production API, would probably still have an endpoint to fetch
these constants as a "source of truth" and the individual frontend
developer can decide whether to use API calls to fetch the source of
truth, or use their own frontend constants.

# TODO: Clean up the explanation above.

-------------------------------------------------------------------

"""


TAROT_DECK = {
    'ace of pentacles': 'make your dreams into reality through tangible action',
    'two of pentacles': 'todo',
    'three of pentacles': 'todo',
    'four of pentacles': 'todo',
    'five of pentacles': 'todo',
    'six of pentacles': 'todo',
    'seven of pentacles': 'todo',
    'eight of pentacles': 'todo',
    'nine of pentacles': 'todo',
    'ten of pentacles': 'todo',
    'page of pentacles': 'todo',
    'knight of pentacles': 'todo',
    'queen of pentacles': 'todo',
    'king of pentacles': 'todo',
    'ace of swords': 'newfound mental clarity, cut through the noise',
    'two of swords': 'todo',
    'three of swords': 'todo',
    'four of swords': 'todo',
    'five of swords': 'todo',
    'six of swords': 'todo',
    'seven of swords': 'todo',
    'eight of swords': 'todo',
    'nine of swords': 'todo',
    'ten of swords': 'todo',
    'page of swords': 'todo',
    'knight of swords': 'todo',
    'queen of swords': 'todo',
    'king of swords': 'todo',
    'ace of wands': 'newfound energy, powerful, strong, take action',
    'two of wands': 'todo',
    'three of wands': 'todo',
    'four of wands': 'todo',
    'five of wands': 'todo',
    'six of wands': 'todo',
    'seven of wands': 'todo',
    'eight of wands': 'todo',
    'nine of wands': 'todo',
    'ten of wands': 'todo',
    'page of wands': 'todo',
    'knight of wands': 'todo',
    'queen of wands': 'todo',
    'king of wands': 'todo',
    'ace of cups': 'new spark of emotions, something you love, passion',
    'two of cups': 'todo',
    'three of cups': 'todo',
    'four of cups': 'todo',
    'five of cups': 'todo',
    'six of cups': 'todo',
    'seven of cups': 'todo',
    'eight of cups': 'todo',
    'nine of cups': 'todo',
    'ten of cups': 'todo',
    'page of cups': 'todo',
    'knight of cups': 'todo',
    'queen of cups': 'todo',
    'king of cups': 'todo',
    'fool': 'todo',
    'magician': 'todo',
    'high priestess': 'todo',
    'empress': 'todo',
    'emperor': 'todo',
    'hierophant': 'todo',
    'lovers': 'todo',
    'chariot': 'todo',
    'strength': 'todo',
    'hermit': 'todo',
    'wheel of fortune': 'todo',
    'justice': 'todo',
    'hanged man': 'todo',
    'death': 'todo',
    'temperance': 'todo',
    'devil': 'todo',
    'tower': 'todo',
    'star': 'todo',
    'moon': 'todo',
    'sun': 'todo',
    'judgment': 'todo',
    'world': 'todo',
}


CELTIC_CROSS = {
    1: {
        'name': 'heart of the matter',
        'explanation': 'todo need to write this',
    },
    2: {
        'name': 'what crosses you',
        'explanation': 'todo need to write this',
    },
    3: {
        'name': 'below',
        'explanation': 'todo need to write this',
    },
    4: {
        'name': 'recent past',
        'explanation': 'todo need to write this',
    },
    5: {
        'name': 'above',
        'explanation': 'todo need to write this',
    },
    6: {
        'name': 'near future',
        'explanation': 'todo need to write this',
    },
    7: {
        'name': 'self',
        'explanation': 'todo need to write this',
    },
    8: {
        'name': 'environment',
        'explanation': 'todo need to write this',
    },
    9: {
        'name': 'guidance',
        'explanation': 'todo need to write this',
    },
    10: {
        'name': 'outcome',
        'explanation': 'todo need to write this',
    },
}
