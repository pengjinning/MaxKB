# Generated by Django 4.2.15 on 2024-09-05 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0006_alter_model_status'),
        ('application', '0011_application_model_params_setting'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='stt_model',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stt_model_id', to='setting.model'),
        ),
        migrations.AddField(
            model_name='application',
            name='stt_model_enable',
            field=models.BooleanField(default=False, verbose_name='语音识别模型是否启用'),
        ),
        migrations.AddField(
            model_name='application',
            name='tts_model',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tts_model_id', to='setting.model'),
        ),
        migrations.AddField(
            model_name='application',
            name='tts_model_enable',
            field=models.BooleanField(default=False, verbose_name='语音合成模型是否启用'),
        ),
    ]
