# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='ID_CATEGORIA', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categoria'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

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


class Producto(models.Model):
    id_producto = models.AutoField(db_column='ID_PRODUCTO', primary_key=True)  # Field name made lowercase.
    id_categoria = models.ForeignKey(Categoria, db_column='ID_CATEGORIA', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=256, blank=True, null=True)  # Field name made lowercase.
    marca = models.CharField(db_column='MARCA', max_length=256, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=256, blank=True, null=True)  # Field name made lowercase.
    cantidad = models.FloatField(db_column='CANTIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto'


class ProductoPrecio(models.Model):
    id_producto_precio = models.AutoField(db_column='ID_PRODUCTO_PRECIO', primary_key=True)  # Field name made lowercase.
    id_supermercado = models.ForeignKey('Supermercado', db_column='ID_SUPERMERCADO', blank=True, null=True)  # Field name made lowercase.
    id_producto = models.ForeignKey(Producto, db_column='ID_PRODUCTO', blank=True, null=True)  # Field name made lowercase.
    id_usuario = models.ForeignKey('Usuario', db_column='ID_USUARIO', blank=True, null=True)  # Field name made lowercase.
    precio = models.IntegerField(db_column='PRECIO', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.
    cant_valoracionpos = models.IntegerField(db_column='CANT_VALORACIONPOS', blank=True, null=True)  # Field name made lowercase.
    cant_valoracionneg = models.IntegerField(db_column='CANT_VALORACIONNEG', blank=True, null=True)  # Field name made lowercase.
    estado_confirmacion = models.IntegerField(db_column='ESTADO_CONFIRMACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto_precio'


class Reporte(models.Model):
    id_reporte = models.AutoField(db_column='ID_REPORTE', primary_key=True)  # Field name made lowercase.
    id_usuario = models.ForeignKey('Usuario', db_column='ID_USUARIO', blank=True, null=True)  # Field name made lowercase.
    id_producto_precio = models.ForeignKey(ProductoPrecio, db_column='ID_PRODUCTO_PRECIO', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.
    comentario = models.CharField(db_column='COMENTARIO', max_length=1024, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reporte'


class Supermercado(models.Model):
    id_supermercado = models.AutoField(db_column='ID_SUPERMERCADO', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=256, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='DIRECCION', max_length=256, blank=True, null=True)  # Field name made lowercase.
    latitud = models.DecimalField(db_column='LATITUD', max_digits=9, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    longitud = models.DecimalField(db_column='LONGITUD', max_digits=9, decimal_places=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'supermercado'


class Usuario(models.Model):
    id_usuario = models.AutoField(db_column='ID_USUARIO', primary_key=True)  # Field name made lowercase.
    nombre_usuario = models.CharField(db_column='NOMBRE_USUARIO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='CORREO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    contrasena = models.CharField(db_column='CONTRASENA', max_length=256, blank=True, null=True)  # Field name made lowercase.
    cant_reportes = models.IntegerField(db_column='CANT_REPORTES', blank=True, null=True)  # Field name made lowercase.
    estado_cuenta = models.IntegerField(db_column='ESTADO_CUENTA', blank=True, null=True)  # Field name made lowercase.
    porcentaje_confiabilidad = models.FloatField(db_column='PORCENTAJE_CONFIABILIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'


class Valoracion(models.Model):
    id_valoracion = models.AutoField(db_column='ID_VALORACION', primary_key=True)  # Field name made lowercase.
    id_usuario = models.ForeignKey(Usuario, db_column='ID_USUARIO', blank=True, null=True)  # Field name made lowercase.
    id_producto_precio = models.ForeignKey(ProductoPrecio, db_column='ID_PRODUCTO_PRECIO', blank=True, null=True)  # Field name made lowercase.
    valoracion = models.IntegerField(db_column='VALORACION', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'valoracion'