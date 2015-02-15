# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Receiving.received_by'
        db.add_column('receiving', 'received_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='receiving_received_by', to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Receiving.created_by'
        db.add_column('receiving', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='receiving_created_by', to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Receiving.creation_datetime'
        db.add_column('receiving', 'creation_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=None),
                      keep_default=False)

        # Adding field 'Receiving.deleted'
        db.add_column('receiving', 'deleted',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Receiving.deleted_datetime'
        db.add_column('receiving', 'deleted_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Receiving.deleted_by'
        db.add_column('receiving', 'deleted_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='receiving_deleted_by', null=True, to=orm['auth.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Receiving.received_by'
        db.delete_column('receiving', 'received_by_id')

        # Deleting field 'Receiving.created_by'
        db.delete_column('receiving', 'created_by_id')

        # Deleting field 'Receiving.creation_datetime'
        db.delete_column('receiving', 'creation_datetime')

        # Deleting field 'Receiving.deleted'
        db.delete_column('receiving', 'deleted')

        # Deleting field 'Receiving.deleted_datetime'
        db.delete_column('receiving', 'deleted_datetime')

        # Deleting field 'Receiving.deleted_by'
        db.delete_column('receiving', 'deleted_by_id')


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
        u'receiving.receiving': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Receiving', 'db_table': "'receiving'"},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'receiving_created_by'", 'to': u"orm['auth.User']"}),
            'creation_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'date_of_receiving': ('django.db.models.fields.DateField', [], {}),
            'deleted': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'deleted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'receiving_deleted_by'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'deleted_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'received_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'receiving_received_by'", 'to': u"orm['auth.User']"}),
            'receiving_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['receiving_category.ReceivingCategory']"})
        },
        u'receiving_category.receivingcategory': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'ReceivingCategory', 'db_table': "'receiving_category'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['receiving']