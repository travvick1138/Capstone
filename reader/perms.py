from permission.logics import AuthorPermissionLogic
from permission.logics import CollaboratorsPermissionLogic

PERMISSION_LOGICS = (
    ('your_app.Article', AuthorPermissionLogic()),
    ('your_app.Article', CollaboratorsPermissionLogic()),
)
