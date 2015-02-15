# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cost'
        db.create_table('cost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cost_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cost_category.CostCategory'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=2)),
            ('date_of_cost', self.gf('django.db.models.fields.DateField')()),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'cost', ['Cost'])


    def backwards(self, orm):
        # Deleting model 'Cost'
        db.delete_table('cost')


    models = {
        u'cost.cost': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Cost', 'db_table': "'cost'"},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'}),
            'cost_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cost_category.CostCategory']"}),
            'date_of_cost': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'cost_category.costcategory': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'CostCategory', 'db_table': "'cost_category'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['cost']