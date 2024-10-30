from flask import Flask, render_template

app = Flask(__name__)

# Example data structure for products and product groups
products = [
    {"name": "Product 1", "image": "image1.jpg", "slug": "extracao-dna-rna-magnetica", "featured": True},
    {"name": "Product 2", "image": "image2.jpg", "slug": "lise-rapida", "featured": False},
    # Add more products as needed
]

product_groups = [
    {"title": "Extração de DNA e RNA", "subtitle": "Linha Sabiá", "slug": "extracao-dna-rna", "descriptionExcerpt": "Descrição breve..."},
    {"title": "Acessórios", "subtitle": "Racks Magnéticas", "slug": "acessorios", "descriptionExcerpt": "Descrição breve..."},
    # Add more product groups as needed
]

section_colors = [
    "bg-amber-500",
    "bg-amber-900",
    "bg-teal-700",
    "bg-teal-500",
    "bg-amber-400",
]

@app.route('/catalog')
def catalog():
    # Zip the product groups with section colors in Python
    product_groups_with_colors = list(zip(product_groups, section_colors))
    
    return render_template(
        'catalog.html',
        title="Microforge - Confira nossos produtos",
        description="Insumos para biomol. Kits de extração de DNA e RNA, Lise Celular, Agarose, Racks Magnéticas à pronta entrega.",
        products=products,
        product_groups_with_colors=product_groups_with_colors
    )

if __name__ == '__main__':
    app.run(debug=True)
