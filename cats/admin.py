from django.contrib import admin


class CatAdmin(admin.ModelAdmin):
    list_display = ("id" "breef", "color")
    fields = "__all__" + "rating"

    def rating(self, obj):
        values = obj.catrating.values_list("value", flat=True)
        return float(sum(values) / len(values))


class BreefAdmin(admin.ModelAdmin):
    list_display = "id" "name"
