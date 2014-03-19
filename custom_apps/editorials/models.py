from django.db import models
from photologue.models import Gallery


class Category(models.Model):
	category = models.CharField(max_length=255, )
	
	def __unicode__(self):
		return self.category

	class Meta:
		verbose_name_plural = "categories"


class Editorial(models.Model):
    active = models.BooleanField(default=True,)
    title = models.CharField(max_length=255, )
    details = models.TextField()


    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/exhibitions/%i/" % self.id
        

