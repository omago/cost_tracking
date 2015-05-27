# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ToDo'
        db.create_table('todo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.TextField')(max_length=11, null=True, blank=True)),
            ('date_to', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('assignee', self.gf('django.db.models.fields.related.ForeignKey')(related_name='todo_assignee', to=orm['auth.User'])),
            ('finished', self.gf('django.db.models.fields.BooleanField')()),
            ('finished_datetime', self.gf('django.db.models.fields.BooleanField')()),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='todo_created_by', to=orm['auth.User'])),
            ('creation_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('deleted', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('deleted_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('deleted_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='todo_deleted_by', null=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'to_do', ['ToDo'])


    def backwards(self, orm):
        # Deleting model 'ToDo'
        db.delete_table('todo')


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
        u'to_do.todo': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'ToDo', 'db_table': "'todo'"},
            'assignee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'todo_assignee'", 'to': u"orm['auth.User']"}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'todo_created_by'", 'to': u"orm['auth.User']"}),
            'creation_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'date_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'deleted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'todo_deleted_by'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'deleted_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'finished': ('django.db.models.fields.BooleanField', [], {}),
            'finished_datetime': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.TextField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['to_do']