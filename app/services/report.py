from app.services.templates.report_service import ReportService
from ..controllers import ReportController

report = ReportService(ReportController).template_service('report', __name__)
