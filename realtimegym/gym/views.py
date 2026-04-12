from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import ContactMessage, MembershipEnquiry, Testimonial, BlogPost


def home(request):
    testimonials = Testimonial.objects.filter(is_active=True)[:6]
    posts = BlogPost.objects.filter(published=True)[:3]
    return render(request, 'gym/index.html', {
        'testimonials': testimonials,
        'posts': posts,
    })


def blog(request):
    posts = BlogPost.objects.filter(published=True)
    return render(request, 'gym/blog.html', {'posts': posts})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    related = BlogPost.objects.filter(published=True).exclude(id=post.id)[:3]
    return render(request, 'gym/blog_detail.html', {'post': post, 'related': related})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        message = request.POST.get('message', '').strip()
        if name and email and message:
            ContactMessage.objects.create(
                name=name, email=email, phone=phone, message=message
            )
            messages.success(request, 'Message sent! We will get back to you shortly.')
        else:
            messages.error(request, 'Please fill in all required fields.')
        return redirect('home')
    return redirect('home')


def membership(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        plan = request.POST.get('plan', '').strip()
        if name and email and phone and plan:
            MembershipEnquiry.objects.create(
                name=name, email=email, phone=phone, plan=plan
            )
            messages.success(request, f'Enquiry received for {plan.title()} plan! We will call you shortly.')
        else:
            messages.error(request, 'Please fill in all required fields.')
        return redirect('home')
    return redirect('home')
