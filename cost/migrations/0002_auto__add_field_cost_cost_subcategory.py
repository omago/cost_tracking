# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Cost.cost_subcategory'
        db.add_column('cost', 'cost_subcategory',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['cost_subcategory.CostSubcategory']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Cost.cost_subcategory'
        db.delete_column('cost', 'cost_subcategory_id')


    models = {
        u'cost.cost': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Cost', 'db_table': "'cost'"},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'}),
            'cost_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cost_category.CostCategory']"}),
            'cost_subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cost_subcategory.CostSubcategory']"}),
            'date_of_cost': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
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

    complete_apps = ['cost']