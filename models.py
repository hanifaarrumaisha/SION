# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    alamat_lengkap = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'USER'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Berita(models.Model):
    kode_unik = models.CharField(primary_key=True, max_length=50)
    kegiatan = models.ForeignKey('Kegiatan', models.DO_NOTHING, db_column='kegiatan')
    judul = models.CharField(max_length=100)
    deskripsi = models.TextField()
    tgl_update = models.DateField()
    tgl_kegiatan = models.DateField()

    class Meta:
        managed = False
        db_table = 'berita'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Donatur(models.Model):
    email = models.ForeignKey(User, models.DO_NOTHING, db_column='email', primary_key=True)
    saldo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'donatur'


class DonaturKegiatan(models.Model):
    donatur = models.ForeignKey(Donatur, models.DO_NOTHING, db_column='donatur', primary_key=True)
    kegiatan = models.ForeignKey('Kegiatan', models.DO_NOTHING, db_column='kegiatan')
    tanggal = models.DateField()
    nominal = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'donatur_kegiatan'
        unique_together = (('donatur', 'kegiatan'),)


class DonaturOrganisasi(models.Model):
    donatur = models.ForeignKey(Donatur, models.DO_NOTHING, db_column='donatur', primary_key=True)
    organisasi = models.ForeignKey('OrganisasiTerverifikasi', models.DO_NOTHING, db_column='organisasi')
    tanggal = models.DateField()
    nominal = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'donatur_organisasi'
        unique_together = (('donatur', 'organisasi'),)


class Kategori(models.Model):
    kode = models.CharField(primary_key=True, max_length=20)
    nama = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'kategori'


class KategoriKegiatan(models.Model):
    kode_kegiatan = models.ForeignKey('Kegiatan', models.DO_NOTHING, db_column='kode_kegiatan', primary_key=True)
    kode_kategori = models.ForeignKey(Kategori, models.DO_NOTHING, db_column='kode_kategori')

    class Meta:
        managed = False
        db_table = 'kategori_kegiatan'
        unique_together = (('kode_kegiatan', 'kode_kategori'),)


class KeahlianRelawan(models.Model):
    email = models.ForeignKey('Relawan', models.DO_NOTHING, db_column='email', primary_key=True)
    keahlian = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'keahlian_relawan'
        unique_together = (('email', 'keahlian'),)


class Kegiatan(models.Model):
    kode_unik = models.CharField(primary_key=True, max_length=20)
    organisasi_perancang = models.ForeignKey('OrganisasiTerverifikasi', models.DO_NOTHING, db_column='organisasi_perancang')
    judul = models.CharField(max_length=50)
    dana_dibutuhkan = models.IntegerField()
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField()
    deskripsi = models.TextField()

    class Meta:
        managed = False
        db_table = 'kegiatan'


class LaporanKeuangan(models.Model):
    organisasi = models.ForeignKey('OrganisasiTerverifikasi', models.DO_NOTHING, db_column='organisasi', primary_key=True)
    tgl_dibuat = models.DateField()
    rincian_pemasukan = models.TextField()
    total_pemasukan = models.IntegerField()
    total_pengeluaran = models.IntegerField()
    is_disetujui = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'laporan_keuangan'
        unique_together = (('organisasi', 'tgl_dibuat'),)


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
        managed = False
        db_table = 'organisasi'


class OrganisasiTerverifikasi(models.Model):
    email_organisasi = models.ForeignKey(Organisasi, models.DO_NOTHING, db_column='email_organisasi', primary_key=True)
    nomor_registrasi = models.CharField(max_length=50)
    status_aktif = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'organisasi_terverifikasi'


class PengurusOrganisasi(models.Model):
    email = models.ForeignKey(User, models.DO_NOTHING, db_column='email', primary_key=True)
    organisasi = models.ForeignKey(Organisasi, models.DO_NOTHING, db_column='organisasi')

    class Meta:
        managed = False
        db_table = 'pengurus_organisasi'


class PenilaianPerforma(models.Model):
    email_relawan = models.ForeignKey('Relawan', models.DO_NOTHING, db_column='email_relawan', primary_key=True)
    organisasi = models.ForeignKey(OrganisasiTerverifikasi, models.DO_NOTHING, db_column='organisasi')
    id = models.IntegerField()
    deskripsi = models.TextField()
    tgl_penilaian = models.DateField()
    nilai_skala = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'penilaian_performa'
        unique_together = (('email_relawan', 'organisasi', 'id'),)


class Relawan(models.Model):
    email = models.ForeignKey(User, models.DO_NOTHING, db_column='email', primary_key=True)
    no_hp = models.CharField(max_length=20)
    tanggal_lahir = models.DateField()

    class Meta:
        managed = False
        db_table = 'relawan'


class RelawanOrganisasi(models.Model):
    email_relawan = models.ForeignKey(Relawan, models.DO_NOTHING, db_column='email_relawan', primary_key=True)
    organisasi = models.ForeignKey(Organisasi, models.DO_NOTHING, db_column='organisasi')

    class Meta:
        managed = False
        db_table = 'relawan_organisasi'
        unique_together = (('email_relawan', 'organisasi'),)


class Reward(models.Model):
    kode_kegiatan = models.ForeignKey(Kegiatan, models.DO_NOTHING, db_column='kode_kegiatan', primary_key=True)
    barang_reward = models.CharField(max_length=50)
    harga_min = models.IntegerField()
    harga_max = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'reward'
        unique_together = (('kode_kegiatan', 'barang_reward'),)


class Sponsor(models.Model):
    email = models.ForeignKey(User, models.DO_NOTHING, db_column='email', primary_key=True)
    logo_sponsor = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'sponsor'


class SponsorOrganisasi(models.Model):
    sponsor = models.ForeignKey(Sponsor, models.DO_NOTHING, db_column='sponsor', primary_key=True)
    organisasi = models.ForeignKey(OrganisasiTerverifikasi, models.DO_NOTHING, db_column='organisasi')
    tanggal = models.DateField()
    nominal = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sponsor_organisasi'
        unique_together = (('sponsor', 'organisasi'),)


class TujuanOrganisasi(models.Model):
    organisasi = models.ForeignKey(Organisasi, models.DO_NOTHING, db_column='organisasi', primary_key=True)
    tujuan = models.TextField()

    class Meta:
        managed = False
        db_table = 'tujuan_organisasi'
        unique_together = (('organisasi', 'tujuan'),)
