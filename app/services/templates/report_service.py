from app.services.templates.abstract_service import AbstractService
from app.utils.services_responses import services_response

class ReportService(AbstractService):
    def __init__(self, controller):
        self.controller = controller
    
    def get(self) -> tuple:
        report, error = self.controller.get_report()
        return services_response(report, error)