from django.shortcuts import render, redirect, get_object_or_404
from .forms import MemberRegistrationForm
from django.utils.timezone import now
from .models import Event
from .forms import BlogPostForm
from .models import BlogPost
from django.contrib.auth.decorators import login_required



# Member registration view
def register(request):
    if request.method == 'POST':
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')  # Redirect to the success page
    else:
        form = MemberRegistrationForm()

    return render(request, 'members/register.html', {'form': form})  # Template path under 'members/'


# Registration success view
def registration_success(request):
    return render(request, 'members/success.html')  # Render the success page


# About Us page view
def about_us(request):
    return render(request, 'about_us.html')


# Gallery page view
def gallery(request):
    return render(request, 'gallery.html')


# Upcoming events page view
def upcoming_events(request):
    return render(request, 'upcoming_events.html')


# Home page view
def home(request):
    return render(request, 'home.html')


# Event list view showing upcoming events
def event_list(request):
    upcoming_events = Event.objects.filter(date__gte=now()).order_by('date')
    context = {'upcoming_events': upcoming_events}
    return render(request, 'events/event_list.html', context)  # Template path under 'events/'


# Event detail view with RSVP form
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    form = RSVPForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        rsvp = form.save(commit=False)
        rsvp.member = request.user.member  # Assuming the user is authenticated and linked to a Member
        rsvp.event = event  # Assign the event to the RSVP instance
        rsvp.save()  # Save the RSVP
        return redirect('event_detail', event_id=event.id)  # Redirect to the event detail page

    context = {
        'event': event,
        'form': form,
    }
    return render(request, 'events/event_detail.html', context)  # Template path under 'events/'


# RSVP view for events
def event_rsvp(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            rsvp = form.save(commit=False)
            rsvp.event = event  # Assign the event to the RSVP instance
            rsvp.member = request.user.member  # Assuming the user is authenticated and linked to a Member
            rsvp.save()
            return redirect('event_detail', event_id=event_id)
    else:
        form = RSVPForm(initial={'event': event})

    return render(request, 'events/event_rsvp.html', {'form': form, 'event': event})

# Success page view
def success(request):
    return render(request, 'members/success.html')  # Ensure the path is correct

def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)  # Do not save to DB yet
            blog_post.author = request.user  # Set the author
            blog_post.save()  # Now save to DB
            return redirect('blog')  # Redirect to the blog page
    else:
        form = BlogPostForm()
    return render(request, 'members/create_blog_post.html', {'form': form})

def blog_view(request):
    # Logic for the blog page, like fetching blog posts
    return render(request, 'members/blog.html')  # Make sure this template exists