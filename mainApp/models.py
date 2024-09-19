from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Xaridor(models.Model):
    ism = models.CharField(max_length=50)
    familya = models.CharField(max_length=50)
    manzil = models.CharField(max_length=100)
    tel_1 = models.CharField(max_length=13)
    tel_2 = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return f"{self.ism} {self.familya}"


class Sotuv(models.Model):
    meva_turi = models.CharField(max_length=20,
                                 choices=(("SUPER", "SUPER"), ("LOLA 1", "LOLA 1"), ("LOALA 2", "LOLA 2"),
                                          ("pishgan", "pishgan")))
    bog = models.CharField(max_length=20, choices=(
        ("Katta bog'", "Katta bog'"), ("Yangi bog'", "Yangi bog'"), ("Burchak", "Burchak"), ("Ishxona", "Ishxona")))
    quti_turi = models.CharField(max_length=20,
                                 choices=(("karzinka", "karzinka"), ("yashik", "yashik"), ("karobka", "karobka")))
    quti_soni = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    quti_ogirligi = models.FloatField(validators=[MinValueValidator(0)], default=0)
    tara = models.FloatField(validators=[MinValueValidator(0.5)])
    otish = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)
    xaridor = models.ForeignKey(Xaridor, on_delete=models.CASCADE)
    sana = models.DateField()
    narxi = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    foyda = models.BigIntegerField(validators=[MinValueValidator(0)], default=0)

    @property
    def formatted_foyda(self):
        return "{:,} so'm ".format(self.foyda)

    def save(self, *args, **kwargs):

        self.foyda = self.narxi * ((self.quti_soni * (self.quti_ogirligi - (self.tara + self.otish))))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.meva_turi} {self.quti_soni} ta"


class Xarajatlar(models.Model):
    umumiy_xarajat = models.FloatField()
    sabab = models.CharField(max_length=255, blank=True, null=True)
    sana = models.DateField()

    def __str__(self):
        return f"{self.umumiy_xarajat} so'm"
