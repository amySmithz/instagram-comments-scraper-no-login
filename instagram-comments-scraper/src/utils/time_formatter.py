thonfrom datetime import datetime

def format_timestamp(timestamp):
    """
    Formats an Instagram timestamp into a human-readable format.
    :param timestamp: Unix timestamp from Instagram
    :return: Human-readable date
    """
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')