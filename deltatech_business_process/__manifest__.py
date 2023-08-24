# ©  2023 Deltatech
# See README.rst file on addons root folder for license details


{
    "name": "Business process",
    "summary": "Business process",
    "version": "15.0.1.0.0",
    "author": "Terrabit, Dorin Hongu",
    "website": "https://www.terrabit.ro",
    "license": "OPL-1",
    "category": "Generic Modules/Other",
    "depends": ["account"],
    "data": [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/business_area_view.xml",
        "views/business_role_view.xml",
        "views/business_development_type_view.xml",
        "views/business_transaction_view.xml",
        "views/business_project_view.xml",
        "views/business_process_view.xml",
        "views/business_process_step_view.xml",
        "views/business_development_view.xml",
        "views/business_process_test_view.xml",
    ],
    "development_status": "Beta",
    "images": ["static/description/main_screenshot.png"],
    "maintainers": ["dhongu"],
    "application": True,
}
