# -*- coding: utf-8 -*-
{
    "name": "meta baatighar design",
    "summary": "An eCommerce design that is suitable for Baatighar design.",
    "description": """
        An eCommerce design that is suitable for Baatighar design.
    """,
    "author": "Ahosan from Metamorphosis Limited",
    "website": "https://www.metamorphosis.com.bd",
    "category": "Uncategorized",
    "licence": "AGPL-3",
    "version": "17.0.0.1",
    "depends": ["theme_prime", "website", "website_sale"],
    "assets": {
        "web.assets_frontend": [
            "/meta_baatighar_design/static/src/css/product_page.css",
            "/meta_baatighar_design/static/src/js/related_product_slide.js",
        ],
    },
    "data": [
        # 'security/ir.model.access.csv',
		'views/product_page.xml',
		'views/magnetic_content_field.xml',
    ],
    "sequence": 10,
    "installable": True,
    "application": True,
}

