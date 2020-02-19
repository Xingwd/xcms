#!/usr/bin/env bash

# 编译admin
echo '########## Building admin ##########'
cd admin
npm install
npm run build
cd ..

# 编译web
echo '########## Building web ##########'
cd web
npm install
npm run build
cd ..

# 打包
echo '########## Packing ##########'

if [ -d './build' ]; then
  rm -rf ./build
fi

mkdir -p build/xcms
cp -rf admin/dist build/xcms/admin
cp -rf web/dist build/xcms/web

mkdir build/xcms/server
cp -rf server/main server/migrations build/xcms/server/
cp server/config.py server/.env server/requirements.txt server/xcms.py build/xcms/server/

cd build/
tar czf xcms.tar.gz xcms
cd ..

echo '########## Finished ##########'
