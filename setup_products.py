import os
import django
import shutil

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'corro.settings')
django.setup()

from products.models import Category, Product
from django.conf import settings

def create_products():
    # Créer les dossiers media si nécessaire
    media_products_path = os.path.join(settings.MEDIA_ROOT, 'products')
    os.makedirs(media_products_path, exist_ok=True)

    # Créer les catégories
    categories = {
        'Vêtements': 'vetements',
        'Accessoires': 'accessoires',
        'Bijoux': 'bijoux'
    }
    
    for name, slug in categories.items():
        Category.objects.get_or_create(name=name, slug=slug)
    
    # Liste des produits avec les noms exacts des images
    products = [
        {
            'category': 'Vêtements',
            'name': 'Pull Cable-Knit Cambridge',
            'slug': 'pull-cable-knit-cambridge',
            'description': 'Confectionné en pure laine mérinos, ce pull torsadé incarne l\'élégance des campus prestigieux. Son motif cable-knit traditionnel et sa coupe classique en font une pièce intemporelle de la garde-robe old money.',
            'price': 295.00,
            'image': 'pull.webp',  # Image existante
            'stock': 50,
            'available': True
        },
        {
            'category': 'Vêtements',
            'name': 'T-shirt Pima Oxford',
            'slug': 't-shirt-pima-oxford',
            'description': 'T-shirt en coton Pima de qualité supérieure. Coupe droite et col rond parfaitement ajusté, idéal sous un blazer ou porté seul.',
            'price': 85.00,
            'image': 'tshirt.webp',  # Image existante
            'stock': 75,
            'available': True
        },
        {
            'category': 'Vêtements',
            'name': 'Pantalon Lin Hampton',
            'slug': 'pantalon-lin-hampton',
            'description': 'Pantalon en lin italien de première qualité. Coupe droite et élégante, parfait pour les journées ensoleillées. Un basique raffiné du style preppy.',
            'price': 245.00,
            'image': 'pentalon.webp',  # Corrigé
            'stock': 40,
            'available': True
        },
        {
            'category': 'Accessoires',
            'name': 'Montre Legacy Classic',
            'slug': 'montre-legacy-classic',
            'description': 'Montre automatique au design épuré avec bracelet en cuir pleine fleur. Cadran blanc cassé et index dorés, symbole d\'une élégance discrète.',
            'price': 890.00,
            'image': 'montre.webp',  # Image existante
            'stock': 15,
            'available': True
        },
        {
            'category': 'Accessoires',
            'name': 'Écharpe Cachemire Wellington',
            'slug': 'echarpe-cachemire-wellington',
            'description': 'Écharpe en pur cachemire écossais. Motif tartan classique dans des tons neutres, frangée main.',
            'price': 245.00,
            'image': 'echarpe.webp',  # Corrigé
            'stock': 30,
            'available': True
        },
        {
            'category': 'Accessoires',
            'name': 'Mocassins Princeton',
            'slug': 'mocassins-princeton',
            'description': 'Mocassins en cuir cordovan, cousus Goodyear. Le summum du style preppy, parfaits du campus au country club.',
            'price': 495.00,
            'image': 'chaussures.webp',  # Corrigé
            'stock': 25,
            'available': True
        },
        {
            'category': 'Bijoux',
            'name': 'Bracelet Nautical Knot',
            'slug': 'bracelet-nautical-knot',
            'description': 'Bracelet en cordage marin et fermoir en laiton patiné. Un accessoire casual chic qui évoque les étés dans les Hamptons.',
            'price': 125.00,
            'image': 'bracelet.webp',  # Image existante
            'stock': 45,
            'available': True
        },
        {
            'category': 'Bijoux',
            'name': 'Bague Chevalière Heritage',
            'slug': 'bague-chevaliere-heritage',
            'description': 'Chevalière en argent sterling, finition satinée. Un classique intemporel qui se transmet de génération en génération.',
            'price': 175.00,
            'image': 'bague-heritage.jpg',  # Corrigé
            'stock': 20,
            'available': True
        }
    ]
    
    # Créer les produits
    for product_data in products:
        source_image = os.path.join(media_products_path, product_data['image'])
        
        if os.path.exists(source_image):
            print(f"Image trouvée : {product_data['image']}")
            
            # Créer le produit
            category = Category.objects.get(name=product_data['category'])
            product, created = Product.objects.get_or_create(
                category=category,
                name=product_data['name'],
                slug=product_data['slug'],
                defaults={
                    'description': product_data['description'],
                    'price': product_data['price'],
                    'image': f"products/{product_data['image']}",
                    'stock': product_data['stock'],
                    'available': product_data['available']
                }
            )
            
            if created:
                print(f"Produit créé : {product_data['name']}")
            else:
                print(f"Produit mis à jour : {product_data['name']}")
        else:
            print(f"ATTENTION : Image manquante : {product_data['image']}")

if __name__ == "__main__":
    create_products() 