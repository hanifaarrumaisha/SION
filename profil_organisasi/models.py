from django.db import models




class OrganisasiTerverifikasi(models.Model):
    email_organisasi = models.ForeignKey('login.Organisasi', models.DO_NOTHING, db_column='email_organisasi', primary_key=True)
    nomor_registrasi = models.CharField(max_length=50)
    status_aktif = models.CharField(max_length=50)

    class Meta:
       # managed = False
        db_table = 'organisasi_terverifikasi'


class PengurusOrganisasi(models.Model):
    email = models.ForeignKey('login.User', models.DO_NOTHING, db_column='email', primary_key=True)
    organisasi = models.ForeignKey('login.Organisasi', models.DO_NOTHING, db_column='organisasi')

    class Meta:
       # managed = False
        db_table = 'pengurus_organisasi'
# Create your models here.
class TujuanOrganisasi(models.Model):
    organisasi = models.ForeignKey('login.Organisasi', models.DO_NOTHING, db_column='organisasi', primary_key=True)
    tujuan = models.TextField()

    class Meta:
      #  managed = False
        db_table = 'tujuan_organisasi'
        unique_together = (('organisasi', 'tujuan'),)

#class Donatur(models.Model):
  #  email = models.ForeignKey('login.User', models.DO_NOTHING, db_column='email', primary_key=True)
   # saldo = models.IntegerField()

    #class Meta:
      #  managed = False
     #   db_table = 'donatur'

class DonaturOrganisasi(models.Model):
    donatur = models.ForeignKey('login.Donatur', models.DO_NOTHING, db_column='donatur', primary_key=True)
    organisasi = models.ForeignKey(OrganisasiTerverifikasi, models.DO_NOTHING, db_column='organisasi')
    tanggal = models.DateField()
    nominal = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'donatur_organisasi'
        unique_together = (('donatur', 'organisasi'),)

#class Sponsor(models.Model):
 #   email = models.ForeignKey('login.User', models.DO_NOTHING, db_column='email', primary_key=True)
  #  logo_sponsor = models.CharField(max_length=100)
#
 #   class Meta:
  #   #   managed = False
   #     db_table = 'sponsor'


class SponsorOrganisasi(models.Model):
    sponsor = models.ForeignKey('login.Sponsor', models.DO_NOTHING, db_column='sponsor', primary_key=True)
    organisasi = models.ForeignKey(OrganisasiTerverifikasi, models.DO_NOTHING, db_column='organisasi')
    tanggal = models.DateField()
    nominal = models.IntegerField()

    class Meta:
     #   managed = False
        db_table = 'sponsor_organisasi'
        unique_together = (('sponsor', 'organisasi'),)

