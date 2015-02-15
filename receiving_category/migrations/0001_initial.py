# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ReceivingCategory'
        db.create_table('receiving_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'receiving_category', ['ReceivingCategory'])


    def backwards(self, orm):
        # Deleting model 'ReceivingCategory'
        db.delete_table('receiving_category')


    models = {
        u'receiving_category.receivingcategory': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'ReceivingCategory', 'db_table': "'receiving_category'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['receiving_category']