# ©  2015-2020 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details
{
    "name": "eCommerce Sale Order status",
    "category": "Website/Website",
    "summary": "Additional filters sales orders by status ",
    "version": "13.0.1.0.0",
    "license": "LGPL-3",
    "author": "Terrabit, Dorin Hongu",
    "website": "https://www.terrabit.ro",
    "depends": ["website_sale_stock", "deltatech_delivery_status", "deltatech_widget_badge"],
    "data": ["views/sale_view.xml", "views/assets.xml"],
    "qweb": ["static/src/xml/*.xml"],
    "images": ["static/description/main_screenshot.png"],
    "installable": True,
    "development_status": "Mature",
    "maintainers": ["dhongu"],
}
