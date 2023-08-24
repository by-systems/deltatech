# ©  2023 Deltatech
# See README.rst file on addons root folder for license details


from . import business_area
from . import business_development_type
from . import business_process
from . import business_process_test
from . import business_transaction
from . import business_development
from . import business_project
from . import business_role
from . import business_open_issue


TEST_SCOPE = [
    ("internal", "Internal"),
    ("integration", "Integration"),
    ("user_acceptance", "User Acceptance"),
    ("regression", "Regression"),
    ("other", "Other"),
]
