from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    alamat_lengkap = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'USER'


class Donatur(models.Model):
    email = models.ForeignKey(User, models.DO_NOTHING, db_column='email', primary_key=True)
    saldo = models.IntegerField()

    class Meta:
        db_table = 'donatur'


class Organisasi(models.Model):
    email_organisasi = models.CharField(primary_key=True, max_length=50)
    website = models.CharField(max_length=50)
    nama = models.CharField(max_length=50)
    provinsi = models.CharField(max_length=50)
    kabupaten_kota = models.CharField(max_length=50)
    kecamatan = models.CharField(max_length=50)
    kelurahan = models.CharField(max_length=50)
    kode_pos = models.CharField(max_length=50)
    status_verifikasi = models.CharField(max_length=50)

    class Meta:
        db_table = 'organisasi'


class Relawan(models.Model):
    email = models.ForeignKey(User, models.DO_NOTHING, db_column='email', primary_key=True)
    no_hp = models.CharField(max_length=20)
    tanggal_lahir = models.DateField()

    class Meta:
        db_table = 'relawan'


class Sponsor(models.Model):
    email = models.ForeignKey(User, models.DO_NOTHING, db_column='email', primary_key=True)
    logo_sponsor = models.CharField(max_length=100)

    class Meta:
        db_table = 'sponsor'
