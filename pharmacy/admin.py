from django.contrib import admin

from pharmacy.models import Organization, Branch, Medicament, MedicamentInBranch


class OrganizationAdmin(admin.ModelAdmin):
    pass


class BranchAdmin(admin.ModelAdmin):
    pass


class MedicamentAdmin(admin.ModelAdmin):
    pass


class MedicamentInBranchAdmin(admin.ModelAdmin):
    pass


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Medicament, MedicamentAdmin)
admin.site.register(MedicamentInBranch, MedicamentInBranchAdmin)
