### Steps before upload to Github
* sed -i 's/pwd=.*/pwd="ChangeMe"/' ./scripts/getprofiles.py
* sed -i 's/.*"bindPassword": ".*/"        bindPassword": "ChangeMe",/' ./helm-chart/config/ad.json
* helm-chart/templates/dremio-registry-secrets.yaml
