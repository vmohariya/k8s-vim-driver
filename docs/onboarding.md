# Onboard in to LM

The following guide details how to onboard the VIM driver in to LM using [lmctl](https://github.com/accanto-systems/lmctl).

Onboard the VIM driver:

```
lmctl vimdriver add --type Kubernetes --url http://k8s-vim-driver:8294 dev
```

Create a Kubernetes [deployment location](http://servicelifecyclemanager.com/reference/lm-api/api-definition/deployment-location-api/) called "my_dl" that uses the VIM driver with deployment location configuration provided by dl.json:

```
# assumes that you've onboarded Brent using the name "brent".
lmctl deployment add -r brent -i Kubernetes -p dl.json dev my_dl
```

where dl.json looks like this (for a [Kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm/) Kubernetes installation):

```
{
  "k8s-server": "https://10.220.217.180:6443",
  "k8s-username": "admin",
  "k8s-certificate-authority-data": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUN5RENDQWJDZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQkFRc0ZBREFWTVJNd0VRWURWUVFERXdwcmRXSmwKY201bGRHVnpNQjRYRFRFNU1UQXhNakV5TURZeU1Gb1hEVEk1TVRBd09URXlNRFl5TUZvd0ZURVRNQkVHQTFVRQpBeE1LYTNWaVpYSnVaWFJsY3pDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2dnRUJBT3pPCmtRSWlONFRrZ0c5R2VzWnFqUkJZT1V1aTBORVhIZjBJK21HZ0RBUFF3Q05RZFdnTUc4djA2bnRnYnJpWjFoSHoKdXV5UkV2ckNkQ3U2ZVllVUdyRVkvelRSNVBiYVQxRDIyNklrSHFzREFSREpzcXpyLzh2NFNqeENES3duNU1GZgphQUNGQTVOMDBObmFJUFlOK2NmRVBoaHFKTGFQbk9NUTg3YVBFa3dweTVpVHlWakdaZVNVTkZ6RlMzczUwRzJQCjNmcC81SjFRM3Vja012REcwQTlGb3FiQ2lrQlFld3VUaFhwL01TSnhyeEV4YU5nbis5alU1U0JZUGoyUDJLUE0KbitvaGZVcWEwVitVNU9ibm9lNjVKWnpqYzA1Qk44Nk42WUJYYzNDVnVuTUsvQUdsR0dBdm9YRFJ4TDY2Z0RHQQo2NXJjYVFER1FueEJsNmc2aWNzQ0F3RUFBYU1qTUNFd0RnWURWUjBQQVFIL0JBUURBZ0trTUE4R0ExVWRFd0VCCi93UUZNQU1CQWY4d0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFKblhZSmpUcTlZNzFMSmlrb25wU1RQQW93dUUKem5NN1JoanpjejN1eGZDZnE2bm1EcVU2MUJGNFlDaFAyNkd6YWJDRnkwOUpDZUw4WEVtUW4vRmhHdUlHV0JHbQprUUV0cmI1TFdQajdheFZ6ODJCT2R3Wmk5N1Y1U3N6Z1I0dEFvQnlWTHp6OEZRSnAyanF6RU1OYkM1QzZpYXdOCm12aXRqRENHb0JuL2taaDlYWG4rMFhkemVGdytOOHlnSXRtMnFyZ2tYeUJ0SDlnSncySDdCcG8xRUhhSWticlYKNURRWmdzSlNYRHdVMVR2RUdzWXhtTVJ0VCtMcFFWYTZaT3VWcm1LZlgrSlVRbkZjYVljMXVSSG1MVnhOcm5HNQpldndGMlAwZlpwdXBUY2tGUzBiOHV0TFhZS1lUVkliQnA5ZFZFbVdMMlQ3VlFMVllXNUY0UVRuT21WMD0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=",
  "k8s-client-certificate-data": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUM4akNDQWRxZ0F3SUJBZ0lJTDFkU1BjRWRubUF3RFFZSktvWklodmNOQVFFTEJRQXdGVEVUTUJFR0ExVUUKQXhNS2EzVmlaWEp1WlhSbGN6QWVGdzB4T1RFd01USXhNakEyTWpCYUZ3MHlNREV3TVRFeE1qQTJNalJhTURReApGekFWQmdOVkJBb1REbk41YzNSbGJUcHRZWE4wWlhKek1Sa3dGd1lEVlFRREV4QnJkV0psY201bGRHVnpMV0ZrCmJXbHVNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQTFJRDNjMjVNNHh2QndvbU4KTkpwNGF1a1BCWnd5SG10Y2UvYXJWMDN3bGcxdUh6QU1ON21vb1VPUlVXQUxzZ29FQ2pPL1FSYlRFM0pSMHk2dQpuejY4QnFFeDhPeGdHdW5YTjNPSDhKYmlHaEd5dEE5dVRJekhRODZZeXVhUktETTBwZ2UvRWJkV3J6dHhWRy9OCnZjQlI2eGlpOXVKN2lYZDJPdmw1ay9wYnpxeTNuekJRdFE0enBURUUvT0tsc2FXU0xOcllTUFBNdG5ldVVGYVAKQTdGZC9HLzVaWGFnOCtwTWtSVlg1aXhIaGkzYTI1OXRkTDdsLzF3WTYwaVJibGV6bHhMNjV1dDJVbUdHZHdpVwpoY09TemxPc3BzVVp1bk5tZFJ4M05DVElsYkVwYm1SZnpRK0hETGZUZE5sVm9zQXQwSUN3YmVjVHJSRGU2TThYCmxpVzNOUUlEQVFBQm95Y3dKVEFPQmdOVkhROEJBZjhFQkFNQ0JhQXdFd1lEVlIwbEJBd3dDZ1lJS3dZQkJRVUgKQXdJd0RRWUpLb1pJaHZjTkFRRUxCUUFEZ2dFQkFCYk9ZLzMzNFdVNmpGTlg3emRUdC9ETGU4Zm9QdEo0MEI4OApOVUozSXk4VGp1aEtodkZOMWRmT3kzQldEYWdzUFMzeXI4RDRuc1VMSHFMK0V0SjhtOVhhOXFqcUQ4MlB2Ulc2Cll0d1B3Y0hieXpZbDFtckRIRnl6SmxNWVh0UGtqSFRMU1kySkJhYjVEcWpaeDZFTmRzbVRSQnBSb29HNzJTWEYKSVptY0VCNytncm9maGlxRFVCd3ZMaGp6cVhzUE80alBKZFpoOFVYVk5mUjMvT0dvRkxPLzBaL05XRW5HS0dEWQp2OTZJZFp0UGxIRERXM1hReTl4NkdtSU5PNG5RZnNTeGNQV1E4Y0RWbEN0aWlZQUw0ZE9rMnI4K1JSN1dBMFBCClRpZUN0WTF6bERPQ0JXVjAxN0VkYXllRmtMeUR2ZmRJdUk5QlBucTJPNkMrb3I5NVpMYz0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=",
  "k8s-client-key-data": "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFcFFJQkFBS0NBUUVBMUlEM2MyNU00eHZCd29tTk5KcDRhdWtQQlp3eUhtdGNlL2FyVjAzd2xnMXVIekFNCk43bW9vVU9SVVdBTHNnb0VDak8vUVJiVEUzSlIweTZ1bno2OEJxRXg4T3hnR3VuWE4zT0g4SmJpR2hHeXRBOXUKVEl6SFE4Nll5dWFSS0RNMHBnZS9FYmRXcnp0eFZHL052Y0JSNnhpaTl1SjdpWGQyT3ZsNWsvcGJ6cXkzbnpCUQp0UTR6cFRFRS9PS2xzYVdTTE5yWVNQUE10bmV1VUZhUEE3RmQvRy81WlhhZzgrcE1rUlZYNWl4SGhpM2EyNTl0CmRMN2wvMXdZNjBpUmJsZXpseEw2NXV0MlVtR0dkd2lXaGNPU3psT3Nwc1VadW5ObWRSeDNOQ1RJbGJFcGJtUmYKelErSERMZlRkTmxWb3NBdDBJQ3diZWNUclJEZTZNOFhsaVczTlFJREFRQUJBb0lCQVFDTkRIMHkxUWVieHhTNAo5MndPZW1sckxQNlhqckdGbDJWdnNxN1A2Qi9FdVcxYXJoMnQ3MEdLcUxxUDlOeE9kRzl5Qmg3d0tTSTVTaXdkCnJHS2p1SlE5SWtsdnpMV05wNkQrWVdUZHdJaWJIUndzZ0FHS05mY2Rmc2ZVQlc1YjdJRUpveUtqczdtSjNqNisKK09ickIvaFh2NmFMa0pESEVkQWNIUE1oMFkrV2diK1lxb09tWm55cmVwMThvQWZ2RmJ4dzBOdlI5dHhtVzNTbApWUjJsV0tDY3J2TEMzUVlNUEVMTnNEUCt6V2RQMCtqdml5eDN1OCtNUWZqb3BnZjdEenJNanFjTWFLUEVRR3lLCldzMFVFbTd3VmxQQmU2bWpQbkVNaUJJMDljS0NVT0ozR2xRZkNONkNKTGNpWjNoZ0RCSUloUDhDNWZhdG13THUKRXB0enZVV1JBb0dCQU5uNHA3WnJ1SmswZFRpMEtKelFsYXUyZHNENzQ5Z1I1Zm9iakNhNnBUUDR3d09XcnBvYwpEMjkyckxjYmJubWROekEzZC9ack9CODFkbHlKODU5TGFFRldJUE5aT3k3MGQydmd1aFU1eEdHQmx1YzgrZkg0ClpjdkRHVWhHV0JzbnRiZ2piMkVxbm9FZm5qOEdZT3EycUsyL2V2dnRNSWdLMzFNbGdhNmVCSlFmQW9HQkFQbVUKSE50d3dHOHZkZkxNNVdxQmRKV29TZU1TZW53Y0ZYRGdZM2pSMDQvWGVEdThMNU1vdWIrTWQ0cnR6dUhSVzNZYQpSMFNNd3ZrZUJYQU1IMWRPVXhyTmtQT3c2QmQxRGFzaG55STVlVHNmam1WMjRxZFVOc1pBTmw0QTJBRGhHUFVZCk9SL3Brd0dUdU9SL1BUNmxXYzBFR3JxeHllam5DZXl4OTd6NGRHb3JBb0dCQUt3bzlMWmxvTGtKTU9qbml3aEkKeTE2RDBJb2VxZGc0VXMvWHdEdTZ3YzhwMVVYWlZ2RUw1cmtnSDh6RVV0NmxhVGloSnhRdm5YVXc4ZHFuYncvTApMSDRtZkFJWTRXRDEzL2tKMTQvNlAzelFNUk5WR3dtZUt6RGtXT3kzK3RELzdVeVNXRitEblF2Wm9GQ2hSaDA4CnhqL3RkRUxWRmJidDkzUWh0S3JwemkzN0FvR0JBTURFaUtGcGJnaXl0THhMUytzK2dBalR5ZlhzSU5UWmNDb1YKOWw2c1dtYmdld3BRYU1LV0V4b0M2WlpSNVpmL2QxQTZMYytobFRxSzJKSlptcDk1YkxEb0U4eFZXSDQ5dDhmMQpHUTk3S3NyaXJiNXEyOWQ0TVRKaENGMEU4OUdDQ3gvTGpOdThNZ0ptMGNrVENmL29BUHRiN3pWQit2eTc3cXQyCkxpNDBETjZ2QW9HQVI0dUw5MHdCUndKR3JSVkRtMG5Lc21rMmNWTjN0VEpNR2k5Skp6eWlEWGhzVHEvVmdJTnQKZGw5aTg2eGM5NS96WFA1UWRVRlErVVJrV2dsakV2YlBTMzVIQTlrOUdhbE9KS09OTnpqNGtjTGVHMHhjUTFUcQpycXhkOFhkNGJYYVVKaUpsZUh1aU45blFBWUNzdlZHYnhQSnZpWjFXTTZSY1pYK0tOMkJ1TVpnPQotLS0tLUVORCBSU0EgUFJJVkFURSBLRVktLS0tLQo=",
  "k8s-namespace": "default"
}
```