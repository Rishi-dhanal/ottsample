from django.contrib import admin


from .models import Register, User, Movie, Membership, PaymentOption, AdultAccount, ChildAccount

# Register your models here.
admin.site.register(Register),
admin.site.register(User),
admin.site.register(Movie),
admin.site.register(Membership),
admin.site.register(PaymentOption),
admin.site.register(AdultAccount),
admin.site.register(ChildAccount),



