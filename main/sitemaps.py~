from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Outreach, Member


class StaticViewSitemap(Sitemap):
	changefreq = "always"
	
	def items(self):
		return ["index", "about"]
		
	def location(self, item):
		return reverse(item)


class OutreachSitemap(Sitemap):
	
	def items(self):
		return Outreach.objects.all()
		
		
class MemberSitemap(Sitemap):
	
	def items(self):
		return Member.objects.all()

