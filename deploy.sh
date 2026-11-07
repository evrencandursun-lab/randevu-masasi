#!/bin/bash
# Randevu Masası → Firebase Hosting (randevu-masasi.web.app)
# Kullanım (Cloud Shell): git clone https://github.com/evrencandursun-lab/randevu-masasi rm && bash rm/deploy.sh
set -e
cd "$(dirname "$0")"
rm -rf _site && mkdir -p _site
cp index.html _site/index.html
base64 -d onay.jpg.b64 > _site/onay.jpg
cat > firebase.json <<'J'
{"hosting":{"public":"_site","rewrites":[{"source":"/y/**","destination":"/index.html"}],"headers":[{"source":"**","headers":[{"key":"Cache-Control","value":"no-cache"}]}]}}
J
firebase deploy --only hosting --project randevu-masasi --non-interactive
echo "BITTI: https://randevu-masasi.web.app"
