def send_alert(error_log):
    """
    Send alert to developers about the new error.
    This is a placeholder for integration with email, Slack, or other alerting tools.
    For now, it just prints to console.
    """
    alert_message = f"ALERT: New error logged! ID: {error_log.id}, Category: {error_log.category}, Message: {error_log.message}"
    print(alert_message)
    # TODO: Integrate with real alerting system (email, Slack, etc.)
