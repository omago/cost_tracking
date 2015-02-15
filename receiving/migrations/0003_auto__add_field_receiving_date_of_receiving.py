# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Receiving.date_of_receiving'
        db.add_column('receiving', 'date_of_receiving',
                      self.gf('django.db.models.fields.DateField')(default=None),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Receiving.date_of_receiving'
        db.delete_column('receiving', 'date_of_receiving')


    models = {
        u'receiving.receiving': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Receiving', 'db_table': "'receiving'"},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'}),
            'date_of_receiving': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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