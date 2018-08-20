from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError

CAT_BREED_CHOICES = (
    ('ABYSSINIAN', 'Abyssinian'), ('AMERICAN-CURL', 'American-Curl'), 
    ('AMERICAN-SHORTHAIR', 'American-Shorthair'),('AMERICAN-WIREHAIR', 'American-Wirehair'),('APPLEHEAD-SIAMESE', 'Applehead-Siamese'),('BALINESE', 'Balinese'),('BENGAL', 'Bengal'),('Birman','Birman'),
    ('BOBTAIL','Bobtail'),('BOMBAY', 'Bombay'),('BRITISH-SHORTHAIR','British-Shorthair'),('BURMESE','Burmese'),('BURMILLA','Burmilla'),('CALICO','Calico'),('CANADIAN-HAIRLESS','Canadian-Hairless'),('CHARTEAUX','Chartreux'),('CHAUSIE','Chausie'),('CHINCHILLA','Chinchilla'),('CORNISH-Rex','Cornish-Rex'),('CYMRIC','Cymric'),
    ('DEVON-REX','Devon-Rex'),('DILUTE-CALICO','Dilute-Calico'),
    ('DILUTE-TORTOISESHELL','Dilute-Tortoiseshell'),('DOMESTIC-LONG-HAIR','Domestic-Long-Hair'),('DOMESTIC-MEDIUM-','Domestic-Medium-Hair'), ('DOMESTIC-SHORT-HAIR','Domestic-Short-Hair'),('EGYPTIAN-MAU','Egyptian-Mau'),('Exotic-Shorthair'),('EXTRA-TOES-CAT/HEMINGWAY-POLYDACTYL','Extra-Toes-Cat/Hemingway-Polydactyl'),('HAVANA','Havana'),
    ('HIMALAYAN','Himalayan'),('JAPANESE-BOBTAIL','Japanese-Bobtail'),
    ('JAVANESE','Javanese'),('KORAT','Korat'),('LAPERM','LaPerm'),('MAINE-COON','Maine-Coon'),('MANX','Manx'),('MUNCHKIN','Munchkin'),
    ('NEBELUNG','Nebelung'),('NORWEGIAN-FOREST-CAT','Norwegian-Forest-Cat'),('OCICAT','Ocicat'),('ORIENTAL-LONG-HAIR','Oriental-Long-Hair'),('ORIENTAL-SHORT-HAIR','Oriental Short Hair'),
    ('ORIENTAL-TABBY','Oriental-Tabby'),('PERSIAN','Persian'),('PIXIE-BOB','Pixie-Bob'),('RAGAMUFFIN','Ragamuffin'),('RAGDOLL','Ragdoll'),('RUSSIAN-BLUE','Russian-Blue'),('SCOTTISH-FOLD','Scottish-Fold'),('SELKIRK-REX','Selkirk-Rex'),('SIAMESE','Siamese'),
    ('SIBERIAN','Siberian'),('SILVER','Silver'),('SINGAPURA','Singapura'),('SNOWSHOE','Snowshoe'),('SOMALI','Somali'),('SPHYNX/HAIRLESS-CAT','Sphynx/Hairless-Cat'),('TABBY','Tabby'),('TIGER','Tiger'),
    ('TOKINESE','Tonkinese'),('TORBIE','Torbie'),('TORTOISESHELL','Tortoiseshell'),('TURKISH-ANGORA','Turkish-Angora')
    ('TURKISH_VAN','Turkish_Van'),('TUXEDO','Tuxedo')
)

DOG_BREED_CHOICES = (
    
)

class AnimalType(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)