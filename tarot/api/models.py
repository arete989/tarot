from django.db import models


class SingleReading(models.Model):
    """
    Model used for a single card reading.
    """
    pass  # TODO


class CrossReading(models.Model):
    """
    Model used for a Celtic Cross reading.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    date_of_reading = models.DateField()  # Note this is NOT the same as the date the database record was created
    question_asked = models.TextField()
    # TODO: Clean up this comment
    # Originally was ForeignKey
    # Storing them as numerical ids right now
    # So that I can chunk the coding work
    # And because I'm considering moving Card model to a constant instead
    # -------------------------------------------------------------------
    # Storing these as CharField rather than IntegerField
    # Because it makes more sense to refer to tarot cards that way
    # And it's short enough to search easily in dict
    pos1_card = models.CharField(max_length=100)
    pos2_card = models.CharField(max_length=100)
    pos3_card = models.CharField(max_length=100)
    pos4_card = models.CharField(max_length=100)
    pos5_card = models.CharField(max_length=100)
    pos6_card = models.CharField(max_length=100)
    pos7_card = models.CharField(max_length=100)
    pos8_card = models.CharField(max_length=100)
    pos9_card = models.CharField(max_length=100)
    pos10_card = models.CharField(max_length=100)
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
