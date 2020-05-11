from django.shortcuts import render, get_object_or_404
from .models import Outreach, Member, Event, OutreachCommentConnector, Donation
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from django.core.mail import send_mail
from django.conf import settings


#########################main shit starts here ###########################

def PreDonationFunc(request):

	if request.method == "POST":
		amount = request.POST.get("amount")
		pub_date = timezone.now()	
		donation = Donation.objects.create(amount=amount, pub_date=pub_date)
		donation.save()
		return HttpResponseRedirect(reverse("donation", args=(donation.id,)))
		
	else:
		return render(request, 'main/pre_donation.html')
		
		
def DonationFunc(request, donation_id):

	if request.method == "POST":
		pass
		
	else:
		donation = Donation.objects.get(id=donation_id)
		context = {"donation": donation}
		return render(request, 'main/donation.html', context)
		


def IndexFunc(request):
	
	if request.method == "POST":
		pass
		
	else:
		event = Event.objects.order_by('-pub_date')[:1]
		events = Event.objects.order_by('-pub_date')[1:11]
		outreach = Outreach.objects.order_by('-pub_date')[:1]
		outreachs = Outreach.objects.order_by('-pub_date')[1:4]
		members = Member.objects.order_by('-pub_date')
		
		context ={"event": event, "events": events, "outreach": outreach, "outreachs": outreachs, "members": members}
		return render(request, 'main/index.html', context)
		
		
def ContactFunc(request):

	if request.method == "POST":
		try:
			name = request.POST.get("name")
			email = request.POST.get("email")
			message = request.POST.get("message")
			email_from = settings.EMAIL_HOST_USER
			recipient_list = ['muritalaibrahim097@gmail.com', 'odiagaraymondrayray@gmail.com'] #this would be funmi nehan in prodcution
			subject = 'message from %s.' % (name)
			main_msg = "hello, funmi nehan foundation.\n Here is an email from (%s). \n \n '%s' \n Reply to his/her email: %s " % (name, message, email)
			send_mail(subject, main_msg, email_from, recipient_list )
		except:
			pass

		return HttpResponse("email sent successfully")

		
	else:
		return render(request, 'main/contact.html')
	
	


def AboutFunc(request):

	members = Member.objects.order_by('-pub_date')
	context ={"members": members}
	return render(request, 'main/about.html', context)
	
	
	
def PostOutreachFunc(request):

	if request.method == "POST":
		title = request.POST.get("title")
		body = request.POST.get("body")
		image = request.FILES["image"]
		pub_date = timezone.now()
		
		outr = Outreach.objects.create(title=title, body=body, image=image, pub_date=pub_date, slug=title)
		outr.save()
		
		return HttpResponseRedirect(reverse("post_outreach"))
		
	else:
		outreachs = Outreach.objects.all()
		outreach_count = outreachs.count()
		context = {"outreach_count": outreach_count}
		#return HttpResponse(outreach_count)
		return render(request, 'main/post_outreach.html', context)
	
def PostMemberFunc(request):

	if request.method == "POST":
		name = request.POST.get("name")
		post = request.POST.get("post")
		bio = request.POST.get("bio")
		image = request.FILES["image"]
		pub_date = timezone.now()
		
		mb = Member.objects.create(name=name, post=post, bio=bio, image=image, pub_date=pub_date)
		mb.save()
		
		return HttpResponseRedirect(reverse("post_member"))
		
	else:
		members = Member.objects.all()
		member_count = members.count()
		context = {"member_count": member_count}
		#return HttpResponse(outreach_count)
		return render(request, 'main/post_member.html', context)
	
def PostEventFunc(request):

	if request.method == "POST":
		title = request.POST.get("title")
		video_url = request.POST.get("video_url") 
		pub_date = timezone.now()
		
		mb = Event.objects.create(title=title, video_url=video_url, pub_date=pub_date)
		mb.save()
		
		return HttpResponseRedirect(reverse("post_event"))
		
	else:
		events = Event.objects.all()
		event_count = events.count()
		context = {"event_count": event_count}
		#return HttpResponse(outreach_count)
		return render(request, 'main/post_event.html', context)




def GalleryFunc(request):
	
	if request.method == "POST":
		pass
		
	else:
		outreachs = Outreach.objects.order_by('-pub_date')
		members = Member.objects.order_by('-pub_date')
		events = Event.objects.order_by('-pub_date')
		context = {"outreachs": outreachs, "members": members, "events": events}
		
		return render(request, 'main/gallery.html', context)



def OutreachFunc(request):

	if request.method == "POST":
		pass
		
	else:
		outreachs = Outreach.objects.order_by('-pub_date')
		members = Member.objects.order_by('-pub_date')
		events = Event.objects.order_by('-pub_date')[1:6]
		event = Event.objects.order_by('-pub_date')[:1]
		context = {"outreachs": outreachs, "members": members, "events": events, "event": event}
		
		return render(request, 'main/outreach.html', context)
		
		

def OutreachDetailFunc(request, slug):

	if request.method == "post":
		pass #dont forget to add the add comment func
	
	else:

		outreach = get_object_or_404(Outreach, slug=slug)
		outreachs = Outreach.objects.order_by('-pub_date')
		members = Member.objects.order_by('-pub_date')
		events = Event.objects.order_by('-pub_date')
		context = {"outreach": outreach, "outreachs": outreachs, "members": members, "events": events}
		
		return render(request, 'main/outreach_detail.html', context)
	
	
def MemberDetailFunc(request, slug):

	if request.method == "post":
		pass #dont forget to add the add comment func
	
	else:

		member = get_object_or_404(Member, slug=slug)
		outreachs = Outreach.objects.order_by('-pub_date')
		members = Member.objects.order_by('-pub_date')
		events = Event.objects.order_by('-pub_date')
		context = {"member": member, "outreachs": outreachs, "members": members, "events": events}
		
		return render(request, 'main/member_detail.html', context)
	


###############################my shit ends it #############################

def causes(request):
	return render(request, 'causes.html')

	context = {}
	return render(request, {})





def portfolio(request):
	return render(request, 'portfolio.html')

	context = {}
	return render(request, {})


def single_causes(request):
	return render(request, 'single-causes.html')

	context = {}
	return render(request, {})

def news(request):
	return render(request, 'news.html')

	context = {}
	return render(request, {})
	
def postnewsOrblogMumu(request):
	return render(request, 'post.html')

	context = {}
	return render(request, {})
