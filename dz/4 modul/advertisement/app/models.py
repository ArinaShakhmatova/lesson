from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()

class Adverisement(models.Model):
    user = models.ForeignKey(to = User, verbose_name="Пользователь", on_delete=models.CASCADE)
    title = models.CharField("Название", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text="Отметьте, если торг уместен")
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField("Изображение", upload_to="advertisement/")

    def created_date(self):
        if self.created_ad.date() == timezone.now().date():
            created_time = self.created_ad.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color:pink; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.created_ad.strftime("%d:%m:%Y в %H:%M:%S")

    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color:blue; font-weight: bold;">Сегодня в {}</span>', updated_time
            )
        return self.updated_at.strftime("%d:%m:%Y в %H:%M:%S")

    def image_form(self):
        from django.utils import html
        return html.format_html("<img scr='{}' alt='' style='width:50px; height:50px'>", self.image.url)




    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = "advertisements"
