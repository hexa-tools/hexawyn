SELECT COUNT(*) FROM incidents WHERE timestamp < now() - INTERVAL '1 day' * ?
