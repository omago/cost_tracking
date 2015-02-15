# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CostName'
        db.create_table('cost_name', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cost_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cost_category.CostCategory'])),
            ('cost_subcategory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cost_subcategory.CostSubcategory'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal(u'cost_name', ['CostName'])


    def backwards(self, orm):
        # Deleting model 'CostName'
        db.delete_table('cost_name')


    models = {
        u'cost_category.costcategory': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'CostCategory', 'db_table': "'cost_category'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monthly_budget': ('django.db.models.fields.IntegerField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'cost_name.costname': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'CostName', 'db_table': "'cost_name'"},
            'cost_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cost_category.CostCategory']"}),
            'cost_subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cost_subcategory.CostSubcategory']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'cost_subcategory.costsubcategory': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'CostSubcategory', 'db_table': "'cost_subcategory'"},
            'cost_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cost_category.CostCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['cost_name']