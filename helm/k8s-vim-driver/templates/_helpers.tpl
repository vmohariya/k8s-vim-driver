{{/*
Generate SSL certificate
*/}}
{{- define "gen-cert" -}}
{{- $cert := genSelfSignedCert "k8s-vim-driver" nil nil 3650 -}}
tls.crt: {{ $cert.Cert | b64enc }}
tls.key: {{ $cert.Key | b64enc }}
{{- end -}}