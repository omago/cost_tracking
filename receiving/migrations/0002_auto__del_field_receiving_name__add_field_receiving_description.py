# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Receiving.name'
        db.delete_column('receiving', 'name')

        # Adding field 'Receiving.description'
        db.add_column('receiving', 'description',
                      self.gf('django.db.models.fields.TextField')(default=None),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Receiving.name'
        db.add_column('receiving', 'name',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=128),
                      keep_default=False)

        # Deleting field 'Receiving.description'
        db.delete_column('receiving', 'description')


    models = {
        u'receiving.receiving': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Receiving', 'db_table': "'receiving'"},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'receiving_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['receiving_category.ReceivingCategory']"})
        },
        u'receiving_category.receivingcategory': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'ReceivingCategory', 'db_table': "'receiving_category'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['receiving']