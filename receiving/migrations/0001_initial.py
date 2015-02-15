# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Receiving'
        db.create_table('receiving', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('receiving_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['receiving_category.ReceivingCategory'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=2)),
        ))
        db.send_create_signal(u'receiving', ['Receiving'])


    def backwards(self, orm):
        # Deleting model 'Receiving'
        db.delete_table('receiving')


    models = {
        u'receiving.receiving': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Receiving', 'db_table': "'receiving'"},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'receiving_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['receiving_category.ReceivingCategory']"})
        },
        u'receiving_category.receivingcategory': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'ReceivingCategory', 'db_table': "'receiving_category'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['receiving']