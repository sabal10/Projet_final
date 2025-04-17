import pytest
from app.services.commands.send_notification_command import SendNotificationCommand
from app.services.commands.command_invoker import CommandInvoker
from app.services.commands.resolve_report_command import ResolveReportCommand

class MockNotificationService:
    def __init__(self):
        self.sent_data = None

    def send(self, data):
        self.sent_data = data
        return "Mock notification sent"

def test_send_notification_command_executes_successfully():
    service = MockNotificationService()
    report = {
        "name": "Test",
        "pollution_type": "Plastiques",
        "description": "Test description",
        "location": "Zone Test",
        "quantity": 20,
        "responder_name": "Agent Test",
        "responder_email": "test@example.com",
        "created_at": "2025-04-17 00:00:00",
        "severity": "Modéré",
        "status": "En attente",
        "source": "test",
        "channel": "console"
    }

    command = SendNotificationCommand(service, report)
    invoker = CommandInvoker()
    invoker.add_command(command)
    invoker.run()

    assert service.sent_data == report

def test_resolve_report_command_updates_report_manager():
    updated = {}

    class MockReportManager:
        def resolve_report(self, report_id):
            updated["called"] = True
            updated["id"] = report_id

    command = ResolveReportCommand(MockReportManager(), 42)
    command.execute()

    assert updated["called"] is True
    assert updated["id"] == 42
