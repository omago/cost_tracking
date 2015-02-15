# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CostSubcategory'
        db.create_table('cost_subcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('cost_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cost_category.CostCategory'])),
        ))
        db.send_create_signal(u'cost_subcategory', ['CostSubcategory'])


    def backwards(self, orm):
        # Deleting model 'CostSubcategory'
        db.delete_table('cost_subcategory')


    models = {
        u'cost_category.costcategory': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'CostCategory', 'db_table': "'cost_category'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'cost_subcategory.costsubcategory': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'CostSubcategory', 'db_table': "'cost_subcategory'"},
            'cost_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cost_category.CostCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['cost_subcategory']