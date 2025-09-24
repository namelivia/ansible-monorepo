{{- if . }}
{{- range . }}
### Target `{{ escapeXML .Target }}`

{{- if (eq (len .Vulnerabilities) 0) }}
#### No Vulnerabilities found
{{- else }}
#### Vulnerabilities ({{ len .Vulnerabilities }})

| Package | ID | Severity | Installed Version | Fixed Version |
| :--- | :--- | :--- | :--- | :--- |
{{- range .Vulnerabilities }}
| `{{ escapeXML .PkgName }}` | {{ escapeXML .VulnerabilityID }} | {{ escapeXML .Severity }} | {{ escapeXML .InstalledVersion }} | {{ escapeXML .FixedVersion }} |
{{- end }}
{{- end }}

{{- if (eq (len .Misconfigurations ) 0) }}
#### No Misconfigurations found
{{- else }}
#### Misconfigurations

| Type | ID | Check | Severity | Message |
| :--- | :--- | :--- | :--- | :--- |
{{- range .Misconfigurations }}
| {{ escapeXML .Type }} | {{ escapeXML .ID }} | {{ escapeXML .Title }} | {{ escapeXML .Severity }} | {{ escapeXML .Message }} ({{ escapeXML .PrimaryURL }}) |
{{- end }}
{{- end }}
{{- end }}
{{- else }}
### Trivy Returned Empty Report
{{- end }}
