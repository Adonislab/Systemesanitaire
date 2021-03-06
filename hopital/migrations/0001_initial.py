# Generated by Django 4.0.6 on 2022-07-15 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Depot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_du_produit', models.CharField(choices=[('Pharmaceutique', 'Pharmaceutique'), ('Magazin', 'Magazin'), ('Banque de sang', 'Banque De Sang'), ('Laboratoire', 'Laboratoire'), ('Depot repartiteur', 'Depot Repartiteur')], max_length=20)),
                ('nom_du_produit', models.CharField(max_length=20)),
                ('nombre_de_stoke', models.IntegerField()),
                ('prix_unitaire', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('sexe', models.CharField(choices=[('masculin', 'Masculin'), ('feminin', 'Feminin')], max_length=9)),
                ('numero', models.CharField(max_length=12, unique=True)),
                ('groupe_sangin', models.CharField(choices=[('A', 'Groupea'), ('B', 'Groupeb'), ('AB', 'Groupeab'), ('O', 'Groupeo')], max_length=20)),
                ('rhesus', models.CharField(choices=[('+', 'Facteur Positif'), ('-', 'Facteur Negatif')], max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RessourceHumaine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_agent', models.CharField(choices=[('Infirmier', 'Infirmier'), ('Medecin', 'Medecin'), ('Sage femme', 'Sage Femme'), ('Aide Soignant', 'Aide Soignant'), ('Laboratin', 'Laboratin'), ('Admnistratif', 'Administratif')], max_length=20)),
                ('nom', models.CharField(max_length=10)),
                ('prenom', models.CharField(max_length=50)),
                ('sexe', models.CharField(choices=[('Masculin', 'Masculin'), ('Feminin', 'Feminin')], max_length=10)),
                ('numero', models.CharField(max_length=12, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='service_anexe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_consulte', models.CharField(choices=[('promotion sante', 'Promotion Sante'), ('planification familiale', 'Planification Familiale'), ('service_hygiene', 'Service Hygiene')], max_length=50)),
                ('Offre', models.CharField(max_length=100)),
                ('Demande', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hopital.patient')),
            ],
        ),
        migrations.CreateModel(
            name='resultat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_consulte', models.CharField(choices=[('consultation g??n??rale', 'Consultation Generale'), ('Urgence', 'Urgence'), ('Pediatrie', 'Pediatrie'), ('Radiologie', 'Radiologie'), ('Ecographie', 'Ecographie'), ('Kinesitherapie', 'Kinesitherapie'), ('Chirugie', 'Chirugie'), ('Laboratoire', 'Laboratoire'), ('Maternite', 'Maternite'), ('Dispensaire', 'Dispensaire'), ('Hospitalisation', 'Hospitalisation'), ('Vaccination', 'Vaccination'), ('Gyn??cologie', 'Gynecologie'), ('Dermathologie', 'Dermathologie')], max_length=50)),
                ('resultat_0', models.CharField(max_length=100)),
                ('resultat_1', models.CharField(max_length=100)),
                ('resultat_2', models.CharField(max_length=100)),
                ('commentaire', models.CharField(max_length=100)),
                ('maladie_0', models.CharField(choices=[('paludisme', 'Paludisme'), ('Fievre', 'Fievre'), ('Diarrhe', 'Diarrhe'), ('Fievre jaune', 'Fievre Jaune'), ('Fievre typhoide', 'Fievre Typhoide'), ('Mammographie', 'Mammographie'), ('Regle_douloureuse', 'Regle Douloureuse'), ('Depression', 'Depression'), ('Maladie infantielle', 'Infantille'), ('Trouble audition', 'Audition')], max_length=20)),
                ('categorie_maladie_0', models.CharField(choices=[('rare', 'Rare'), ('tropicale', 'Tropicale'), ('infectieuse', 'Infectieuse'), ('nouvelle', 'Nouvelle'), ('mysterieuse', 'Mysterieuse'), ('mortelle', 'Mortelle')], max_length=20)),
                ('maladie_1', models.CharField(choices=[('paludisme', 'Paludisme'), ('Fievre', 'Fievre'), ('Diarrhe', 'Diarrhe'), ('Fievre jaune', 'Fievre Jaune'), ('Fievre typhoide', 'Fievre Typhoide'), ('Mammographie', 'Mammographie'), ('Regle_douloureuse', 'Regle Douloureuse'), ('Depression', 'Depression'), ('Maladie infantielle', 'Infantille'), ('Trouble audition', 'Audition')], max_length=20)),
                ('categorie_maladie_1', models.CharField(choices=[('rare', 'Rare'), ('tropicale', 'Tropicale'), ('infectieuse', 'Infectieuse'), ('nouvelle', 'Nouvelle'), ('mysterieuse', 'Mysterieuse'), ('mortelle', 'Mortelle')], max_length=20)),
                ('prescription_0', models.CharField(max_length=100)),
                ('prescription_1', models.CharField(max_length=100)),
                ('prescription_2', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hopital.patient')),
            ],
        ),
        migrations.CreateModel(
            name='pronostic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceconsulte', models.CharField(choices=[('consultation g??n??rale', 'Consultation Generale'), ('Urgence', 'Urgence'), ('Pediatrie', 'Pediatrie'), ('Radiologie', 'Radiologie'), ('Ecographie', 'Ecographie'), ('Kinesitherapie', 'Kinesitherapie'), ('Chirugie', 'Chirugie'), ('Laboratoire', 'Laboratoire'), ('Maternite', 'Maternite'), ('Dispensaire', 'Dispensaire'), ('Hospitalisation', 'Hospitalisation'), ('Vaccination', 'Vaccination'), ('Gyn??cologie', 'Gynecologie'), ('Dermathologie', 'Dermathologie')], max_length=22)),
                ('guerison', models.CharField(choices=[('oui', 'Oui'), ('non', 'Non')], max_length=5)),
                ('rechute', models.CharField(choices=[('oui', 'Oui'), ('non', 'Non')], max_length=5)),
                ('sequelle', models.CharField(choices=[('oui', 'Oui'), ('non', 'Non')], max_length=5)),
                ('deces', models.CharField(choices=[('oui', 'Oui'), ('non', 'Non')], max_length=5)),
                ('perte_de_vue', models.CharField(choices=[('oui', 'Oui'), ('non', 'Non')], max_length=5)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hopital.patient')),
            ],
        ),
        migrations.CreateModel(
            name='consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_consulte', models.CharField(choices=[('consultation g??n??rale', 'Consultation Generale'), ('Urgence', 'Urgence'), ('Pediatrie', 'Pediatrie'), ('Radiologie', 'Radiologie'), ('Ecographie', 'Ecographie'), ('Kinesitherapie', 'Kinesitherapie'), ('Chirugie', 'Chirugie'), ('Laboratoire', 'Laboratoire'), ('Maternite', 'Maternite'), ('Dispensaire', 'Dispensaire'), ('Hospitalisation', 'Hospitalisation'), ('Vaccination', 'Vaccination'), ('Gyn??cologie', 'Gynecologie'), ('Dermathologie', 'Dermathologie')], max_length=50)),
                ('symptome_0', models.CharField(max_length=100)),
                ('symptome_1', models.CharField(max_length=100)),
                ('symptome_2', models.CharField(max_length=100)),
                ('observation_0', models.CharField(max_length=100)),
                ('observation_1', models.CharField(max_length=100)),
                ('observation_2', models.CharField(max_length=100)),
                ('symdrome_0', models.CharField(max_length=50)),
                ('symdrome_1', models.CharField(max_length=50)),
                ('symdrome_2', models.CharField(max_length=50)),
                ('commentaire', models.CharField(max_length=100)),
                ('paraclinique_0', models.CharField(max_length=500)),
                ('paraclinique_1', models.CharField(max_length=500)),
                ('paraclinique_3', models.CharField(max_length=500)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hopital.patient')),
            ],
        ),
        migrations.CreateModel(
            name='constante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poids', models.IntegerField()),
                ('temperature', models.IntegerField()),
                ('taille', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hopital.patient')),
            ],
        ),
    ]
