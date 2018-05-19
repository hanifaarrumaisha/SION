from django.db import models




class OrganisasiTerverifikasi(models.Model):
    email_organisasi = models.ForeignKey('login.Organisasi', models.DO_NOTHING, db_column='email_organisasi', primary_key=True)
    nomor_registrasi = models.CharField(max_length=50)
    status_aktif = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'organisasi_terverifikasi'


class PengurusOrganisasi(models.Model):
    email = models.ForeignKey('login.User', models.DO_NOTHING, db_column='email', primary_key=True)
    organisasi = models.ForeignKey('login.Organisasi', models.DO_NOTHING, db_column='organisasi')

    class Meta:
        managed = False
        db_table = 'pengurus_organisasi'
# Create your models here.
class TujuanOrganisasi(models.Model):
    organisasi = models.ForeignKey('login.Organisasi', models.DO_NOTHING, db_column='organisasi', primary_key=True)
    tujuan = models.TextField()

    class Meta:
        managed = False
        db_table = 'tujuan_organisasi'
        unique_together = (('organisasi', 'tujuan'),)
