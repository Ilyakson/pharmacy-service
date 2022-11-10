from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from pharmacy.models import Department, Medicine, Manufacturer


@login_required
def index(request):
    num_departments = Department.objects.count()
    num_medicines = Medicine.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_accounts": num_departments,
        "num_medicines": num_medicines,
        "num_manufacturers": num_manufacturers,
        "num_visits": num_visits + 1
    }

    return render(request, "pharmacy/index.html", context=context)
