from django.urls import path

from pharmacy.views import index, MedicineCreateView, MedicineListView, ManufacturerListView, MedicineDetailView, \
    DepartmentListView, DepartmentDetailView, ManufacturerCreateView, ManufacturerUpdateView, ManufacturerDeleteView, \
    MedicineUpdateView, MedicineDeleteView, DepartmentAddressUpdateView, DepartmentPhoneUpdateView, \
    DepartmentTimeWorkUpdateView, DepartmentNameUpdateView, DepartmentDeleteView, link_add, DepartmentCreateView, \
    DepartmentLicenseUpdateView

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/",
         ManufacturerListView.as_view(),
         name="manufacturer-list"),
    path(
        "manufacturers/create/",
        ManufacturerCreateView.as_view(),
        name="manufacturer-create"
    ),
    path(
        "manufacturers/<int:pk>/update/",
        ManufacturerUpdateView.as_view(),
        name="manufacturer-update"
    ),
    path(
        "manufacturers/<int:pk>/delete/",
        ManufacturerDeleteView.as_view(),
        name="manufacturer-delete"
    ),
    path(
        "medicine/",
        MedicineListView.as_view(),
        name="medicine-list"
    ),
    path(
        "medicine/<int:pk>/",
        MedicineDetailView.as_view(),
        name="medicine-detail"
    ),
    path(
        "medicine/create/",
        MedicineCreateView.as_view(),
        name="medicine-create"
    ),
    path(
        "medicine/<int:pk>/update/",
        MedicineUpdateView.as_view(),
        name="medicine-update"
    ),
    path(
        "medicine/<int:pk>/delete/",
        MedicineDeleteView.as_view(),
        name="medicine-delete"
    ),
    path("departments/", DepartmentListView.as_view(), name="department-list"),
    path(
        "departments/<int:pk>/",
        DepartmentDetailView.as_view(),
        name="department-detail"
    ),
    path(
        "department/create/", DepartmentCreateView.as_view(), name="department-create"),
    path(
        "department/<int:pk>/update/license/",
        DepartmentLicenseUpdateView.as_view(),
        name="department-update-license"
    ),
    path(
        "department/<int:pk>/update/address/",
        DepartmentAddressUpdateView.as_view(),
        name="department-update-address",
    ),
    path(
        "department/<int:pk>/update/phone/",
        DepartmentPhoneUpdateView.as_view(),
        name="department-update-phone",
    ),
    path(
        "department/<int:pk>/update/time_work/",
        DepartmentTimeWorkUpdateView.as_view(),
        name="department-update-time-work",
    ),
    path(
        "department/<int:pk>/update/name/",
        DepartmentNameUpdateView.as_view(),
        name="department-update-name",
    ),
    path(
        "department/<int:pk>/delete/",
        DepartmentDeleteView.as_view(),
        name="department-delete"
    ),
    path("medicine/<int:pk>/assign/", link_add, name="link-add")
]

app_name = "pharmacy"
