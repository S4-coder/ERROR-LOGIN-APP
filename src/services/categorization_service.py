def categorize_error(message, metadata=None):
    """
    Simple categorization logic based on keywords in the error message.
    This can be extended with ML models or more complex rules.
    """
    message = message.lower()
    if 'timeout' in message:
        return 'Timeout Error'
    elif 'connection' in message:
        return 'Connection Error'
    elif 'authentication' in message or 'unauthorized' in message:
        return 'Authentication Error'
    elif 'not found' in message:
        return 'Not Found Error'
    elif 'validation' in message:
        return 'Validation Error'
    else:
        return 'General Error'
