from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


from pharmacy.forms import (
    DepartmentCreationForm,
    DepartmentLicenseUpdateForm,
    DepartmentAddressUpdateForm,
    DepartmentPhoneUpdateForm,
    DepartmentTimeWorkUpdateForm,
    DepartmentNameUpdateForm,
    MedicineForm,
    MedicineSearchForm,
    ManufacturerSearchForm,
    DepartmentSearchForm
)
from pharmacy.models import Department, Medicine, Manufacturer


@login_required
def index(request):
    num_departments = Department.objects.count()
    num_medicines = Medicine.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_departments": num_departments,
        "num_medicines": num_medicines,
        "num_manufacturers": num_manufacturers,
        "num_visits": num_visits + 1
    }

    return render(request, "pharmacy/index.html", context=context)


class ManufacturerListView(LoginRequiredMixin, generic.ListView):
    model = Manufacturer
    template_name = "pharmacy/manufacturer_list.html"
    queryset = Manufacturer.objects.order_by("name")
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ManufacturerListView, self).get_context_data(**kwargs)

        context["search_form"] = ManufacturerSearchForm()

        return context

    def get_queryset(self):
        name = self.request.GET.get("name", None)

        if name:
            return self.queryset.filter(name__icontains=name)
        return self.queryset


class ManufacturerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("pharmacy:manufacturer-list")


class ManufacturerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("pharmacy:manufacturer-list")


class ManufacturerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Manufacturer
    success_url = reverse_lazy("pharmacy:manufacturer-list")


class MedicineListView(LoginRequiredMixin, generic.ListView):
    model = Medicine
    paginate_by = 5
    template_name = "pharmacy/medicine_list.html"
    queryset = Medicine.objects.select_related("manufacturer")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MedicineListView, self).get_context_data(**kwargs)

        context["search_form"] = MedicineSearchForm()

        return context

    def get_queryset(self):
        name = self.request.GET.get("name", None)

        if name:
            return self.queryset.filter(model__icontains=name)
        return self.queryset


class MedicineDetailView(LoginRequiredMixin, generic.DetailView):
    model = Medicine
    template_name = "pharmacy/medicine_detail.html"


class MedicineCreateView(LoginRequiredMixin, generic.CreateView):
    model = Medicine
    form_class = MedicineForm
    success_url = reverse_lazy("pharmacy:medicine-list")


class MedicineUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Medicine
    form_class = MedicineForm
    success_url = reverse_lazy("pharmacy:medicine-list")


class MedicineDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Medicine
    success_url = reverse_lazy("pharmacy:medicine-list")


class DepartmentListView(LoginRequiredMixin, generic.ListView):
    model = Department
    template_name = "pharmacy/department_list.html"
    paginate_by = 5
    queryset = Department.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DepartmentListView, self).get_context_data(**kwargs)

        context["search_form"] = DepartmentSearchForm()

        return context

    def get_queryset(self):
        name_pharmacy = self.request.GET.get("name_pharmacy", None)

        if name_pharmacy:
            return self.queryset.filter(name_pharmacy__icontains=name_pharmacy)
        return self.queryset


class DepartmentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Department
    template_name = "pharmacy/department_detail.html"
    queryset = Department.objects.prefetch_related("medicines__manufacturer")


class DepartmentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Department
    form_class = DepartmentCreationForm


class DepartmentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Department
    success_url = reverse_lazy("pharmacy:department-list")


class DepartmentLicenseUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Department
    form_class = DepartmentLicenseUpdateForm
    success_url = reverse_lazy("pharmacy:department-list")


class DepartmentAddressUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Department
    form_class = DepartmentAddressUpdateForm
    success_url = reverse_lazy("pharmacy:department-list")


class DepartmentPhoneUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Department
    form_class = DepartmentPhoneUpdateForm
    success_url = reverse_lazy("pharmacy:department-list")


class DepartmentTimeWorkUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Department
    form_class = DepartmentTimeWorkUpdateForm
    success_url = reverse_lazy("pharmacy:department-list")


class DepartmentNameUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Department
    form_class = DepartmentNameUpdateForm
    success_url = reverse_lazy("pharmacy:department-list")


@login_required
def link_add(request, pk):
    medicine = Medicine.objects.get(id=pk)
    user = get_user_model().objects.get(id=request.user.id)
    if user in medicine.departments.all():
        medicine.departments.remove(user)
    else:
        medicine.departments.add(user)
    return HttpResponseRedirect(
        reverse_lazy(
            "pharmacy:medicine-detail",
            args=[pk]
        )
    )
