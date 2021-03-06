# Generated by Django 2.2 on 2020-11-27 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('club', models.CharField(max_length=35, primary_key=True, serialize=False)),
                ('division', models.CharField(max_length=1)),
                ('cantJugadores', models.IntegerField(null=True)),
                ('amonestados', models.IntegerField(null=True)),
                ('expulsados', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('idPartido', models.CharField(default='', max_length=8, primary_key=True, serialize=False)),
                ('numLine', models.IntegerField(null=True)),
                ('numScrum', models.IntegerField(null=True)),
                ('numPenales', models.IntegerField(null=True)),
                ('tri', models.IntegerField(null=True)),
                ('numConversiones', models.IntegerField(null=True)),
                ('numDrop', models.IntegerField(null=True)),
                ('numTacles', models.IntegerField(null=True)),
                ('numMaul', models.IntegerField(null=True)),
                ('numRuck', models.IntegerField(null=True)),
                ('cantPases', models.IntegerField(null=True)),
                ('numLinePerdidos', models.IntegerField(null=True)),
                ('numScrumPerdidos', models.IntegerField(null=True)),
                ('numPenalesEnContra', models.IntegerField(null=True)),
                ('numPelotasCaidas', models.IntegerField(null=True)),
                ('numConversionesErrados', models.IntegerField(null=True)),
                ('numTaclesErrados', models.IntegerField(null=True)),
                ('numPaseFoword', models.IntegerField(null=True)),
                ('numDropErrados', models.IntegerField(null=True)),
                ('numMaulErrados', models.IntegerField(null=True)),
                ('numRuckErrados', models.IntegerField(null=True)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=25)),
                ('apellido', models.CharField(default='', max_length=25)),
                ('dni', models.IntegerField(null=True)),
                ('tel', models.IntegerField(null=True)),
                ('posicion', models.CharField(default='', max_length=50)),
                ('asistenciaComp', models.BooleanField(default=False)),
                ('gym', models.BooleanField(default=False)),
                ('amonestado', models.BooleanField(default=False)),
                ('expulsado', models.BooleanField(default=False)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Entrenador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=25)),
                ('apellido', models.CharField(default='', max_length=25)),
                ('dni', models.IntegerField(null=True)),
                ('telefono', models.IntegerField(null=True)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Equipo')),
            ],
        ),
    ]
