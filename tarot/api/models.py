from django.db import models


class Card(models.Model):
    """
    Considered (re)naming this to TarotCard to be more explicit.
    Decided not to because it creates potential for naming inconsistency
    and therefore bugs down the road, ie. some places using tarotcard, tarot_card, card, etc.
    One single word is easier to remember for consistency.
    """
    title = models.CharField(max_length=100, default='')
    explanation = models.TextField()


class ReadingSingle(models.Model):
    """
    TODO: Model used for a single card reading
    """
    pass


class ReadingCross(models.Model):
    """
    Originally called TarotReadingCross - changed to ReadingCross
    to be consistent with Card - for same reasons as documented in docstring
    for Card model.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    date_of_reading = models.DateField()  # Note this is NOT the same as the date the database record was created
    question_asked = models.TextField()
    # TODO: Originally was ForeignKey
    # Storing them as numerical ids right now
    # So that I can chunk the coding work
    # And because I'm considering moving Card model to a constant instead
    #
    # Storing these as CharField rather than IntegerField
    # Because it makes more sense to refer to tarot cards that way
    # And it's short enough to search easily in dict
    pos1_card = models.CharField(max_length=100, default='')
    pos2_card = models.CharField(max_length=100, default='')
    pos3_card = models.CharField(max_length=100, default='')
    pos4_card = models.CharField(max_length=100, default='')
    pos5_card = models.CharField(max_length=100, default='')
    pos6_card = models.CharField(max_length=100, default='')
    pos7_card = models.CharField(max_length=100, default='')
    pos8_card = models.CharField(max_length=100, default='')
    pos9_card = models.CharField(max_length=100, default='')
    pos10_card = models.CharField(max_length=100, default='')
    # TODO: I realized this is better stored as constants also
    # pos1_meaning = models.TextField()
    # pos2_meaning = models.TextField()
    # pos3_meaning = models.TextField()
    # pos4_meaning = models.TextField()
    # pos5_meaning = models.TextField()
    # pos6_meaning = models.TextField()
    # pos7_meaning = models.TextField()
    # pos8_meaning = models.TextField()
    # pos9_meaning = models.TextField()
    # pos10_meaning = models.TextField()
    pos1_mytake = models.TextField(blank=True)
    pos2_mytake = models.TextField(blank=True)
    pos3_mytake = models.TextField(blank=True)
    pos4_mytake = models.TextField(blank=True)
    pos5_mytake = models.TextField(blank=True)
    pos6_mytake = models.TextField(blank=True)
    pos7_mytake = models.TextField(blank=True)
    pos8_mytake = models.TextField(blank=True)
    pos9_mytake = models.TextField(blank=True)
    pos10_mytake = models.TextField(blank=True)
    pos1_recap = models.TextField(blank=True)
    pos2_recap = models.TextField(blank=True)
    pos3_recap = models.TextField(blank=True)
    pos4_recap = models.TextField(blank=True)
    pos5_recap = models.TextField(blank=True)
    pos6_recap = models.TextField(blank=True)
    pos7_recap = models.TextField(blank=True)
    pos8_recap = models.TextField(blank=True)
    pos9_recap = models.TextField(blank=True)
    pos10_recap = models.TextField(blank=True)
