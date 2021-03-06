# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Cost.cost_name'
        db.delete_column('cost', 'cost_name_id')

        # Deleting field 'Cost.receipt'
        db.delete_column('cost', 'receipt_id')

        # Deleting field 'Cost.attachment'
        db.delete_column('cost', 'attachment')

        # Deleting field 'Cost.cost_subcategory'
        db.delete_column('cost', 'cost_subcategory_id')

        # Deleting field 'Cost.quantity'
        db.delete_column('cost', 'quantity')


    def backwards(self, orm):
        # Adding field 'Cost.cost_name'
        db.add_column('cost', 'cost_name',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cost_name.CostName'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cost.receipt'
        db.add_column('cost', 'receipt',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['receipt.Receipt'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cost.attachment'
        db.add_column('cost', 'attachment',
                      self.gf('django.db.models.fields.files.FileField')(default=None, max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Cost.cost_subcategory'
        db.add_column('cost', 'cost_subcategory',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cost_subcategory.CostSubcategory'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cost.quantity'
        db.add_column('cost', 'quantity',
                      self.gf('django.db.models.fields.DecimalField')(default=None, max_digits=11, decimal_places=2),
                      keep_default=False)


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'cost.cost': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Cost', 'db_table': "'cost'"},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'}),
            'cost_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cost_category.CostCategory']"}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cost_created_by'", 'to': u"orm['auth.User']"}),
            'creation_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'date_of_cost': ('django.db.models.fields.DateField', [], {}),
            'deleted': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'deleted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'cost_deleted_by'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'deleted_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paid_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cost_paid_by'", 'to': u"orm['auth.User']"})
        },
        u'cost_category.costcategory': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'CostCategory', 'db_table': "'cost_category'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monthly_budget': ('django.db.models.fields.IntegerField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['cost']