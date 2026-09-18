# Privacy

Offline scan, redaction, and report generation use local files only. The tool creates no telemetry, startup item, scheduled task, or automatic upload.

`audit --plan` makes no network request. An audit run sends only synthetic benchmark prompts to the explicitly selected configured endpoint. Credentials are read from the named local environment variable and are never written to stdout, reports, or logs.

The redaction command writes a new output file and never overwrites its input. It does not create a reversible mapping.

