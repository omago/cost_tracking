# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CostCategory.monthly_budget'
        db.add_column('cost_category', 'monthly_budget',
                      self.gf('django.db.models.fields.IntegerField')(max_length=11, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CostCategory.monthly_budget'
        db.delete_column('cost_category', 'monthly_budget')


    models = {
        u'cost_category.costcategory': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'CostCategory', 'db_table': "'cost_category'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monthly_budget': ('django.db.models.fields.IntegerField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['cost_category']