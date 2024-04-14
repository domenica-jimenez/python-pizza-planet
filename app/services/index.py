from app.services.templates.index_service import IndexService
from ..controllers import IndexController

index = IndexService(IndexController).template_service('index', __name__)
