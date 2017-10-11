from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class App(models.Model):
	IOS = 'i'
	ANDROID = 'a'
	PLATFORM_CHOICES = (
        (IOS, 'iOS'),
        (ANDROID, 'Android')
    )
	name = models.CharField(max_length=50)
	description = models.TextField(max_length=200, null=True, blank=True)
	platform = models.CharField(max_length=1, choices=PLATFORM_CHOICES, default=IOS)
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.name + '/' + self.platform 

	def get_absolute_url(self):
		return reverse ('appStore:detail', kwargs={'pk': self.pk})

	def platform_description(self):
		for choice in self.PLATFORM_CHOICES:
			if choice[0] == self.platform:
				return choice[1]
		return ''
