from src.log_parser import parse_logs

def test_parse_logs():
    events = parse_logs("logs/sample_auth.log")
    assert len(events) > 0
