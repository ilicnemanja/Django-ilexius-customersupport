from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.http import HttpRequest
from .models.user import User
from .models.customer_support import CustomerSupport
from .models.comments import Comments



def customer_support(request: HttpRequest):
    
    if request.method == "GET":
        success = request.session.get('success', None)
        error = request.session.get('error', None)

        if success is not None:
            del request.session['success']

        if error is not None:
            del request.session['error']

        context = { "success" : success, "error": error }
        return render(request, "support/customer_support.html", context=context)
    if request.method == "POST":
        new_customer = CustomerSupport()
        new_customer.name = request.POST["name"]
        new_customer.phone = request.POST["phone"]
        new_customer.company = request.POST["company"]
        new_customer.customer_email = request.POST["email"]
        new_customer.subject = request.POST["subject"]
        new_customer.issue_description = request.POST["description"]
        new_customer.date_time = request.POST["datetime"]
        new_customer.save()
        request.session['success'] = "The message was sent successfully."
        return redirect("support:customer_support")

def check_support(request: HttpRequest):
    success = request.session.get('success', None)
    error = request.session.get('error', None)

    if success is not None:
        del request.session['success']

    if error is not None:
        del request.session['error']

    context = { "success" : success, "error": error }

    user_session = request.session.get("user")
    if user_session != None:
        return render(request, "user/check_support.html", context=context)
    else:
        return redirect("support:customer_support")

def view_list(request: HttpRequest):
    user_session = request.session.get("user")
    if user_session != None:
        success = request.session.get('success', None)
        error = request.session.get('error', None)
        if success is not None:
            del request.session['success']

        if error is not None:
            del request.session['error']

        customer_supports = CustomerSupport.objects.filter(is_archived=False).order_by('-sent')

        context = { "customer_supports": customer_supports, "success" : success, "error": error }
        return render(request, "support/view_list.html", context)
    else:
        return redirect("support:customer_support")

def view_detail(request: HttpRequest, customer_id: int):
    user_session = request.session.get("user")
    if user_session != None:
        customersupports = CustomerSupport.objects.get(id=customer_id)
        comments = Comments.objects.order_by("-added")
        context = { "customersupports": customersupports, "comments":comments }
        return render(request, "support/view_detail.html", context)
    else:
        return redirect("support:customer_support")


def add_to_archive(request: HttpRequest, customer_id: int):
    user_session = request.session.get("user")
    if user_session != None:
        customersupports = CustomerSupport.objects.get(id=customer_id)
        customersupports.is_archived = True
        customersupports.save()
        context = { "customersupports":customersupports }
        request.session["success"] = "You have successfully add to archive."
        return redirect("support:check_support")
    else:
        return redirect("support:customer_support")

def view_archived_list(request: HttpRequest):
    user_session = request.session.get("user")
    if user_session != None:
        customer_supports = CustomerSupport.objects.filter(is_archived=True).order_by('-sent')

        context = { "customer_supports": customer_supports }
        return render(request, "support/view_archived_list.html", context)
    else:
        return redirect("support:customer_support")

def restore(request: HttpRequest, customer_id: int):
    user_session = request.session.get("user")
    if user_session != None:
        customersupports = CustomerSupport.objects.get(id=customer_id)
        customersupports.is_archived = False
        customersupports.save()
        context = { "customersupports":customersupports }
        request.session["success"] = "You have successfully restored."
        return redirect("support:check_support")
    else:
        return redirect("support:customer_support")

def delete(request: HttpRequest, customer_id: int):
    user_session = request.session.get("user")
    if user_session != None:
        selected_issue = CustomerSupport.objects.get(id=customer_id)
        selected_issue.delete()
        request.session["success"] = "You have successfully deleted."
        return redirect("support:check_support")
    else:
        return redirect("support:customer_support")

def add_comment(request: HttpRequest, customer_id: int):
    user_session = request.session.get("user")
    if user_session != None:
        if request.method == "GET":
            return redirect("support:view_list")
        if request.method == "POST":
            new_comment = Comments()
            new_comment.user = User.objects.get(first_name=request.session["user"]["first_name"])
            new_comment.customer_support = CustomerSupport.objects.get(id=customer_id)
            new_comment.text = request.POST["comment"]
            new_comment.save()
            
            request.session['success'] = "Comment has been send."
            return redirect("support:view_list")
    else:
        return redirect("support:customer_support")



def register(request: HttpRequest):
    if request.method == "GET":
        user_session = request.session.get("user")
        if user_session != None:
            return redirect("support:check_support")
        else:
            success = request.session.get('success', None)
            error = request.session.get('error', None)

            if success is not None:
                del request.session['success']

            if error is not None:
                del request.session['error']

            context = { "success" : success, "error": error }
            return render(request,"user/registration.html", context=context) 
    if request.method == "POST":
        new_user = User()
        new_user.first_name = request.POST['first_name']
        new_user.last_name = request.POST['last_name']
        new_user.email = request.POST['r_email']
        if request.POST["password"] == request.POST["c_password"]:
            new_user.create_hashed_password(request.POST['password'])
        else:
            request.session['error'] = "The passwords did not match!"
            return redirect("support:register")
        
        try:
            new_user.save()
            request.session['success'] = "User has been saved to database."
            return redirect("support:check_support")
        except IntegrityError as iex:
            request.session['error'] = f"User with email: {request.POST['r_email']}  already exists."
            return redirect("support:register")
        except Exception as ex:
            request.session['error'] = f"{ex}"
            return redirect("support:register")

def login(request: HttpRequest):
    if request.method == "GET":
        error = request.session.get("error", None)
        if error is not None:
            del request.session['error']
        context={ "error": error }
        return render(request, "user/login.html", context)
    if request.method == "POST":
        try:
            login_user = User.objects.get(email=request.POST['email'])
            if login_user.verify_password(request.POST['password']):
                request.session['user'] = login_user.to_dict()
                request.session['success'] = "Successfully logged in."
                return redirect("support:check_support")
        except:
            pass
        request.session['error'] = "Username and/or password invalid."
        return redirect("support:login")


def logout(request:HttpRequest):
    user = request.session.get('user', None)
    if user is not None:
        request.session['success'] = "You have successfully logged out."
        del request.session['user']
    return redirect('support:customer_support')