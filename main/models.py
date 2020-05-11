from django.db import models
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.


class Donation(models.Model):
	amount = models.IntegerField(blank=False, null=False)
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.pub_date
	


class Comment(models.Model):
	name = models.CharField(max_length=50)
	comment = models.CharField(max_length=200)
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.name

class Outreach(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField(default="Nothing yet")
	location = models.CharField(max_length=200, default="No where")
	image = models.ImageField(upload_to='main/outreach_image/')
	comments = models.ManyToManyField(Comment, through="OutreachCommentConnector")
	pub_date = models.DateTimeField(default=timezone.now)
	slug = models.SlugField(unique=True)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super().save(*args, **kwargs)
		
	def get_absolute_url(self):
		return "/outreach/%s/"%self.slug
		
	def __str__(self):
		return self.title
    	
    	
    	
    
class Member(models.Model):
	name = models.CharField(max_length=100)
	post = models.CharField(max_length=100)
	bio = models.TextField(default="Nothing yet")
	image = models.ImageField(upload_to='main/member_image/')
	pub_date = models.DateTimeField(default=timezone.now)
	slug = models.SlugField(unique=True, default="ray slug")
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)
		
	def get_absolute_url(self):
		return "/member/%s/"%self.slug
		
	def __str__(self):
		return self.name
    	
    	
    	
    	
class Event(models.Model):
	title = models.CharField(max_length=100)
	#video = models.FileField(upload_to='project/event/video/', null=True, verbose_name="")
	video_url = models.TextField(default="Nothing yet")
	pub_date = models.DateTimeField(default=timezone.now)


	def __str__(self):
		return self.title
	
	
	
	
class OutreachCommentConnector(models.Model):
	outreach = models.ForeignKey(Outreach, on_delete=models.CASCADE, default="")
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE, default="")
	pub_date = models.DateTimeField(default=timezone.now)
	
	
	

